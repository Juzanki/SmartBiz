<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">👤 User Profile Settings</h2>
    </div>

    <!-- Profile Form Card -->
    <div class="card shadow-sm border-0 p-4">
      <ProfileForm :profile="profile" @submit="saveProfile" />
    </div>

    <!-- Success Alert -->
    <div v-if="successMessage" class="alert alert-success alert-dismissible fade show mt-4" role="alert">
      ✅ {{ successMessage }}
      <button type="button" class="btn-close" @click="successMessage = ''"></button>
    </div>

    <!-- Error Alert -->
    <div v-if="errorMessage" class="alert alert-danger alert-dismissible fade show mt-3" role="alert">
      ⚠️ {{ errorMessage }}
      <button type="button" class="btn-close" @click="errorMessage = ''"></button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProfileForm from '@/components/ProfileForm.vue'

const successMessage = ref('')
const errorMessage = ref('')

const profile = ref({
  fullName: '',
  email: '',
  phone: '',
  password: '',
  location: '',
  bio: '',
  avatar: '',
  notificationPreference: ''
})

onMounted(() => {
  const saved = localStorage.getItem('user_profile')
  if (saved) {
    profile.value = { ...JSON.parse(saved), password: '' }
  }
})

function saveProfile(data) {
  if (!data.fullName || !data.email) {
    errorMessage.value = 'Full name and email are required.'
    return
  }

  const toSave = { ...data }
  if (!toSave.password) delete toSave.password

  localStorage.setItem('user_profile', JSON.stringify(toSave))
  successMessage.value = 'Profile updated successfully!'
  errorMessage.value = ''
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
