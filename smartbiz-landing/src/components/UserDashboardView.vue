<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold text-blue-900 mb-4">Welcome back, SmartBiz Admin!</h1>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        v-for="card in dashboardCards"
        :key="card.label"
        class="bg-white p-5 rounded-xl shadow border border-gray-200"
      >
        <h2 class="text-sm text-gray-600">{{ card.label }}</h2>
        <p class="text-2xl font-semibold text-blue-900">{{ card.value }}</p>
      </div>
    </div>

    <div class="mt-6 bg-white p-6 rounded-xl shadow border border-gray-200">
      <h2 class="text-lg font-semibold text-blue-900 mb-4">System Logs (Coming Soon)</h2>
      <div class="h-32 border-dashed border-2 border-gray-300 flex items-center justify-center text-gray-400">
        Placeholder for logs or recent activity
      </div>
    </div>
  </div>
</template>

<script setup>
const dashboardCards = [
  { label: "Total Users", value: 358 },
  { label: "New Signups", value: 42 },
  { label: "Active Subscriptions", value: 127 }
];
</script>
