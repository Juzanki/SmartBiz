<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">📡 Start Live Stream</h2>
    </div>

    <!-- Eligibility Notice -->
    <div class="alert alert-info mb-4">
      ⚠️ Only users with an active <strong>SmartBiz subscription</strong> can start a Live Stream.
    </div>

    <!-- Live Stream Setup -->
    <div class="card p-4 shadow-sm border-0">
      <form @submit.prevent="startLive">
        <div class="mb-3">
          <label class="form-label">Live Title</label>
          <input type="text" class="form-control" v-model="form.title" required>
        </div>

        <div class="mb-3">
          <label class="form-label">Select Category</label>
          <select class="form-select" v-model="form.category">
            <option value="fashion">Fashion</option>
            <option value="electronics">Electronics</option>
            <option value="training">Training</option>
            <option value="entertainment">Entertainment</option>
            <option value="business">Business Pitch</option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Select Products to Show (Fly-Over)</label>
          <div class="row g-2">
            <div v-for="product in products" :key="product.id" class="col-md-4">
              <div class="form-check border rounded p-2">
                <input class="form-check-input" type="checkbox" :id="product.id" :value="product.id" v-model="form.selected">
                <label class="form-check-label" :for="product.id">
                  {{ product.name }} - {{ product.price }} TZS
                </label>
              </div>
            </div>
          </div>
        </div>

        <div class="text-end">
          <button type="submit" class="btn btn-primary">
            🎥 Go Live Now
          </button>
        </div>
      </form>
    </div>

    <!-- Feedback -->
    <div v-if="message" class="alert alert-success mt-4">{{ message }}</div>
    <div v-if="error" class="alert alert-danger mt-4">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form = ref({
  title: '',
  category: 'fashion',
  selected: []
})
const products = ref([])
const message = ref('')
const error = ref('')

onMounted(async () => {
  try {
    const res = await axios.get('/api/products/my')
    products.value = res.data
  } catch (err) {
    error.value = 'Failed to load your products.'
  }
})

async function startLive() {
  try {
    const payload = {
      ...form.value
    }
    const res = await axios.post('/api/live/start', payload)
    message.value = '✅ Your live session has started successfully!'
    error.value = ''
  } catch (err) {
    error.value = err.response?.data?.detail || '❌ Failed to start live.'
    message.value = ''
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
