<template>
  <div
    class="flex flex-col items-center p-4 rounded-lg border transition bg-gray-50"
    :class="connected ? 'border-green-400 shadow-md' : 'border-gray-200 opacity-50'"
  >
    <div class="text-3xl mb-2">{{ icon }}</div>
    <div class="text-lg font-bold">{{ name }}</div>
    <span class="text-xs mt-1" :class="connected ? 'text-green-600' : 'text-gray-400'">
      {{ connected ? 'Connected' : 'Disconnected' }}
    </span>
  </div>
</template>

<script setup>
defineProps(['name', 'icon', 'connected'])
</script>
