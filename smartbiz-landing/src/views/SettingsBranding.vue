<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">⚙️ Settings & Branding</h2>
    </div>

    <!-- Settings Form -->
    <div class="card shadow-sm p-4 border-0">
      <form @submit.prevent="saveSettings">
        <div class="row g-4">

          <!-- Business Name -->
          <div class="col-md-6">
            <label class="form-label">Business Name</label>
            <input type="text" class="form-control" v-model="settings.businessName" required>
          </div>

          <!-- Preferred Language -->
          <div class="col-md-6">
            <label class="form-label">Preferred Language</label>
            <select class="form-select" v-model="settings.language" required>
              <option value="en">English</option>
              <option value="sw">Swahili</option>
              <option value="fr">French</option>
              <option value="es">Spanish</option>
            </select>
          </div>

          <!-- Tagline -->
          <div class="col-md-6">
            <label class="form-label">Business Tagline</label>
            <input type="text" class="form-control" v-model="settings.tagline" placeholder="Your slogan or mission">
          </div>

          <!-- Timezone -->
          <div class="col-md-3">
            <label class="form-label">Timezone</label>
            <select class="form-select" v-model="settings.timezone">
              <option>Africa/Nairobi</option>
              <option>Africa/Dar_es_Salaam</option>
              <option>UTC</option>
              <option>Asia/Dubai</option>
              <option>America/New_York</option>
            </select>
          </div>

          <!-- Currency -->
          <div class="col-md-3">
            <label class="form-label">Default Currency</label>
            <select class="form-select" v-model="settings.currency">
              <option value="TZS">TZS</option>
              <option value="USD">USD</option>
              <option value="KES">KES</option>
              <option value="EUR">EUR</option>
            </select>
          </div>

          <!-- Logo URL -->
          <div class="col-md-6">
            <label class="form-label">Upload Logo URL</label>
            <input type="url" class="form-control" v-model="settings.logoUrl">
            <small class="text-muted">Paste direct image link (e.g., from your host or CDN).</small>
          </div>

          <!-- Primary Color -->
          <div class="col-md-3">
            <label class="form-label">Primary Color</label>
            <input type="color" class="form-control form-control-color" v-model="settings.primaryColor">
          </div>

          <!-- Secondary Color -->
          <div class="col-md-3">
            <label class="form-label">Secondary Color</label>
            <input type="color" class="form-control form-control-color" v-model="settings.secondaryColor">
          </div>

          <!-- Enable Custom Domain -->
          <div class="col-md-12 form-check form-switch mt-3">
            <input class="form-check-input" type="checkbox" id="customDomain" v-model="settings.enableCustomDomain">
            <label class="form-check-label" for="customDomain">Enable Custom Domain (e.g. yourbiz.co.tz)</label>
          </div>

        </div>

        <!-- Save Button -->
        <div class="text-end mt-4">
          <button class="btn btn-primary" type="submit">
            💾 Save Changes
          </button>
        </div>
      </form>
    </div>

    <!-- Success Message -->
    <div v-if="success" class="alert alert-success alert-dismissible fade show mt-4" role="alert">
      ✅ Settings saved successfully!
      <button type="button" class="btn-close" @click="success = false"></button>
    </div>

    <!-- Branding Preview -->
    <div v-if="settings.logoUrl" class="card shadow-sm border-0 text-center mt-5 p-4">
      <h5 class="text-primary mb-2">{{ settings.businessName }}</h5>
      <p class="text-muted">{{ settings.tagline }}</p>
      <img :src="settings.logoUrl" alt="Logo" class="img-fluid rounded" style="max-height: 120px;">
      <div class="mt-3">
        <span class="badge me-2" :style="{backgroundColor: settings.primaryColor, color: '#fff'}">
          Primary
        </span>
        <span class="badge" :style="{backgroundColor: settings.secondaryColor, color: '#fff'}">
          Secondary
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const success = ref(false)

const settings = ref({
  businessName: '',
  tagline: '',
  language: 'en',
  logoUrl: '',
  primaryColor: '#0d6efd',
  secondaryColor: '#6c757d',
  timezone: 'Africa/Dar_es_Salaam',
  currency: 'TZS',
  enableCustomDomain: false
})

onMounted(() => {
  const saved = JSON.parse(localStorage.getItem('user_settings'))
  if (saved) settings.value = saved
})

function saveSettings() {
  localStorage.setItem('user_settings', JSON.stringify(settings.value))
  success.value = true
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
