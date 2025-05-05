<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-6xl mx-auto bg-white rounded-xl shadow p-8">
      <h1 class="text-3xl font-bold text-blue-900 mb-6">Integrations</h1>

      <p class="text-gray-600 mb-8">
        Connect SmartBiz with your favorite platforms and automate your workflows easily.
      </p>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="integration in integrations"
          :key="integration.name"
          class="border rounded-xl shadow-sm p-6 bg-white flex flex-col justify-between"
        >
          <div>
            <div class="flex items-center gap-3 mb-4">
              <span class="text-3xl">{{ integration.icon }}</span>
              <h2 class="text-xl font-bold text-blue-900">{{ integration.name }}</h2>
            </div>
            <p class="text-gray-700 text-sm mb-4">{{ integration.desc }}</p>
          </div>
          <div class="flex justify-between items-center">
            <span
              :class="integration.connected ? 'text-green-600' : 'text-red-500'"
              class="text-sm font-semibold"
            >
              {{ integration.connected ? 'Connected' : 'Not Connected' }}
            </span>
            <button
              @click="toggleIntegration(integration)"
              :class="integration.connected
                ? 'bg-gray-300 text-gray-700 hover:bg-gray-400'
                : 'bg-blue-900 text-white hover:bg-blue-800'"
              class="px-4 py-2 rounded-lg text-sm font-semibold transition"
            >
              {{ integration.connected ? 'Disconnect' : 'Connect' }}
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'IntegrationView'
})

import { ref } from 'vue'

const integrations = ref([
  {
    name: 'WhatsApp Business API',
    icon: '📱',
    desc: 'Send and receive messages via WhatsApp.',
    connected: true
  },
  {
    name: 'Telegram Bot',
    icon: '✈️',
    desc: 'Enable automated Telegram replies and updates.',
    connected: false
  },
  {
    name: 'Stripe',
    icon: '💳',
    desc: 'Accept payments from customers securely.',
    connected: true
  },
  {
    name: 'Zapier',
    icon: '⚡',
    desc: 'Automate your business processes with thousands of apps.',
    connected: false
  },
  {
    name: 'Slack',
    icon: '💬',
    desc: 'Get instant team notifications via Slack.',
    connected: false
  },
  {
    name: 'Google Sheets',
    icon: '📊',
    desc: 'Export reports to Google Sheets in real-time.',
    connected: false
  }
])

const toggleIntegration = (integration) => {
  integration.connected = !integration.connected
}
</script>

<style scoped>
/* Custom colors can go here if needed */
</style>
