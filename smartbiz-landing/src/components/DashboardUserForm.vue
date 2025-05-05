<template>
  <form
    class="bg-white rounded-xl shadow p-6 max-w-xl mx-auto flex flex-col gap-4 border border-yellow-300"
    @submit.prevent="handleSubmit"
    autocomplete="off"
  >
    <h3 class="text-xl font-bold text-blue-900 mb-2">Update Profile</h3>

    <!-- Full Name -->
    <div>
      <label for="userName" class="block text-sm font-medium text-blue-900 mb-1">Full Name</label>
      <input
        id="userName"
        v-model="form.name"
        type="text"
        placeholder="Your full name"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Email -->
    <div>
      <label for="userEmail" class="block text-sm font-medium text-blue-900 mb-1">Email</label>
      <input
        id="userEmail"
        v-model="form.email"
        type="email"
        placeholder="your@email.com"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Phone Number -->
    <div>
      <label for="userPhone" class="block text-sm font-medium text-blue-900 mb-1">Phone</label>
      <input
        id="userPhone"
        v-model="form.phone"
        type="tel"
        placeholder="+255..."
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
      />
    </div>

    <!-- Notifications (toggle) -->
    <div class="flex items-center gap-2">
      <input
        id="notif"
        type="checkbox"
        v-model="form.notifications"
        class="form-checkbox h-4 w-4 text-yellow-500 rounded"
      />
      <label for="notif" class="text-sm text-blue-900 select-none">Receive Notifications</label>
    </div>

    <!-- Success Feedback -->
    <transition name="fade">
      <div
        v-if="success"
        class="text-green-600 bg-green-50 border border-green-200 px-3 py-2 rounded text-center font-medium shadow-sm"
      >
        ✔️ Profile updated!
      </div>
    </transition>

    <!-- Submit Button -->
    <button
      type="submit"
      class="bg-yellow-400 text-blue-900 font-bold rounded-lg py-2 px-4 shadow hover:bg-yellow-300 transition"
      :disabled="loading"
    >
      <span v-if="!loading">Save Changes</span>
      <span v-else>
        <svg class="animate-spin inline h-5 w-5 mr-1" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/>
        </svg>
        Saving...
      </span>
    </button>
  </form>
</template>

<script setup>
import { ref, watch, defineProps, defineEmits } from 'vue'

const props = defineProps({
  userData: { type: Object, default: () => ({}) }
})

const emit = defineEmits(['update'])

const form = ref({
  name: props.userData.name || '',
  email: props.userData.email || '',
  phone: props.userData.phone || '',
  notifications: props.userData.notifications ?? true
})

const loading = ref(false)
const success = ref(false)

// Sync form with changes to userData
watch(
  () => props.userData,
  (val) => {
    form.value = {
      name: val.name || '',
      email: val.email || '',
      phone: val.phone || '',
      notifications: val.notifications ?? true
    }
  },
  { deep: true }
)

const handleSubmit = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    emit('update', { ...form.value })
    success.value = true
    setTimeout(() => (success.value = false), 2000)
  }, 1000)
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
.form-checkbox:focus {
  outline: 2px solid #ffd600;
  outline-offset: 1px;
}
</style>
