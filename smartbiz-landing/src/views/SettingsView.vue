<template>
  <div class="container py-5">
    <h2 class="text-center fw-bold text-primary mb-4">User Settings</h2>

    <div class="row g-4">
      <!-- Profile Settings -->
      <div class="col-md-6">
        <div class="card shadow border-0 rounded-4 p-4">
          <h5 class="text-warning mb-3">Profile Information</h5>
          <form @submit.prevent="updateProfile">
            <div class="mb-3">
              <label class="form-label">Full Name</label>
              <input type="text" v-model="form.full_name" class="form-control" required />
            </div>
            <div class="mb-3">
              <label class="form-label">Email</label>
              <input type="email" v-model="form.email" class="form-control" disabled />
            </div>
            <div class="mb-3">
              <label class="form-label">Phone Number</label>
              <input type="text" v-model="form.phone_number" class="form-control" />
            </div>
            <div class="mb-3">
              <label class="form-label">Language</label>
              <select v-model="form.language" class="form-select">
                <option value="sw">Swahili</option>
                <option value="en">English</option>
                <option value="fr">French</option>
                <option value="ar">Arabic</option>
              </select>
            </div>
            <div class="form-check form-switch mb-3">
              <input class="form-check-input" type="checkbox" v-model="form.auto_ai" id="autoAI" />
              <label class="form-check-label" for="autoAI">Enable AI Auto Assistant</label>
            </div>
            <button class="btn btn-primary w-100 fw-bold" :disabled="loading">
              <span v-if="loading" class="spinner-border spinner-border-sm"></span>
              <span v-else>Update Profile</span>
            </button>
          </form>
        </div>
      </div>

      <!-- Password Reset -->
      <div class="col-md-6">
        <div class="card shadow border-0 rounded-4 p-4">
          <h5 class="text-danger mb-3">Change Password</h5>
          <form @submit.prevent="changePassword">
            <div class="mb-3">
              <label class="form-label">Current Password</label>
              <input type="password" v-model="passwordForm.old_password" class="form-control" required />
            </div>
            <div class="mb-3">
              <label class="form-label">New Password</label>
              <input type="password" v-model="passwordForm.new_password" class="form-control" required />
            </div>
            <button class="btn btn-danger w-100 fw-bold" :disabled="loadingPass">
              <span v-if="loadingPass" class="spinner-border spinner-border-sm"></span>
              <span v-else>Update Password</span>
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'

const toast = useToast()
const loading = ref(false)
const loadingPass = ref(false)
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const form = ref({
  full_name: '',
  email: '',
  phone_number: '',
  language: 'sw',
  auto_ai: JSON.parse(localStorage.getItem('auto_ai') || 'false')
})

const passwordForm = ref({
  old_password: '',
  new_password: ''
})

onMounted(async () => {
  try {
    const res = await axios.get(`${API_BASE}/auth/me`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    form.value = { ...res.data, auto_ai: JSON.parse(localStorage.getItem('auto_ai') || 'false') }
  } catch (err) {
    toast.error('Failed to load profile')
  }
})

const updateProfile = async () => {
  loading.value = true
  try {
    await axios.put(`${API_BASE}/auth/me`, form.value, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    localStorage.setItem('auto_ai', form.value.auto_ai)
    toast.success('Profile updated successfully')
  } catch (err) {
    toast.error('Update failed')
  } finally {
    loading.value = false
  }
}

const changePassword = async () => {
  loadingPass.value = true
  try {
    await axios.post(`${API_BASE}/auth/change-password`, passwordForm.value, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    toast.success('Password changed successfully')
    passwordForm.value.old_password = ''
    passwordForm.value.new_password = ''
  } catch (err) {
    toast.error('Failed to change password')
  } finally {
    loadingPass.value = false
  }
}
</script>

<style scoped>
.container {
  max-width: 960px;
}
.card {
  background-color: #fff;
  border-radius: 1rem;
}
</style>
