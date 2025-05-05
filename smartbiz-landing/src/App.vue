<template>
  <div :class="themeClass">
    <header class="bg-white py-6 shadow">
      <div class="max-w-6xl mx-auto px-4 flex items-center justify-between">
        <!-- Logo + Greeting -->
        <div class="flex items-center gap-6">
          <img
            alt="SmartBiz logo"
            class="logo"
            src="./assets/logo.svg"
            width="80"
            height="80"
          />
          <UserGreeting :msg="$t('welcome')" />
        </div>

        <!-- Language + Theme Switchers -->
        <div class="flex items-center gap-4">
          <LanguageSwitcher />
          <select v-model="theme" @change="switchTheme" class="theme-selector">
            <option value="light">☀️ Light</option>
            <option value="dark">🌙 Dark</option>
          </select>
        </div>
      </div>
    </header>

    <!-- Role-based Navigation -->
    <nav class="max-w-6xl mx-auto px-4 py-4 flex gap-4">
      <router-link v-if="isLoggedIn" to="/dashboard">📊 Dashboard</router-link>
      <router-link v-if="role === 'admin'" to="/dashboard/admin">🛠️ Admin Panel</router-link>
      <router-link v-if="role === 'owner'" to="/dashboard/owner">👑 Owner Controls</router-link>
    </nav>

    <!-- ✅ Hii hapa ndiyo imebadilishwa -->
    <main class="max-w-6xl mx-auto px-4 py-10">
      <router-view />
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import UserGreeting from "./components/UserGreeting.vue"
import LanguageSwitcher from "./components/LanguageSwitcher.vue"

// 🌙 Theme logic with system detection fallback
const detectSystemTheme = () =>
  window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'

const theme = ref(localStorage.getItem('theme') || detectSystemTheme())
const themeClass = computed(() => theme.value === 'dark' ? 'theme-dark' : 'theme-light')

const switchTheme = () => {
  localStorage.setItem('theme', theme.value)
  document.body.className = themeClass.value
}

onMounted(() => {
  document.body.className = themeClass.value

  // Listen to system theme changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) {
      theme.value = e.matches ? 'dark' : 'light'
      document.body.className = themeClass.value
    }
  })
})

// 🔐 Role-based nav display
const isLoggedIn = ref(!!localStorage.getItem("access_token"))
const role = ref(localStorage.getItem("user_role") || "")
</script>

<style>
.logo {
  display: block;
}

.theme-selector {
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 0.9rem;
}

/* 🌙 Theme styles */
.theme-light {
  --bg-color: #ffffff;
  --text-color: #111111;
}

.theme-dark {
  --bg-color: #0d1117;
  --text-color: #f0f0f0;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: all 0.3s ease-in-out;
}
</style>
