<template>
  <div class="container mt-5">
    <div class="card shadow-sm p-4">
      <h3 class="fw-bold text-primary mb-4">📺 Live Stream Settings</h3>

      <!-- Step 1: Stream Type -->
      <div v-if="step === 1">
        <h5 class="mb-3">Step 1: Choose Stream Type</h5>
        <div class="form-check form-switch mb-3">
          <input class="form-check-input" type="checkbox" v-model="isPrivate" id="privateSwitch">
          <label class="form-check-label" for="privateSwitch">
            {{ isPrivate ? 'Private (Only invited users)' : 'Public (Anyone with the link)' }}
          </label>
        </div>
        <button class="btn btn-primary" @click="nextStep">Next</button>
      </div>

      <!-- Step 2: Schedule Stream -->
      <div v-else-if="step === 2">
        <h5 class="mb-3">Step 2: Schedule Date & Time</h5>
        <div class="mb-3">
          <label class="form-label">Start Time</label>
          <input type="datetime-local" class="form-control" v-model="startTime" />
        </div>
        <div class="mb-3">
          <label class="form-label">End Time</label>
          <input type="datetime-local" class="form-control" v-model="endTime" />
        </div>
        <div class="d-flex justify-content-between">
          <button class="btn btn-secondary" @click="prevStep">Back</button>
          <button class="btn btn-primary" @click="nextStep">Next</button>
        </div>
      </div>

      <!-- Step 3: Preview & Save -->
      <div v-else-if="step === 3">
        <h5 class="mb-3">Step 3: Confirm & Save</h5>
        <ul class="list-group mb-3">
          <li class="list-group-item">
            <strong>Type:</strong> {{ isPrivate ? 'Private' : 'Public' }}
          </li>
          <li class="list-group-item">
            <strong>Start:</strong> {{ formatDate(startTime) }}
          </li>
          <li class="list-group-item">
            <strong>End:</strong> {{ formatDate(endTime) }}
          </li>
        </ul>
        <div class="d-flex justify-content-between">
          <button class="btn btn-secondary" @click="prevStep">Back</button>
          <button class="btn btn-success" @click="saveSettings">Save & Continue</button>
        </div>
      </div>

      <!-- Step 4: Success -->
      <div v-else>
        <div class="alert alert-success">
          ✅ Live stream settings saved successfully!
        </div>
        <router-link class="btn btn-primary" to="/live-stream">Go to Live Stream Hub</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const step = ref(1)
const isPrivate = ref(false)
const startTime = ref('')
const endTime = ref('')

const nextStep = () => step.value++
const prevStep = () => step.value--

const formatDate = (value) => {
  if (!value) return 'Not set'
  return new Date(value).toLocaleString()
}

const saveSettings = () => {
  // Hapa unaweza kuwasilisha kwa API kama /api/livestream/settings
  console.log({
    privacy: isPrivate.value ? 'private' : 'public',
    start: startTime.value,
    end: endTime.value
  })
  step.value++
}
</script>

<style scoped>
.container {
  max-width: 700px;
}
</style>
