// src/views/DashboardUser.vue
<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">🤖 Smart Business Assistant (AI Bot)</h2>
    </div>

    <!-- Assistant Configuration -->
    <div class="card p-4 shadow-sm border-0">
      <form @submit.prevent="saveSettings">
        <div class="row g-4">
          <!-- Activation Toggle -->
          <div class="col-md-6">
            <label class="form-label">Activate AI Assistant</label>
            <select class="form-select" v-model="settings.active">
              <option :value="true">Enabled</option>
              <option :value="false">Disabled</option>
            </select>
          </div>

          <!-- Language Preference -->
          <div class="col-md-6">
            <label class="form-label">Preferred Language</label>
            <select class="form-select" v-model="settings.language">
              <option value="en">English</option>
              <option value="sw">Swahili</option>
              <option value="fr">French</option>
              <option value="es">Spanish</option>
            </select>
          </div>

          <!-- Default Greeting Message -->
          <div class="col-md-12">
            <label class="form-label">Default Greeting Message</label>
            <textarea class="form-control" rows="2" v-model="settings.defaultGreeting"></textarea>
          </div>

          <!-- Platforms -->
          <div class="col-md-12">
            <label class="form-label">Platforms to Use</label>
            <div class="d-flex gap-3 flex-wrap">
              <div v-for="platform in platformOptions" :key="platform.name" class="form-check">
                <input type="checkbox" class="form-check-input" :id="platform.name"
                       v-model="settings.platforms" :value="platform.name" />
                <label class="form-check-label" :for="platform.name">{{ platform.label }}</label>
              </div>
            </div>
          </div>

          <!-- Keyword-Based Training Templates (future) -->
          <div class="col-md-12">
            <label class="form-label">Example Template: Product Availability</label>
            <input type="text" class="form-control" disabled
                   value="e.g. 'Do you have [product]?' => AI will check product list & respond" />
          </div>
        </div>

        <div class="text-end mt-4">
          <button type="submit" class="btn btn-primary">📂 Save Assistant Settings
          </button>
        </div>
      </form>
    </div>

    <!-- Save Message -->
    <div v-if="successMessage" class="alert alert-success alert-dismissible fade show mt-4">
      ✅ {{ successMessage }}
      <button type="button" class="btn-close" @click="successMessage = ''"></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const successMessage = ref('')

const settings = ref({
  active: true,
  language: 'en',
  defaultGreeting: 'Hello! How can I assist you today?',
  platforms: ['whatsapp', 'telegram']
})

const platformOptions = [
  { name: 'whatsapp', label: 'WhatsApp' },
  { name: 'telegram', label: 'Telegram' },
  { name: 'sms', label: 'SMS' },
  { name: 'webchat', label: 'Web Chat' }
]

onMounted(async () => {
  try {
    const res = await axios.get('/api/ai-bot/settings')
    settings.value = res.data
  } catch (e) {
    console.warn('No settings found, using defaults')
  }
})

async function saveSettings() {
  try {
    await axios.put('/api/ai-bot/settings', settings.value)
    successMessage.value = 'Settings saved successfully!'
  } catch (err) {
    console.error(err)
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
