<template>
  <div class="dashboard-layout flex min-h-screen">
    <!-- Sidebar -->
    <aside
      :class="[
        'bg-white dark:bg-gray-900 text-gray-800 dark:text-white shadow-md transition-all duration-300 ease-in-out',
        collapsed ? 'w-16' : 'w-64'
      ]"
      class="h-screen px-4 py-6 relative"
    >
      <!-- Sidebar Header -->
      <div class="flex items-center justify-between mb-6">
        <h2 v-if="!collapsed" class="text-xl font-bold">SmartBiz</h2>
        <button @click="toggleSidebar" class="text-2xl focus:outline-none">
          {{ collapsed ? '☰' : '×' }}
        </button>
      </div>

      <!-- Navigation Links -->
      <nav class="flex flex-col gap-4 text-sm">
        <router-link class="hover:text-blue-600" to="/dashboard">
          📊 {{ $t('dashboard') }}
        </router-link>

        <router-link
          v-if="role === 'admin'"
          class="hover:text-blue-600"
          to="/admin"
        >
          👥 {{ $t('users') }}
        </router-link>

        <router-link
          v-if="role === 'owner'"
          class="hover:text-blue-600"
          to="/owner"
        >
          ⚙️ {{ $t('settings') }}
        </router-link>

        <button @click="logout" class="text-left text-red-600 hover:text-red-400">
          🔓 {{ $t('logout') }}
        </button>
      </nav>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 bg-gray-50 dark:bg-gray-800 text-gray-800 dark:text-white p-6 overflow-y-auto">
      <slot />
    </main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      collapsed: window.innerWidth < 768
    }
  },
  computed: {
    role() {
      return localStorage.getItem('user_role') || ''
    }
  },
  methods: {
    toggleSidebar() {
      this.collapsed = !this.collapsed
    },
    logout() {
      localStorage.clear()
      this.$router.push('/login')
    },
    handleResize() {
      this.collapsed = window.innerWidth < 768
    }
  },
  mounted() {
    window.addEventListener('resize', this.handleResize)
  },
  beforeUnmount() {
    window.removeEventListener('resize', this.handleResize)
  }
}
</script>

<style scoped>
.dashboard-layout {
  background-color: var(--bg-color);
  color: var(--text-color);
  transition: background 0.3s, color 0.3s;
}
</style>
