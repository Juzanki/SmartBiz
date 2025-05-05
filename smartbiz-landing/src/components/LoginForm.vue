<template>
  <div class="w-full max-w-md bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 space-y-6">
    <!-- Logo -->
    <div class="flex justify-center">
      <img
        src="@/assets/logo.svg"
        alt="SmartBiz Logo"
        class="h-16 w-16 rounded-full shadow border border-gray-300 dark:border-gray-600"
      />
    </div>

    <!-- Title -->
    <h2 class="text-2xl md:text-3xl font-bold text-center text-blue-900 dark:text-white">
      Welcome Back 👋
    </h2>

    <!-- Form -->
    <form @submit.prevent="handleLogin" class="space-y-4">
      <input
        v-model="form.identifier"
        type="text"
        placeholder="📧 Email / Phone / Username"
        class="input-field"
        required
      />
      <input
        v-model="form.password"
        type="password"
        placeholder="🔒 Password"
        class="input-field"
        required
      />
      <button
        type="submit"
        class="w-full bg-blue-900 text-white py-3 rounded-lg font-semibold hover:bg-blue-800 transition duration-300 ease-in-out"
      >
        {{ loading ? 'Logging In...' : 'Login' }}
      </button>
    </form>

    <!-- Signup Link -->
    <p class="text-center text-sm text-gray-600 dark:text-gray-300">
      Don't have an account?
      <router-link
        to="/signup"
        class="text-blue-700 dark:text-blue-400 font-semibold hover:underline transition"
      >
        Sign Up
      </router-link>
    </p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginPage',
  data() {
    return {
      loading: false,
      form: {
        identifier: '',
        password: ''
      }
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      try {
        const res = await axios.post('/auth/login', this.form)
        const user = res.data.user

        localStorage.setItem('access_token', res.data.access_token)
        localStorage.setItem('user_role', user.role)
        localStorage.setItem('user_lang', user.language || 'en')
        this.$i18n.locale = user.language || 'en'

        // Navigate based on role
        if (user.role === 'admin') this.$router.push('/dashboard/admin')
        else if (user.role === 'owner') this.$router.push('/dashboard/owner')
        else this.$router.push('/dashboard')
      } catch (err) {
        alert('⚠️ Login failed. Please check your credentials.')
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.input-field {
  @apply w-full px-4 py-3 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-gray-700 dark:text-white dark:border-gray-600;
}
</style>
