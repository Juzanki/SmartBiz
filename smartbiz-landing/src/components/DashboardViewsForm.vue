<!-- src/components/DashboardViewsForm.vue -->
<template>
  <form
    class="bg-white rounded-xl shadow p-6 max-w-lg mx-auto flex flex-col gap-4 border border-yellow-300"
    @submit.prevent="handleSubmit"
    autocomplete="off"
  >
    <h3 class="text-xl font-bold text-blue-900 mb-2">
      {{ $t('quick_profile_edit') || 'Quick Profile Edit' }}
    </h3>

    <!-- Full Name -->
    <div>
      <label for="fullName" class="block text-sm font-medium text-blue-900 mb-1">
        {{ $t('full_name') || 'Full Name' }}
      </label>
      <input
        id="fullName"
        v-model.trim="form.fullName"
        type="text"
        autocomplete="name"
        :placeholder="$t('enter_full_name') || 'Enter full name'"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Email -->
    <div>
      <label for="userEmail" class="block text-sm font-medium text-blue-900 mb-1">
        {{ $t('email') || 'Email' }}
      </label>
      <input
        id="userEmail"
        v-model.trim="form.email"
        type="email"
        autocomplete="email"
        :placeholder="$t('your_email') || 'your@email.com'"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        required
      />
    </div>

    <!-- Phone Number -->
    <div>
      <label for="phone" class="block text-sm font-medium text-blue-900 mb-1">
        {{ $t('phone') || 'Phone' }}
      </label>
      <input
        id="phone"
        v-model.trim="form.phone"
        type="tel"
        autocomplete="tel"
        :placeholder="$t('your_phone') || '+255...'"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
      />
    </div>

    <!-- Change Password (optional) -->
    <div>
      <label for="password" class="block text-sm font-medium text-blue-900 mb-1">
        {{ $t('change_password') || 'Change Password' }}
      </label>
      <input
        id="password"
        v-model="form.password"
        type="password"
        :placeholder="$t('new_password') || '•••••••••••'"
        class="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-yellow-400"
        autocomplete="new-password"
      />
      <small class="text-xs text-gray-500">{{ $t('leave_blank_to_keep') || 'Leave blank to keep your current password.' }}</small>
    </div>

    <!-- Notifications -->
    <div class="flex items-center gap-2">
      <input
        id="notif"
        type="checkbox"
        v-model="form.notifications"
        class="form-checkbox h-4 w-4 text-yellow-500 rounded"
      />
      <label for="notif" class="text-sm text-blue-900">
        {{ $t('enable_notifications') || 'Enable notifications' }}
      </label>
    </div>

    <!-- Submit Button -->
    <button
      type="submit"
      class="bg-yellow-400 text-blue-900 font-bold rounded-lg py-2 px-4 shadow hover:bg-yellow-300 transition"
      :disabled="loading"
    >
      <span v-if="!loading">{{ $t('save_changes') || 'Save Changes' }}</span>
      <span v-else>{{ $t('saving') || 'Saving...' }}</span>
    </button>

    <!-- Error/Success Slot (Optional, e.g. for toast or validation) -->
    <slot name="feedback"></slot>
  </form>
</template>

<script setup>
import { ref, defineProps, defineEmits, watch } from 'vue'

// Props: modelValue enables v-model support
const props = defineProps({
  modelValue: {
    type: Object,
    default: () => ({
      fullName: '',
      email: '',
      phone: '',
      notifications: true
    })
  }
})
const emit = defineEmits(['update:modelValue', 'saved'])

// Local form state
const form = ref({
  fullName: props.modelValue.fullName || '',
  email: props.modelValue.email || '',
  phone: props.modelValue.phone || '',
  password: '',
  notifications: props.modelValue.notifications ?? true
})
const loading = ref(false)

// Watch for prop changes and update form
watch(
  () => props.modelValue,
  (val) => {
    form.value = {
      fullName: val.fullName || '',
      email: val.email || '',
      phone: val.phone || '',
      password: '',
      notifications: val.notifications ?? true
    }
  },
  { deep: true }
)

// Handle form submission
const handleSubmit = async () => {
  loading.value = true
  // Simulate backend call (replace with API in production)
  setTimeout(() => {
    loading.value = false
    // Remove password if blank
    const payload = { ...form.value }
    if (!payload.password) delete payload.password
    // Emit to parent component
    emit('update:modelValue', payload)
    emit('saved', payload) // For showing toast at parent
    form.value.password = ''
  }, 900)
}
</script>
