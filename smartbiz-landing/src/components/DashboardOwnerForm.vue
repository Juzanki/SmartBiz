<template>
  <form
    class="bg-white p-6 rounded-xl shadow-md max-w-lg mx-auto border border-yellow-300"
    @submit.prevent="handleSubmit"
    autocomplete="off"
  >
    <h3 class="text-xl font-bold mb-4 text-blue-900">
      {{ $t('update_owner_profile') }}
    </h3>

    <!-- Owner Name -->
    <div class="mb-3">
      <label for="ownerName" class="form-label text-blue-900">{{ $t('full_name') }}</label>
      <input
        id="ownerName"
        v-model="form.ownerName"
        type="text"
        class="form-control"
        :placeholder="$t('enter_full_name')"
        required
      />
    </div>

    <!-- Business Name -->
    <div class="mb-3">
      <label for="businessName" class="form-label text-blue-900">{{ $t('business_name') }}</label>
      <input
        id="businessName"
        v-model="form.businessName"
        type="text"
        class="form-control"
        :placeholder="$t('enter_business_name')"
        required
      />
    </div>

    <!-- Business Domain (Optional) -->
    <div class="mb-3">
      <label for="domain" class="form-label text-blue-900">{{ $t('custom_domain') }}</label>
      <input
        id="domain"
        v-model="form.domain"
        type="text"
        class="form-control"
        :placeholder="$t('your_custom_domain')"
        pattern="^([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
        title="Valid domain only (e.g. smartbiz.co.tz)"
      />
      <small class="text-muted">{{ $t('optional') }}</small>
    </div>

    <!-- Language Select -->
    <div class="mb-4">
      <label for="lang" class="form-label text-blue-900">{{ $t('language') }}</label>
      <select id="lang" v-model="form.language" class="form-select" required>
        <option value="sw">Kiswahili</option>
        <option value="en">English</option>
        <option value="fr">Français</option>
        <option value="ar">العربية</option>
      </select>
    </div>

    <!-- Save Button -->
    <button
      class="btn btn-warning fw-bold text-dark w-100"
      :disabled="loading"
      type="submit"
    >
      <span v-if="!loading">{{ $t('save_changes') }}</span>
      <span v-else>
        <i class="bi bi-arrow-repeat spinner-border spinner-border-sm me-1"></i>
        {{ $t('saving') }}...
      </span>
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useToast } from 'vue-toastification'
import axios from 'axios'

const toast = useToast()
const loading = ref(false)

// Hapa unaweza pokea props/modelValue ili i-react na parent page, au ku-fetch data kutoka backend
const form = ref({
  ownerName: localStorage.getItem('user_name') || '',
  businessName: localStorage.getItem('business_name') || '',
  domain: '',
  language: localStorage.getItem('user_lang') || 'sw',
})

const handleSubmit = async () => {
  loading.value = true
  try {
    // Example: Send to backend
    // await axios.put('/api/owner/profile', form.value)
    // For demo, save locally
    localStorage.setItem('user_name', form.value.ownerName)
    localStorage.setItem('business_name', form.value.businessName)
    localStorage.setItem('user_lang', form.value.language)
    toast.success('✔️ Profile updated successfully!')
  } catch (err) {
    toast.error('❌ Failed to update profile. Try again!')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.form-label { font-weight: 500; }
.form-control, .form-select {
  border-radius: 0.5rem;
  border: 1.5px solid #FFD600;
  box-shadow: none;
}
.form-control:focus, .form-select:focus {
  border-color: #FFD600;
  box-shadow: 0 0 0 2px #FFD60033;
}
</style>
