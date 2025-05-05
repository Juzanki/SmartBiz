<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">✉️ Messaging Center</h2>
    </div>

    <!-- Message Form -->
    <div class="card shadow-sm p-4 border-0">
      <form @submit.prevent="sendMessage">
        <div class="row g-4">
          <!-- Select Customer -->
          <div class="col-md-6">
            <label class="form-label">Select Customer</label>
            <select class="form-select" v-model="form.customerId" required>
              <option value="">-- Select Customer --</option>
              <option v-for="cust in customers" :key="cust.id" :value="cust.id">
                {{ cust.name }} ({{ cust.platform }})
              </option>
            </select>
          </div>

          <!-- Select Platform -->
          <div class="col-md-6">
            <label class="form-label">Select Platform</label>
            <select class="form-select" v-model="form.platform" required>
              <option value="">-- Select Platform --</option>
              <option>WhatsApp</option>
              <option>Telegram</option>
              <option>SMS</option>
              <option>Email</option>
            </select>
          </div>

          <!-- Message Content -->
          <div class="col-12">
            <label class="form-label">Message</label>
            <textarea 
              class="form-control" 
              v-model="form.message" 
              rows="4" 
              placeholder="Type your message here..." 
              required
            ></textarea>
          </div>
        </div>

        <div class="text-end mt-4">
          <button class="btn btn-primary" type="submit">
            🚀 Send Message
          </button>
        </div>
      </form>
    </div>

    <!-- Success Message -->
    <div v-if="successMessage" class="alert alert-success alert-dismissible fade show mt-4" role="alert">
      {{ successMessage }}
      <button type="button" class="btn-close" @click="successMessage = ''"></button>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const customers = ref([])
const successMessage = ref('')
const form = ref({
  customerId: '',
  platform: '',
  message: ''
})

onMounted(() => {
  fetchCustomers()
})

function fetchCustomers() {
  // For demo purposes, fetching customers from localStorage
  const demoCustomers = JSON.parse(localStorage.getItem('my_customers')) || [
    { id: 1, name: 'John Doe', platform: 'WhatsApp' },
    { id: 2, name: 'Jane Smith', platform: 'Telegram' },
    { id: 3, name: 'Ali Khan', platform: 'SMS' }
  ]
  customers.value = demoCustomers
}

function sendMessage() {
  if (!form.value.customerId || !form.value.platform || !form.value.message) {
    alert('Please complete all fields before sending.')
    return
  }

  // Simulate API sending
  setTimeout(() => {
    successMessage.value = 'Message sent successfully to customer!'
    form.value = { customerId: '', platform: '', message: '' }
  }, 1000)
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
textarea {
  resize: none;
}
</style>
