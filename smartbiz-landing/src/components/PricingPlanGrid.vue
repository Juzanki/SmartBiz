<template>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
    <div
      v-for="plan in plans"
      :key="plan.name"
      class="bg-white p-6 rounded-2xl shadow-md transition hover:shadow-lg border-2"
      :class="plan.highlight ? 'border-gold-500' : 'border-gray-200'"
    >
      <!-- Plan Name -->
      <h3 class="text-xl font-bold text-blue-900 mb-2 text-center">
        {{ plan.name }}
      </h3>

      <!-- Price -->
      <p class="text-4xl font-extrabold text-center mb-4 text-blue-900">
        ${{ plan.price }}
        <span class="text-base font-medium text-gray-600">/month</span>
      </p>

      <!-- Features List -->
      <ul class="mb-6 space-y-3 text-sm text-gray-700">
        <li
          v-for="feature in plan.features"
          :key="feature"
          class="flex items-start gap-2"
        >
          <span class="text-green-500">✔</span>
          <span>{{ feature }}</span>
        </li>
      </ul>

      <!-- Slot for external buttons -->
      <div class="mt-auto">
        <slot name="button" :plan="plan" />
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  plans: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.border-gold-500 {
  border-color: #d4af37;
}
</style>
