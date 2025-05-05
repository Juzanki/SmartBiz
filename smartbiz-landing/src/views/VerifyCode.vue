<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import AuthLayout from '@/layouts/AuthLayout.vue'

const toast = useToast()

const code = ref('')
const loading = ref(false)

const verifyCode = async () => {
  loading.value = true
  try {
    const res = await axios.post('/auth/verify-code', { code: code.value })

    // ✅ Hifadhi token au identifier ya reset (ikihitajika kwenye hatua inayofuata)
    localStorage.setItem('reset_token', res.data.reset_token)

    toast.success('✅ Code verified! Now reset your password.')
    window.location.href = '/reset-password'
  } catch (err) {
    console.error(err)
    toast.error(err.response?.data?.detail || '❌ Invalid code. Please try again.')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <div>
      <!-- Title -->
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Enter Verification Code</h2>

      <!-- Instructions -->
      <p class="text-sm text-center text-gray-300 mb-6">
        We've sent a 6-digit code to your email or phone. Enter it below to continue.
      </p>

      <!-- Form -->
      <form @submit.prevent="verifyCode" class="space-y-4">
        <input
          v-model="code"
          type="text"
          maxlength="6"
          placeholder="🔐 Enter 6-digit code"
          class="input"
          required
        />

        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-all disabled:bg-gray-500 disabled:cursor-not-allowed"
        >
          <span v-if="!loading">Verify Code</span>
          <span v-else>Verifying...</span>
        </button>
      </form>

      <!-- Go Back -->
      <p class="text-center text-sm text-gray-400 mt-6">
        Didn't get the code?
        <router-link to="/forgot-password" class="text-blue-400 hover:underline">Request Again</router-link>
      </p>
    </div>
  </AuthLayout>
</template>

<style scoped>
.input {
  @apply w-full bg-gray-800 text-white px-4 py-3 rounded-lg border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm placeholder:text-gray-400;
}
</style>
