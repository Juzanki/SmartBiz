<template>
  <DashboardLayout>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">{{ $t('orders') }}</h2>
      <p class="text-gray-600 mb-6">{{ $t('orders_intro') }}</p>

      <!-- Orders Table -->
      <div class="bg-white rounded-xl shadow p-4 overflow-x-auto">
        <table class="min-w-full">
          <thead>
            <tr class="bg-gray-50">
              <th class="text-left px-4 py-2 text-sm text-gray-500">#</th>
              <th class="text-left px-4 py-2 text-sm text-gray-500">{{ $t('customer') }}</th>
              <th class="text-left px-4 py-2 text-sm text-gray-500">{{ $t('product') }}</th>
              <th class="text-left px-4 py-2 text-sm text-gray-500">{{ $t('status') }}</th>
              <th class="text-left px-4 py-2 text-sm text-gray-500">{{ $t('date') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="order in orders"
              :key="order.id"
              class="border-b hover:bg-gray-50"
            >
              <td class="px-4 py-2">{{ order.id }}</td>
              <td class="px-4 py-2">{{ order.customer }}</td>
              <td class="px-4 py-2">{{ order.product }}</td>
              <td class="px-4 py-2">{{ order.status }}</td>
              <td class="px-4 py-2 text-sm text-gray-500">{{ order.date }}</td>
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

const orders = ref([
  { id: 1, customer: 'John Doe', product: 'Promo Pack', status: 'Pending', date: '2025-04-19' },
  { id: 2, customer: 'Jane Smith', product: 'AI Bot Subscription', status: 'Completed', date: '2025-04-18' },
  { id: 3, customer: 'Ali Mussa', product: 'SMS Package', status: 'Processing', date: '2025-04-17' }
])
</script>

<style scoped>
th, td {
  padding: 0.75rem;
}
</style>
