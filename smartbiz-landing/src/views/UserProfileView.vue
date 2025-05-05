<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-3xl mx-auto bg-white rounded-xl shadow p-8">
      <h1 class="text-3xl font-bold text-blue-900 mb-6">User Profile</h1>

      <div class="grid md:grid-cols-2 gap-6 mb-6">
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1">Full Name</label>
          <input
            v-model="profile.name"
            type="text"
            class="w-full p-3 border border-gray-300 rounded-lg"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1">Username</label>
          <input
            v-model="profile.username"
            type="text"
            class="w-full p-3 border border-gray-300 rounded-lg"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1">Email</label>
          <input
            v-model="profile.email"
            type="email"
            class="w-full p-3 border border-gray-300 rounded-lg"
          />
        </div>
        <div>
          <label class="block text-sm font-semibold text-gray-700 mb-1">Phone</label>
          <input
            v-model="profile.phone"
            type="text"
            class="w-full p-3 border border-gray-300 rounded-lg"
          />
        </div>
      </div>

      <!-- Profile Picture -->
      <div class="mb-6">
        <label class="block text-sm font-semibold text-gray-700 mb-2">Profile Picture</label>
        <input type="file" @change="handleFileUpload" class="block" />
        <div v-if="profile.photoUrl" class="mt-4">
          <img :src="profile.photoUrl" class="h-24 w-24 rounded-full object-cover" />
        </div>
      </div>

      <!-- Save Button -->
      <div class="text-right">
        <button
          @click="saveProfile"
          class="bg-blue-900 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-800"
        >
          Save Profile
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'UserProfileView'
})

import { ref } from "vue"

const profile = ref({
  name: "Jane Doe",
  username: "jdoe",
  email: "jane@example.com",
  phone: "+255 700 000 000",
  photoUrl: ""
})

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    profile.value.photoUrl = URL.createObjectURL(file)
  }
}

const saveProfile = () => {
  console.log("Saving profile...", profile.value)
  alert("Profile updated!")
}
</script>

<style scoped>
/* Extra styles can be added */
</style>
