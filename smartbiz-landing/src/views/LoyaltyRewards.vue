<template>
  <DashboardLayout>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">{{ $t('loyalty_points') }}</h2>
      <p class="text-gray-600 mb-6">{{ $t('loyalty_intro') }}</p>

      <!-- Points Table -->
      <div class="bg-white shadow rounded-xl p-4 overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="bg-gray-50">
              <th class="text-left py-2 px-4 text-sm text-gray-500">#</th>
              <th class="text-left py-2 px-4 text-sm text-gray-500">{{ $t('customer') }}</th>
              <th class="text-left py-2 px-4 text-sm text-gray-500">{{ $t('points') }}</th>
              <th class="text-left py-2 px-4 text-sm text-gray-500">{{ $t('last_activity') }}</th>
              <th class="text-left py-2 px-4 text-sm text-gray-500">{{ $t('actions') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(user, index) in customers"
              :key="user.id"
              class="border-b hover:bg-gray-50"
            >
              <td class="py-2 px-4">{{ index + 1 }}</td>
              <td class="py-2 px-4">{{ user.name }}</td>
              <td class="py-2 px-4">{{ user.points }}</td>
              <td class="py-2 px-4 text-gray-500">{{ user.lastActivity }}</td>
              <td class="py-2 px-4">
                <button class="text-sm text-blue-600 hover:underline">
                  {{ $t('view_history') }}
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import { ref } from 'vue'

const customers = ref([
  { id: 1, name: 'Jane Doe', points: 320, lastActivity: '2025-04-18' },
  { id: 2, name: 'Ali Mussa', points: 120, lastActivity: '2025-04-17' },
  { id: 3, name: 'Mariam John', points: 250, lastActivity: '2025-04-15' },
])
</script>

<style scoped>
th, td {
  padding: 0.75rem;
  font-size: 0.95rem;
}
</style>
