<template>
  <aside class="w-full md:w-64 bg-blue-900 text-white p-6 rounded-xl">
    <h2 class="text-lg font-bold mb-6">Settings</h2>
    <ul class="space-y-4">
      <li v-for="item in links" :key="item.name">
        <router-link
          :to="item.path"
          class="block p-2 rounded hover:bg-blue-800 transition-colors"
          active-class="bg-gold-500 text-blue-900 font-semibold"
        >
          {{ item.name }}
        </router-link>
      </li>
    </ul>
  </aside>
</template>

<script setup>
defineOptions({
  name: 'SettingsSidebar'
})

import { ref } from 'vue'

const links = ref([
  { name: 'Profile', path: '/settings/profile' },
  { name: 'Security', path: '/settings/security' },
  { name: 'Notifications', path: '/settings/notifications' },
  { name: 'Billing', path: '/settings/billing' },
  { name: 'Integrations', path: '/settings/integrations' },
])
</script>

<style scoped>
.bg-gold-500 {
  background-color: #d4af37;
}
</style>
