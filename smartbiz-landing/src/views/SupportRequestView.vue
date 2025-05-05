<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">🛟 Request Support</h2>
    </div>

    <!-- Support Form -->
    <div class="card p-4 shadow-sm border-0">
      <form @submit.prevent="submitRequest">
        <div class="row g-4">

          <!-- Subject -->
          <div class="col-md-12">
            <label class="form-label">Subject</label>
            <input type="text" class="form-control" v-model="form.subject" required />
          </div>

          <!-- Type of Issue -->
          <div class="col-md-6">
            <label class="form-label">Issue Type</label>
            <select class="form-select" v-model="form.type">
              <option value="technical">Technical Issue</option>
              <option value="billing">Billing/Payments</option>
              <option value="ai-bot">AI Assistant</option>
              <option value="other">Other</option>
            </select>
          </div>

          <!-- Description -->
          <div class="col-md-12">
            <label class="form-label">Describe the Issue</label>
            <textarea class="form-control" rows="4" v-model="form.description" required></textarea>
          </div>

          <!-- Screenshot Upload -->
          <div class="col-md-12">
            <label class="form-label">Upload Screenshot (optional)</label>
            <input type="file" class="form-control" @change="handleFile" />
          </div>

        </div>

        <div class="text-end mt-4">
          <button type="submit" class="btn btn-primary">
            🚀 Submit Request
          </button>
        </div>
      </form>
    </div>

    <!-- Success Alert -->
    <div v-if="successMessage" class="alert alert-success alert-dismissible fade show mt-4">
      ✅ {{ successMessage }}
      <button type="button" class="btn-close" @click="successMessage = ''"></button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const form = ref({
  subject: '',
  type: 'technical',
  description: '',
  attachment: null
})

const successMessage = ref('')

function handleFile(event) {
  form.value.attachment = event.target.files[0]
}

async function submitRequest() {
  const formData = new FormData()
  formData.append('subject', form.value.subject)
  formData.append('type', form.value.type)
  formData.append('description', form.value.description)
  if (form.value.attachment) {
    formData.append('attachment', form.value.attachment)
  }

  try {
    await axios.post('/api/support', formData)
    successMessage.value = 'Support request submitted successfully!'
    form.value = { subject: '', type: 'technical', description: '', attachment: null }
  } catch (err) {
    console.error('Support submission failed', err)
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
