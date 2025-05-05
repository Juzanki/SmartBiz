<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useToast } from 'vue-toastification'
import AuthLayout from '@/layouts/AuthLayout.vue'

const toast = useToast()

const identifier = ref('')
const loading = ref(false)

const requestReset = async () => {
  loading.value = true
  try {
    await axios.post('/auth/request-reset', { identifier: identifier.value })
    toast.success('✅ Reset code sent successfully! Check your email or SMS.')
    window.location.href = '/verify-code'
  } catch (error) {
    console.error(error)
    toast.error(error.response?.data?.detail || '❌ Failed to send reset code.')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <div>
      <!-- Title -->
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Forgot Your Password?</h2>

      <!-- Instructions -->
      <p class="text-sm text-center text-gray-300 mb-6">
        Enter your email or phone number and we'll send you a code to reset your password.
      </p>

      <!-- Forgot Password Form -->
      <form @submit.prevent="requestReset" class="space-y-4">
        <input
          v-model="identifier"
          type="text"
          placeholder="📧 Email or Phone Number"
          class="input"
          required
        />

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-all disabled:bg-gray-500 disabled:cursor-not-allowed"
        >
          <span v-if="!loading">Send Reset Code</span>
          <span v-else>Sending Code...</span>
        </button>
      </form>

      <!-- Back to Login -->
      <p class="text-center text-sm text-gray-400 mt-6">
        Remembered your password?
        <router-link to="/login" class="text-blue-400 hover:underline">Back to Login</router-link>
      </p>
    </div>
  </AuthLayout>
</template>

<style scoped>
.input {
  @apply w-full bg-gray-800 text-white px-4 py-3 rounded-lg border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm placeholder:text-gray-400;
}
</style>
