<template>
  <div class="container py-5">
    <h2 class="text-primary fw-bold mb-4">👨‍💼 Admin Branding Settings</h2>

    <div class="card shadow-sm border-0 p-4">
      <SettingsForm :settings="adminSettings" @submit="saveAdminSettings" />
    </div>

    <div v-if="success" class="alert alert-success mt-4">
      ✅ Admin branding settings saved successfully!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import SettingsForm from '@/components/SettingsForm.vue'

const success = ref(false)
const adminSettings = ref({
  businessName: '',
  tagline: '',
  language: 'en',
  logoUrl: '',
  primaryColor: '#0d6efd',
  secondaryColor: '#6c757d',
  timezone: 'UTC',
  currency: 'USD',
  enableCustomDomain: false
})

onMounted(() => {
  const saved = JSON.parse(localStorage.getItem('admin_settings'))
  if (saved) adminSettings.value = saved
})

function saveAdminSettings(data) {
  localStorage.setItem('admin_settings', JSON.stringify(data))
  success.value = true
}
</script>
