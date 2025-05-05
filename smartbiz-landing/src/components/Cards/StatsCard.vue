<template>
  <div class="bg-white rounded-lg shadow-sm p-5 flex flex-col items-center justify-center text-center">
    <div class="text-4xl mb-2">{{ icon }}</div>
    <div class="text-2xl font-bold mb-1">{{ value }}</div>
    <div class="text-gray-500 text-sm font-semibold uppercase tracking-wide">{{ title }}</div>
  </div>
</template>

<script setup>
defineProps(['title', 'value', 'icon'])
</script>
