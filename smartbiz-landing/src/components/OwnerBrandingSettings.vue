<template>
  <div class="container py-5">
    <h2 class="text-primary fw-bold mb-4">🏢 Owner Branding Settings</h2>

    <div class="card shadow-sm border-0 p-4">
      <SettingsForm :settings="ownerSettings" @submit="saveOwnerSettings" />
    </div>

    <div v-if="success" class="alert alert-success mt-4">
      ✅ Your business branding has been saved!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import SettingsForm from '@/components/SettingsForm.vue'

const success = ref(false)
const ownerSettings = ref({
  businessName: '',
  tagline: '',
  language: 'en',
  logoUrl: '',
  primaryColor: '#198754',
  secondaryColor: '#6c757d',
  timezone: 'Africa/Dar_es_Salaam',
  currency: 'TZS',
  enableCustomDomain: true
})

onMounted(() => {
  const saved = JSON.parse(localStorage.getItem('owner_settings'))
  if (saved) ownerSettings.value = saved
})

function saveOwnerSettings(data) {
  localStorage.setItem('owner_settings', JSON.stringify(data))
  success.value = true
}
</script>
