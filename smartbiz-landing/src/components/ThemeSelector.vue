<template>
  <select v-model="theme" @change="switchTheme" class="theme-selector">
    <option value="light">☀️ Light</option>
    <option value="dark">🌙 Dark</option>
  </select>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'

const theme = ref(localStorage.getItem('theme') || 'light')

const switchTheme = () => {
  localStorage.setItem('theme', theme.value)
  document.body.className = theme.value === 'dark' ? 'theme-dark' : 'theme-light'
}

onMounted(() => {
  document.body.className = theme.value === 'dark' ? 'theme-dark' : 'theme-light'
})
</script>

<style scoped>
.theme-selector {
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 0.9rem;
}
</style>
