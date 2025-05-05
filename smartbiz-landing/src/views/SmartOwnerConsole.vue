<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">🧠 AI Command Center (Owner Control)</h2>
    </div>

    <!-- Command Input -->
    <div class="card p-4 shadow-sm border-0">
      <form @submit.prevent="submitCommand">
        <div class="mb-3">
          <label class="form-label">Enter a command (e.g. 'Freeze user johndoe')</label>
          <textarea class="form-control" rows="3" v-model="command" required></textarea>
        </div>
        <div class="text-end">
          <button type="submit" class="btn btn-primary">
            ⚡ Execute Command
          </button>
        </div>
      </form>
    </div>

    <!-- AI Response -->
    <div v-if="response" class="alert alert-info mt-4">
      <strong>AI:</strong> {{ response }}
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const command = ref('')
const response = ref('')

async function submitCommand() {
  try {
    const res = await axios.post('/api/owner/command', { prompt: command.value })
    response.value = res.data.message || '✅ Command executed.'
    command.value = ''
  } catch (err) {
    response.value = err.response?.data?.detail || '❌ Failed to execute command.'
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
textarea {
  resize: vertical;
}
</style>
