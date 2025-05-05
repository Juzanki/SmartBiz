<template>
  <div class="min-h-screen bg-[#0d1b2a] text-[#e0e1dd]">
    <!-- Top Navbar -->
    <header class="flex justify-between items-center px-6 py-3 bg-[#1b263b] shadow-md">
      <div class="flex items-center gap-3">
        <button @click="toggleSidebar" class="text-yellow-400 text-3xl focus:outline-none">
          ☰
        </button>
        <img
          src="@/assets/logo-circle.png"
          alt="SmartBiz Logo"
          class="w-10 h-10 rounded-full border-2 border-yellow-400 bg-white shadow-md object-contain"
        />
        <h1 class="text-yellow-400 font-bold text-lg hidden sm:block">SmartBiz</h1>
      </div>
      <div class="text-sm sm:text-lg font-semibold text-yellow-400">OWNER PANEL</div>
    </header>

    <!-- Sidebar -->
    <aside :class="['fixed top-0 left-0 h-full w-60 z-40 bg-[#1b263b] text-[#e0e1dd] pt-16 px-4 transform transition-transform duration-300', { '-translate-x-full': !isSidebarOpen }]">
      <ul class="space-y-3">
        <li v-for="link in links" :key="link.name" @click="navigate(link.path)" :class="['cursor-pointer p-3 rounded hover:bg-[#778da9]', { 'bg-[#f4d160] text-black font-bold': currentPage === link.path, 'bg-[#415a77]': currentPage !== link.path }]">
          <span class="mr-2">{{ link.icon }}</span>{{ link.name }}
        </li>
      </ul>
    </aside>

    <!-- Main Content -->
    <main class="ml-0 md:ml-60 px-6 pt-6 pb-20">
      <h2 class="text-2xl font-bold text-[#f4d160] mb-6">{{ currentTitle }}</h2>

      <div v-if="currentPage === '/dashboard/owner'" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="bg-[#415a77] p-4 rounded-lg shadow-md text-center">
          <h3 class="text-white text-xl font-semibold">3,210</h3>
          <p class="text-[#d9d9d9]">Total Users</p>
        </div>
        <div class="bg-[#415a77] p-4 rounded-lg shadow-md text-center">
          <h3 class="text-white text-xl font-semibold">4</h3>
          <p class="text-[#d9d9d9]">Active Admins</p>
        </div>
        <div class="bg-[#415a77] p-4 rounded-lg shadow-md text-center">
          <h3 class="text-white text-xl font-semibold">Tsh 1,450,000</h3>
          <p class="text-[#d9d9d9]">Weekly Revenue</p>
        </div>
        <div class="bg-[#415a77] p-4 rounded-lg shadow-md text-center">
          <h3 class="text-white text-xl font-semibold">92%</h3>
          <p class="text-[#d9d9d9]">Uptime</p>
        </div>
      </div>

      <!-- Fallback Page -->
      <div v-else class="mt-6 text-[#e0e1dd] bg-[#1b263b] p-6 rounded-lg shadow-md">
        <h3 class="text-lg font-semibold text-yellow-300">Page: {{ currentTitle }}</h3>
        <p class="mt-2">This section will load the component for <strong>{{ currentPage }}</strong> when connected to Vue Router properly.</p>
      </div>
    </main>

    <!-- Footer -->
    <footer class="w-full bg-[#1b263b] text-center py-3 text-xs text-[#e0e1dd] border-t border-gray-700">
      &copy; {{ new Date().getFullYear() }} SmartBiz SaaS. All rights reserved.
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isSidebarOpen = ref(false)
const currentPage = ref('/dashboard/owner')
const currentTitle = ref('Owner Dashboard')

const links = [
  { name: 'Dashboard', path: '/dashboard/owner', icon: '📊' },
  { name: 'Admins', path: '/owner/admins', icon: '🛡️' },
  { name: 'Users', path: '/owner/users', icon: '👥' },
  { name: 'Payments', path: '/owner/payments', icon: '💳' },
  { name: 'Plans', path: '/owner/plans', icon: '📆' },
  { name: 'Logs', path: '/owner/logs', icon: '📜' },
  { name: 'Settings', path: '/owner/settings', icon: '⚙️' },
]

function toggleSidebar() {
  isSidebarOpen.value = !isSidebarOpen.value
}

function navigate(path) {
  currentPage.value = path
  const match = links.find((l) => l.path === path)
  currentTitle.value = match ? match.name : 'Dashboard'
  router.push(path)
  isSidebarOpen.value = false
}
</script>

<style scoped>
@media (min-width: 768px) {
  aside {
    transform: translateX(0) !important;
  }
}

header {
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}
</style>
