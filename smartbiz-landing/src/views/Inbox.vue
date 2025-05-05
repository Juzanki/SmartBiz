<template>
  <DashboardLayout>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">{{ $t('inbox') }}</h2>
      <p class="text-gray-600 mb-6">{{ $t('inbox_intro') }}</p>

      <!-- Messages List -->
      <div class="bg-white rounded-xl shadow p-4">
        <ul>
          <li
            v-for="msg in messages"
            :key="msg.id"
            class="border-b py-4 hover:bg-gray-50"
          >
            <div class="flex justify-between">
              <div>
                <p class="font-semibold text-blue-900">{{ msg.sender }}</p>
                <p class="text-sm text-gray-600">{{ msg.text }}</p>
              </div>
              <span class="text-xs text-gray-500">{{ msg.timestamp }}</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import { ref } from 'vue'

const messages = ref([
  { id: 1, sender: '+255 789 123 456', text: 'Hello, is the promo still valid?', timestamp: '2 mins ago' },
  { id: 2, sender: '@customer_bot', text: 'Thanks for your support.', timestamp: '5 mins ago' },
  { id: 3, sender: 'support@biz.com', text: 'Your issue has been resolved.', timestamp: '1 hour ago' }
])
</script>

<style scoped>
ul li {
  padding: 0.5rem 0;
}
</style>
