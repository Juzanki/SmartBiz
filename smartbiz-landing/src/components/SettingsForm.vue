<template>
  <form @submit.prevent="handleSubmit">
    <div class="row g-4">

      <!-- Business Name -->
      <div class="col-md-6">
        <label class="form-label">Business Name</label>
        <input type="text" class="form-control" v-model="model.businessName" required>
      </div>

      <!-- Preferred Language -->
      <div class="col-md-6">
        <label class="form-label">Preferred Language</label>
        <select class="form-select" v-model="model.language" required>
          <option value="en">English</option>
          <option value="sw">Swahili</option>
          <option value="fr">French</option>
          <option value="es">Spanish</option>
        </select>
      </div>

      <!-- Tagline -->
      <div class="col-md-6">
        <label class="form-label">Business Tagline</label>
        <input type="text" class="form-control" v-model="model.tagline" placeholder="Your slogan or mission">
      </div>

      <!-- Timezone -->
      <div class="col-md-3">
        <label class="form-label">Timezone</label>
        <select class="form-select" v-model="model.timezone">
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
        <select class="form-select" v-model="model.currency">
          <option value="TZS">TZS</option>
          <option value="USD">USD</option>
          <option value="KES">KES</option>
          <option value="EUR">EUR</option>
        </select>
      </div>

      <!-- Logo URL -->
      <div class="col-md-6">
        <label class="form-label">Upload Logo URL</label>
        <input type="url" class="form-control" v-model="model.logoUrl">
        <small class="text-muted">Paste direct image link (e.g., from your host or CDN).</small>
      </div>

      <!-- Primary Color -->
      <div class="col-md-3">
        <label class="form-label">Primary Color</label>
        <input type="color" class="form-control form-control-color" v-model="model.primaryColor">
      </div>

      <!-- Secondary Color -->
      <div class="col-md-3">
        <label class="form-label">Secondary Color</label>
        <input type="color" class="form-control form-control-color" v-model="model.secondaryColor">
      </div>

      <!-- Enable Custom Domain -->
      <div class="col-md-12 form-check form-switch mt-3">
        <input class="form-check-input" type="checkbox" id="customDomain" v-model="model.enableCustomDomain">
        <label class="form-check-label" for="customDomain">Enable Custom Domain (e.g. yourbiz.co.tz)</label>
      </div>

    </div>

    <div class="text-end mt-4">
      <button class="btn btn-primary" type="submit">
        💾 Save Changes
      </button>
    </div>
  </form>
</template>

<script setup>
import { reactive, watch } from 'vue'

const props = defineProps({
  settings: {
    type: Object,
    required: true
  }
})

const emit = defineEmits(['submit'])

const model = reactive({ ...props.settings })

watch(() => props.settings, (newVal) => {
  Object.assign(model, newVal)
})

function handleSubmit() {
  emit('submit', { ...model })
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
