<!-- src/components/DashboardAdminForm.vue -->
<template>
  <form
    class="bg-white rounded-xl shadow p-6 max-w-lg mx-auto flex flex-col gap-4 border border-yellow-300"
    @submit.prevent="handleSubmit"
    autocomplete="off"
  >
    <h3 class="text-xl font-semibold text-blue-900 mb-2">
      {{ formTitle }}
    </h3>

    <!-- System/Business Name -->
    <div>
      <label for="businessName" class="block text-sm font-medium text-blue-900 mb-1">System/Business Name</label>
      <input
        id="businessName"
        v-model="form.businessName"
        type="text"
        placeholder="System or business name"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Admin Email -->
    <div>
      <label for="businessEmail" class="block text-sm font-medium text-blue-900 mb-1">Admin Email</label>
      <input
        id="businessEmail"
        v-model="form.businessEmail"
        type="email"
        placeholder="e.g. admin@yourbiz.com"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Admin Phone -->
    <div>
      <label for="businessPhone" class="block text-sm font-medium text-blue-900 mb-1">Phone</label>
      <input
        id="businessPhone"
        v-model="form.businessPhone"
        type="tel"
        placeholder="+255..."
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Description (optional) -->
    <div>
      <label for="desc" class="block text-sm font-medium text-blue-900 mb-1">Short Description</label>
      <textarea
        id="desc"
        v-model="form.businessDesc"
        rows="3"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        placeholder="Describe your system or business (optional)"
      ></textarea>
    </div>

    <!-- Feedback Message -->
    <transition name="fade">
      <div v-if="successMsg" class="text-green-600 bg-green-50 border border-green-200 px-3 py-2 rounded text-center font-medium shadow-sm">
        {{ successMsg }}
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
        <svg class="animate-spin inline h-5 w-5 mr-1" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"/><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8z"/></svg>
        Saving...
      </span>
    </button>
  </form>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  formTitle: { type: String, default: 'Business/System Settings' },
  initialData: { type: Object, default: () => ({}) }
})

const emit = defineEmits(['submit'])

const form = ref({
  businessName: props.initialData.businessName || '',
  businessEmail: props.initialData.businessEmail || '',
  businessPhone: props.initialData.businessPhone || '',
  businessDesc: props.initialData.businessDesc || '',
})
const loading = ref(false)
const successMsg = ref('')

const handleSubmit = async () => {
  loading.value = true
  successMsg.value = ''
  // Fanya submission hapa (API/emit)
  setTimeout(() => {
    loading.value = false
    successMsg.value = '✔️ Changes saved successfully!'
    emit('submit', { ...form.value })
    setTimeout(() => (successMsg.value = ''), 2200)
  }, 1200)
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .4s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>
