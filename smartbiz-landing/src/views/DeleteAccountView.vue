<template>
  <div class="container py-5">
    <div class="max-w-xl mx-auto bg-white p-4 p-md-5 rounded-3 shadow border border-danger-subtle">
      <div class="text-center mb-4">
        <i class="bi bi-exclamation-triangle-fill text-danger" style="font-size: 2rem;"></i>
        <h2 class="fw-bold text-danger mt-2">Delete Account</h2>
        <p class="text-muted small">This action is permanent and cannot be undone.</p>
      </div>

      <form @submit.prevent="confirmDelete">
        <div class="mb-3">
          <label class="form-label text-danger small">Confirm your password</label>
          <input
            type="password"
            v-model="password"
            class="form-control border border-danger-subtle"
            placeholder="Enter your password"
            required
          />
        </div>

        <div class="d-grid mt-4">
          <button
            type="submit"
            class="btn btn-danger fw-bold"
            :disabled="loading"
          >
            <span v-if="loading">
              <span class="spinner-border spinner-border-sm me-1"></span>
              Deleting...
            </span>
            <span v-else>Yes, Delete My Account</span>
          </button>
        </div>
      </form>

      <div class="text-center mt-4">
        <router-link to="/settings" class="text-decoration-none small text-muted">Cancel and go back</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const password = ref('')
const loading = ref(false)
const router = useRouter()
const toast = useToast()

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const confirmDelete = async () => {
  if (!password.value) {
    toast.error('Password is required.')
    return
  }

  loading.value = true
  try {
    const token = localStorage.getItem('access_token')
    await axios.delete(`${API_BASE}/profile/me`, {
      headers: {
        Authorization: `Bearer ${token}`
      },
      data: {
        password: password.value
      }
    })

    toast.success('✅ Your account has been deleted.')
    localStorage.clear()
    router.push('/signup')
  } catch (err) {
    toast.error(err.response?.data?.detail || '❌ Failed to delete account.')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.container {
  background: #f9f9fa;
}
</style>
