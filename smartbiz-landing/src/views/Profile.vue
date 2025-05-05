<template>
  <DashboardLayout>
    <div class="p-6 max-w-xl mx-auto">
      <h2 class="text-2xl font-bold mb-4">{{ $t('profile') }}</h2>
      <p class="text-gray-600 mb-6">{{ $t('profile_intro') }}</p>

      <!-- Profile Picture -->
      <div class="flex items-center gap-4 mb-6">
        <img :src="profile.photo || defaultPhoto" alt="Profile" class="w-16 h-16 rounded-full object-cover border" />
        <input type="file" @change="handlePhotoUpload" accept="image/*" />
      </div>

      <form @submit.prevent="saveProfile" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">{{ $t('full_name') }}</label>
          <input v-model="profile.fullName" class="w-full p-2 border rounded" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">{{ $t('email') }}</label>
          <input v-model="profile.email" type="email" class="w-full p-2 border rounded" />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">{{ $t('language') }}</label>
          <select v-model="profile.language" class="w-full p-2 border rounded">
            <option value="en">🇬🇧 English</option>
            <option value="sw">🇰🇪 Kiswahili</option>
            <option value="fr">🇫🇷 Français</option>
          </select>
        </div>

        <!-- Change Password Section -->
        <div class="pt-6 border-t">
          <label class="block text-sm font-medium text-gray-700">{{ $t('new_password') }}</label>
          <input v-model="password.new" type="password" class="w-full p-2 border rounded" placeholder="********" />

          <label class="block text-sm font-medium text-gray-700 mt-4">{{ $t('confirm_password') }}</label>
          <input v-model="password.confirm" type="password" class="w-full p-2 border rounded" placeholder="********" />
        </div>

        <button type="submit" class="bg-blue-900 text-white px-4 py-2 rounded hover:bg-blue-800">
          {{ $t('save_changes') }}
        </button>
      </form>
    </div>
  </DashboardLayout>
</template>

<script setup>
import { ref } from 'vue'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

const defaultPhoto = 'https://via.placeholder.com/150'

const profile = ref({
  fullName: localStorage.getItem('user_name') || '',
  email: localStorage.getItem('user_email') || '',
  language: localStorage.getItem('user_lang') || 'en',
  photo: localStorage.getItem('user_photo') || ''
})

const password = ref({ new: '', confirm: '' })

function saveProfile() {
  if (password.value.new && password.value.new !== password.value.confirm) {
    alert('Passwords do not match')
    return
  }

  localStorage.setItem('user_name', profile.value.fullName)
  localStorage.setItem('user_email', profile.value.email)
  localStorage.setItem('user_lang', profile.value.language)
  localStorage.setItem('user_photo', profile.value.photo)
  if (password.value.new) {
    localStorage.setItem('user_password', password.value.new)
  }
  location.reload() // Refresh i18n if needed
}

function handlePhotoUpload(event) {
  const file = event.target.files[0]
  if (!file) return
  const reader = new FileReader()
  reader.onload = (e) => {
    profile.value.photo = e.target.result
  }
  reader.readAsDataURL(file)
}
</script>

<style scoped>
input, select {
  outline: none;
  border-color: #ccc;
}
input:focus, select:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 1px #3b82f6;
}
</style>
