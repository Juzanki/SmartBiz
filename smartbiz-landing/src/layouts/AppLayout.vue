<template>
  <div :class="themeClass">
    <!-- 🔝 Navbar -->
    <header class="bg-white dark:bg-gray-900 shadow">
      <div class="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        <!-- Logo + App Name -->
        <div class="flex items-center gap-3">
          <img src="/assets/logo.svg" alt="SmartBiz" class="w-10 h-10 rounded" />
          <span class="text-xl font-bold text-blue-900 dark:text-white">SmartBiz</span>
        </div>

        <!-- Lang & Theme Switcher -->
        <div class="flex gap-4">
          <LanguageSwitcher />
          <ThemeSelector />
        </div>
      </div>
    </header>

    <!-- 🌐 Main Content -->
    <main class="min-h-screen py-10 px-6 max-w-6xl mx-auto">
      <slot />
    </main>

    <!-- 🔻 Footer (optional) -->
    <footer class="text-center text-gray-500 text-sm py-6 dark:text-gray-400">
      © 2025 SmartBiz Assistance — All rights reserved
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import LanguageSwitcher from '@/components/LanguageSwitcher.vue'
import ThemeSelector from '@/components/ThemeSelector.vue'

const theme = ref(localStorage.getItem('theme') || 'light')

const themeClass = computed(() => theme.value === 'dark' ? 'theme-dark' : 'theme-light')

onMounted(() => {
  document.body.className = themeClass.value
})
</script>

<style>
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
