// src/stores/auth.js
import { reactive, computed } from 'vue'

const state = reactive({
  accessToken: localStorage.getItem('access_token') || null,
  userRole: localStorage.getItem('user_role') || 'guest'
})

export function useAuthStore() {
  // Reactivity for isLoggedIn
  const isLoggedIn = computed(() => !!state.accessToken)
  const role = computed(() => state.userRole)

  // Call this after login/logout to update state
  function refresh() {
    state.accessToken = localStorage.getItem('access_token') || null
    state.userRole = localStorage.getItem('user_role') || 'guest'
  }

  // Optional: logout helper
  function logout() {
    localStorage.removeItem('access_token')
    localStorage.removeItem('user_role')
    refresh()
  }

  return {
    isLoggedIn,
    userRole: role,
    refresh,
    logout
  }
}
