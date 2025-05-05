<template>
  <div>
    <div class="grid md:grid-cols-2 gap-6 mb-6">
      <input v-model="profile.name" type="text" placeholder="Full Name" class="p-3 border rounded-lg" />
      <input v-model="profile.username" type="text" placeholder="Username" class="p-3 border rounded-lg" />
      <input v-model="profile.email" type="email" placeholder="Email" class="p-3 border rounded-lg" />
      <input v-model="profile.phone" type="text" placeholder="Phone" class="p-3 border rounded-lg" />
    </div>

    <div class="mb-6">
      <label>Profile Picture</label>
      <input type="file" @change="handleFileUpload" class="block mt-1" />
      <div v-if="profile.photoUrl" class="mt-4">
        <img :src="profile.photoUrl" class="h-24 w-24 rounded-full object-cover" />
      </div>
    </div>

    <div class="text-right">
      <button @click="saveProfile" class="bg-blue-900 text-white px-6 py-3 rounded-lg font-bold hover:bg-blue-800">
        Save Profile
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const profile = ref({
  name: 'Jane Doe',
  username: 'jdoe',
  email: 'jane@example.com',
  phone: '+255 700 000 000',
  photoUrl: ''
})

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (file) {
    profile.value.photoUrl = URL.createObjectURL(file)
  }
}

const saveProfile = () => {
  console.log('Profile Saved:', profile.value)
  alert('Profile updated!')
}
</script>
