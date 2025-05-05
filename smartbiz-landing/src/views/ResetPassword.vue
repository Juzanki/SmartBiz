<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import AuthLayout from '@/layouts/AuthLayout.vue'

const toast = useToast()

const password = ref('')
const confirmPassword = ref('')
const loading = ref(false)

const resetPassword = async () => {
  if (password.value !== confirmPassword.value) {
    toast.error('❌ Passwords do not match!')
    return
  }

  const resetToken = localStorage.getItem('reset_token')
  if (!resetToken) {
    toast.error('❌ Reset session expired. Please start again.')
    window.location.href = '/forgot-password'
    return
  }

  loading.value = true
  try {
    await axios.post('/auth/reset-password', {
      token: resetToken,
      new_password: password.value
    })

    toast.success('✅ Password has been reset successfully!')
    localStorage.removeItem('reset_token')
    window.location.href = '/login'
  } catch (err) {
    console.error(err)
    toast.error(err.response?.data?.detail || '❌ Failed to reset password.')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <div>
      <!-- Title -->
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Reset Your Password</h2>

      <!-- Instructions -->
      <p class="text-sm text-center text-gray-300 mb-6">
        Enter a new password for your account.
      </p>

      <!-- Form -->
      <form @submit.prevent="resetPassword" class="space-y-4">
        <input
          v-model="password"
          type="password"
          placeholder="🔐 New Password"
          class="input"
          required
        />

        <input
          v-model="confirmPassword"
          type="password"
          placeholder="🔒 Confirm Password"
          class="input"
          required
        />

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-green-500 hover:bg-green-600 text-black font-semibold py-3 rounded-lg transition-all disabled:bg-gray-500 disabled:cursor-not-allowed"
        >
          <span v-if="!loading">Reset Password</span>
          <span v-else>Resetting...</span>
        </button>
      </form>

      <!-- Back to Login -->
      <p class="text-center text-sm text-gray-400 mt-6">
        Already know your password?
        <router-link to="/login" class="text-green-400 hover:underline">Back to Login</router-link>
      </p>
    </div>
  </AuthLayout>
</template>

<style scoped>
.input {
  @apply w-full bg-gray-800 text-white px-4 py-3 rounded-lg border border-gray-600 focus:outline-none focus:ring-2 focus:ring-green-500 text-sm placeholder:text-gray-400;
}
</style>
