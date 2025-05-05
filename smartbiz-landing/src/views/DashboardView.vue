<template>
  <div class="min-h-screen bg-gray-100 flex">
    <!-- Sidebar (Desktop Only) -->
    <aside
      class="fixed inset-y-0 left-0 w-64 bg-blue-900 text-white p-6 flex-col z-40 hidden md:flex"
      aria-label="Sidebar"
    >
      <div class="flex items-center gap-3 text-2xl font-bold mb-10">
        <img src="@/assets/logo-circle.png" class="w-9 h-9 rounded-full bg-white border border-yellow-400 shadow" />
        <span>SmartBiz</span>
      </div>
      <nav class="flex-1 space-y-2">
        <router-link
          v-for="link in navLinks"
          :key="link.name"
          :to="link.path"
          class="flex items-center gap-3 p-3 rounded-lg hover:bg-blue-800 transition-colors focus:outline-none"
          active-class="router-link-exact-active"
          tabindex="0"
          :aria-label="$t(link.name)"
        >
          <span>{{ link.icon }}</span>
          <span class="font-semibold">{{ $t(link.name) }}</span>
        </router-link>
      </nav>
      <footer class="mt-auto pt-6 border-t border-blue-800 text-xs text-gray-300">
        &copy; {{ new Date().getFullYear() }} SmartBiz
      </footer>
    </aside>

    <!-- Main Content -->
    <main class="flex-1 p-4 md:p-8 md:ml-64">
      <!-- Header -->
      <div class="flex flex-col md:flex-row justify-between items-center mb-8 gap-3">
        <h1 class="text-2xl font-bold text-blue-900 flex items-center gap-2">
          <span class="text-gold-500">🏠</span> {{ $t('dashboard') }}
        </h1>
        <div class="flex items-center gap-4">
          <span class="text-gray-700 font-medium">{{ userName }}</span>
          <div
            class="w-9 h-9 bg-gray-300 rounded-full flex items-center justify-center text-lg text-blue-900 font-bold"
            :title="userName"
          >
            {{ userInitials }}
          </div>
        </div>
      </div>

      <!-- Quick Stats -->
      <section class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <StatsCard
          v-for="stat in stats"
          :key="stat.title"
          :title="$t(stat.title)"
          :value="stat.value"
          :icon="stat.icon"
        />
      </section>

      <!-- Platform Connections -->
      <section class="bg-white rounded-2xl shadow-sm p-6 mb-8">
        <h2 class="text-xl font-bold text-blue-900 mb-4">{{ $t('platform_connections') }}</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
          <PlatformCard
            v-for="platform in platforms"
            :key="platform.name"
            :name="$t(platform.name)"
            :icon="platform.icon"
            :connected="platform.connected"
          />
        </div>
      </section>

      <!-- Recent Messages Table -->
      <section class="bg-white rounded-2xl shadow-sm p-6">
        <h2 class="text-xl font-bold text-blue-900 mb-4">{{ $t('recent_messages') }}</h2>
        <div class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50">
              <tr>
                <th class="text-left py-3 px-4 text-sm text-gray-500">{{ $t('platform') }}</th>
                <th class="text-left py-3 px-4 text-sm text-gray-500">{{ $t('sender') }}</th>
                <th class="text-left py-3 px-4 text-sm text-gray-500">{{ $t('message') }}</th>
                <th class="text-left py-3 px-4 text-sm text-gray-500">{{ $t('timestamp') }}</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="message in recentMessages"
                :key="message.id"
                class="border-t border-gray-100 hover:bg-gray-50 transition"
              >
                <td class="py-3 px-4 flex items-center gap-2">
                  <span>{{ message.platform.icon }}</span>
                  {{ $t(message.platform.name) }}
                </td>
                <td class="py-3 px-4">{{ message.sender }}</td>
                <td class="py-3 px-4">{{ message.text }}</td>
                <td class="py-3 px-4 text-gray-500">{{ message.timestamp }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { computed } from "vue"
import PlatformCard from '@/components/Cards/PlatformCard.vue'
import StatsCard from '@/components/Cards/StatsCard.vue'

// User Info
const userName = localStorage.getItem('user_name') || 'User'
const userInitials = computed(() => {
  if (!userName.trim()) return 'U'
  const names = userName.split(' ')
  if (names.length === 1) return names[0].slice(0, 2).toUpperCase()
  return names.map(n => n[0]).join('').substring(0, 2).toUpperCase()
})

// Sidebar Links
const navLinks = [
  { name: "dashboard", path: "/dashboard", icon: "🏠" },
  { name: "autoresponder", path: "/autoresponder", icon: "🤖" },
  { name: "analytics", path: "/analytics", icon: "📊" },
  { name: "billing", path: "/billing", icon: "💳" },
  { name: "settings", path: "/settings", icon: "⚙️" },
]

// Stats (for dashboard cards)
const stats = [
  { title: "messages_sent", value: "2,543", icon: "📨" },
  { title: "active_platforms", value: "3/5", icon: "🔌" },
  { title: "response_rate", value: "89%", icon: "🚀" },
]

// Connected Platforms
const platforms = [
  { name: "whatsapp", icon: "📱", connected: true },
  { name: "telegram", icon: "✈️", connected: true },
  { name: "sms", icon: "📲", connected: false },
  { name: "email", icon: "📧", connected: true },
]

// Recent messages table
const recentMessages = [
  {
    id: 1,
    platform: { name: "whatsapp", icon: "📱" },
    sender: "+255 712 345 678",
    text: "Hello, I need support!",
    timestamp: "2 min ago",
  },
  {
    id: 2,
    platform: { name: "email", icon: "📧" },
    sender: "john@company.com",
    text: "Order confirmation",
    timestamp: "1 hour ago",
  },
  {
    id: 3,
    platform: { name: "telegram", icon: "✈️" },
    sender: "@johndoe",
    text: "Bot not working",
    timestamp: "3 hours ago",
  },
]
</script>

<style scoped>
.text-gold-500 { color: #FFD600; }
.bg-blue-900 { background-color: #181829 !important; }
.hover\:bg-blue-800:hover { background-color: #222d4a !important; }
.router-link-exact-active {
  background-color: #FFD600 !important;
  color: #181829 !important;
  font-weight: 700;
}
</style>
