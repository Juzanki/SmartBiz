<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">📣 Create Referral Campaign</h2>
    </div>

    <div class="card p-4 shadow-sm border-0">
      <form @submit.prevent="createCampaign">
        <div class="mb-3">
          <label class="form-label">Campaign Title</label>
          <input v-model="form.title" class="form-control" required />
        </div>

        <div class="mb-3">
          <label class="form-label">Product to Promote</label>
          <select v-model="form.product_id" class="form-select" required>
            <option v-for="p in products" :key="p.id" :value="p.id">
              {{ p.name }} - {{ p.price }} TZS
            </option>
          </select>
        </div>

        <div class="mb-3">
          <label class="form-label">Commission Rate (%)</label>
          <input type="number" v-model.number="form.rate" class="form-control" min="1" max="50" required />
        </div>

        <div class="mb-3">
          <label class="form-label">Campaign Duration (days)</label>
          <input type="number" v-model.number="form.duration" class="form-control" min="1" required />
        </div>

        <div class="text-end">
          <button type="submit" class="btn btn-primary">🚀 Launch Campaign</button>
        </div>
      </form>
    </div>

    <div v-if="success" class="alert alert-success mt-4">{{ success }}</div>
    <div v-if="error" class="alert alert-danger mt-4">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form = ref({
  title: '',
  product_id: '',
  rate: 10,
  duration: 7
})
const products = ref([])
const success = ref('')
const error = ref('')

onMounted(async () => {
  const res = await axios.get('/api/products/my')
  products.value = res.data
})

async function createCampaign() {
  try {
    await axios.post('/api/campaigns/create', form.value)
    success.value = 'Campaign created successfully!'
    error.value = ''
    form.value = { title: '', product_id: '', rate: 10, duration: 7 }
  } catch (e) {
    error.value = e.response?.data?.detail || 'Something went wrong.'
    success.value = ''
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
