<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold text-blue-900 mb-4">Analytics Overview</h1>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
      <div
        v-for="card in summaryCards"
        :key="card.label"
        class="bg-white rounded-xl shadow p-4 border border-gray-200"
      >
        <h2 class="text-sm text-gray-600">{{ card.label }}</h2>
        <p class="text-2xl font-semibold text-blue-900">{{ card.value }}</p>
      </div>
    </div>

    <div class="bg-white p-6 rounded-xl shadow border border-gray-200">
      <h2 class="text-lg font-semibold text-blue-900 mb-4">User Activity</h2>
      <p class="text-gray-600 text-sm">Charts and metrics will appear here.</p>
      <!-- Replace with real chart later -->
      <div class="mt-4 border-dashed border-2 border-gray-300 h-40 flex items-center justify-center text-gray-400">
        Placeholder for Chart (e.g., Bar or Line Chart)
      </div>
    </div>
  </div>
</template>

<script setup>
const summaryCards = [
  { label: "Active Users", value: 120 },
  { label: "Monthly Growth", value: "15%" },
  { label: "Bounce Rate", value: "32%" }
];
</script>
