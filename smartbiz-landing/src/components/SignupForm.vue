<template>
  <form @submit.prevent="signup" autocomplete="off">
    <!-- FULL NAME -->
    <div class="mb-3">
      <label for="fullname" class="form-label text-warning">Full Name</label>
      <FormInput id="fullname" icon="person-fill" placeholder="Enter your full name" v-model="form.full_name" required />
    </div>
    <!-- ...weka fields zingine zote hapa... -->
    <!-- BUTTON -->
    <button type="submit" class="btn btn-warning w-100 fw-bold text-dark" :disabled="loading">
      <span v-if="!loading">Signup</span>
      <span v-else><i class="bi bi-arrow-repeat spinner-border spinner-border-sm me-1"></i> Signing Up...</span>
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import FormInput from '@/components/shared/FormInput.vue'
import FormSelect from '@/components/shared/FormSelect.vue'

const toast = useToast()
const form = ref({
  full_name: '',
  username: '',
  email: '',
  password: '',
  phone_number: '',
  language: 'sw',
  business_name: '',
  business_type: ''
})
const loading = ref(false)

const signup = async () => {
  loading.value = true
  try {
    // ... API logic ...
    toast.success('✅ Account created successfully!')
    window.location.href = '/login'
  } catch (err) {
    toast.error(err.response?.data?.detail || '❌ Signup failed. Please try again.')
  } finally {
    loading.value = false
  }
}
</script>
