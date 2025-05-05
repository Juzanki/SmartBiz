<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import AuthLayout from '@/layouts/AuthLayout.vue'

const toast = useToast()
const code = ref('')
const loading = ref(false)

const verify2FA = async () => {
  loading.value = true
  try {
    const res = await axios.post('/auth/verify-2fa', { code: code.value })

    // ✅ Save token + user info
    localStorage.setItem('access_token', res.data.access_token)
    localStorage.setItem('user_role', res.data.user.role)
    localStorage.setItem('user_lang', res.data.user.language || 'en')

    toast.success('✅ 2FA Verified Successfully!')

    // 👉 Redirect based on role
    if (res.data.user.role === 'admin') window.location.href = '/dashboard/admin'
    else if (res.data.user.role === 'owner') window.location.href = '/dashboard/owner'
    else window.location.href = '/dashboard'

  } catch (err) {
    console.error(err)
    toast.error(err.response?.data?.detail || '❌ Invalid 2FA code.')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <AuthLayout>
    <div>
      <h2 class="text-3xl font-bold text-center mb-4 text-white">Two-Factor Verification</h2>
      <p class="text-sm text-center text-gray-300 mb-6">
        Enter the 6-digit code sent to your registered email or phone number.
      </p>

      <form @submit.prevent="verify2FA" class="space-y-4">
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

      <p class="text-center text-sm text-gray-400 mt-6">
        Didn't get the code?
        <a href="#" @click.prevent="toast.info('⏳ Resend link coming soon')" class="text-blue-400 hover:underline">Resend Code</a>
      </p>
    </div>
  </AuthLayout>
</template>

<style scoped>
.input {
  @apply w-full bg-gray-800 text-white px-4 py-3 rounded-lg border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm placeholder:text-gray-400;
}
</style>
