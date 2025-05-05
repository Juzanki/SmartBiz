<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-6xl mx-auto bg-white rounded-xl shadow p-8">
      <h1 class="text-3xl font-bold text-blue-900 mb-6">Choose Your Plan</h1>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div
          v-for="plan in plans"
          :key="plan.name"
          class="p-6 rounded-xl border shadow"
          :class="plan.name === selectedPlan.name ? 'border-gold-500' : 'border-gray-200'"
        >
          <h2 class="text-xl font-bold text-blue-900 mb-2">{{ plan.name }}</h2>
          <p class="text-4xl font-bold mb-4">
            ${{ plan.price }}
            <span class="text-sm text-gray-600">/month</span>
          </p>

          <ul class="mb-6 space-y-1 text-sm text-gray-700">
            <li v-for="(feature, i) in plan.features" :key="i">
              ✔ {{ feature }}
            </li>
          </ul>

          <button
            @click="selectPlan(plan)"
            class="w-full py-2 rounded-lg font-semibold"
            :class="plan.name === selectedPlan.name
              ? 'bg-gray-300 text-gray-600'
              : 'bg-blue-900 text-white hover:bg-blue-800'"
          >
            {{ plan.name === selectedPlan.name ? 'Current Plan' : 'Upgrade Now' }}
          </button>
        </div>
      </div>

      <div class="mt-12 text-center text-sm text-gray-500">
        Need help choosing a plan? <a href="/help" class="text-blue-900 font-semibold underline">Contact Support</a>
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'PlansView'
})

import { ref } from 'vue'

const selectedPlan = ref({
  name: 'Pro',
  price: 29,
  features: [
    '10,000 messages/month',
    'All platforms supported',
    'Advanced analytics',
    'Priority email support'
  ]
})

const plans = ref([
  {
    name: 'Free',
    price: 0,
    features: [
      '1,000 messages/month',
      'WhatsApp & Email only',
      'Basic analytics'
    ]
  },
  {
    name: 'Pro',
    price: 29,
    features: [
      '10,000 messages/month',
      'All platforms supported',
      'Advanced analytics',
      'Priority email support'
    ]
  },
  {
    name: 'Enterprise',
    price: 99,
    features: [
      'Unlimited messages',
      'All platforms + API Access',
      'Dedicated support manager',
      'Custom SLAs'
    ]
  }
])

const selectPlan = (plan) => {
  selectedPlan.value = plan
}
</script>

<style scoped>
.border-gold-500 {
  border-color: #d4af37;
}
</style>
