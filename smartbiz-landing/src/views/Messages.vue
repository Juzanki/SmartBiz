<template>
  <DashboardLayout>
    <div class="p-6">
      <h2 class="text-2xl font-bold mb-4">{{ $t('messages') }}</h2>
      <p class="text-gray-600 mb-6">{{ $t('messages_intro') }}</p>

      <!-- Conversation Thread Example -->
      <div class="bg-white rounded-xl shadow p-4 space-y-4">
        <div
          v-for="msg in thread"
          :key="msg.id"
          :class="msg.sender === 'user' ? 'text-right' : 'text-left'"
        >
          <div
            :class="[
              'inline-block px-4 py-2 rounded-lg',
              msg.sender === 'user' ? 'bg-blue-100 text-blue-900' : 'bg-gray-100 text-gray-700'
            ]"
          >
            {{ msg.text }}
          </div>
          <div class="text-xs text-gray-500 mt-1">{{ msg.timestamp }}</div>
        </div>

        <!-- Reply Form -->
        <div class="mt-6">
          <input
            v-model="reply"
            @keyup.enter="sendReply"
            class="w-full p-3 border rounded"
            :placeholder="$t('type_reply')"
          />
        </div>
      </div>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref } from 'vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

const thread = ref([
  { id: 1, sender: 'customer', text: 'Can I get this service today?', timestamp: '10:05 AM' },
  { id: 2, sender: 'user', text: 'Yes, we are available.', timestamp: '10:07 AM' },
])

const reply = ref('')

function sendReply() {
  if (!reply.value) return
  thread.value.push({
    id: Date.now(),
    sender: 'user',
    text: reply.value,
    timestamp: new Date().toLocaleTimeString()
  })
  reply.value = ''
}
</script>

<style scoped>
input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 1px #3b82f6;
}
</style>
