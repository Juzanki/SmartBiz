<template>
  <form @submit.prevent="handleSubmit">
    <div class="row g-4">
      <!-- Avatar -->
      <div class="col-md-12 text-center">
        <img :src="model.avatar || defaultAvatar" alt="Avatar"
             class="rounded-circle mb-2" style="width:100px; height:100px; object-fit:cover;">
        <div class="form-text mb-2">Avatar (Paste Image URL)</div>
        <input type="url" class="form-control w-50 mx-auto" placeholder="https://..." v-model="model.avatar">
      </div>

      <!-- Full Name -->
      <div class="col-md-6">
        <label class="form-label">👤 Full Name</label>
        <input type="text" class="form-control" v-model="model.fullName" required>
      </div>

      <!-- Email -->
      <div class="col-md-6">
        <label class="form-label">📧 Email Address</label>
        <input type="email" class="form-control" v-model="model.email" required>
      </div>

      <!-- Phone -->
      <div class="col-md-6">
        <label class="form-label">📞 Phone Number</label>
        <input type="text" class="form-control" v-model="model.phone">
      </div>

      <!-- Password -->
      <div class="col-md-6">
        <label class="form-label">🔒 New Password</label>
        <input type="password" class="form-control" v-model="model.password" placeholder="Leave blank to keep current">
      </div>

      <!-- Location -->
      <div class="col-md-6">
        <label class="form-label">📍 Location</label>
        <input type="text" class="form-control" v-model="model.location">
      </div>

      <!-- Bio -->
      <div class="col-md-6">
        <label class="form-label">📝 Short Bio</label>
        <textarea class="form-control" rows="2" v-model="model.bio" placeholder="About you..."></textarea>
      </div>

      <!-- Notification -->
      <div class="col-md-12">
        <label class="form-label">🔔 Notification Preference</label>
        <select class="form-select" v-model="model.notificationPreference">
          <option value="">-- Select --</option>
          <option>Email</option>
          <option>SMS</option>
          <option>Both</option>
        </select>
      </div>
    </div>

    <div class="text-end mt-4">
      <button class="btn btn-primary" type="submit">
        💾 Save Changes
      </button>
    </div>
  </form>
</template>

<script setup>
import { reactive, watch } from 'vue'

const defaultAvatar = '/default-avatar.png'
const props = defineProps({
  profile: { type: Object, required: true }
})
const emit = defineEmits(['submit'])

const model = reactive({ ...props.profile })

watch(() => props.profile, (newVal) => {
  Object.assign(model, newVal)
})

function handleSubmit() {
  emit('submit', { ...model })
}
</script>

<style scoped>
img {
  box-shadow: 0 0 4px rgba(0, 0, 0, 0.1);
}
</style>
