<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">🚀 Available Campaigns</h2>
      <span class="badge bg-info">Affiliate Marketplace</span>
    </div>

    <div class="row g-4">
      <div v-for="c in campaigns" :key="c.id" class="col-md-4">
        <div class="card p-3 shadow-sm border-0 h-100 d-flex flex-column justify-content-between">
          <div>
            <h5 class="text-primary">{{ c.title }}</h5>
            <p class="mb-1 text-muted">{{ c.product.name }} - {{ c.product.price }} TZS</p>
            <p class="mb-1">Commission: <strong>{{ c.commission_rate }}%</strong></p>
            <small class="text-muted">Ends: {{ formatDate(c.ends_at) }}</small>
          </div>
          <button class="btn btn-outline-success mt-3" @click="joinCampaign(c.id)">
            🤝 Join Campaign
          </button>
        </div>
      </div>
    </div>

    <div v-if="message" class="alert alert-success mt-4">{{ message }}</div>
    <div v-if="error" class="alert alert-danger mt-4">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const campaigns = ref([])
const message = ref('')
const error = ref('')

onMounted(async () => {
  const res = await axios.get('/api/campaigns/available')
  campaigns.value = res.data
})

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}

async function joinCampaign(id) {
  try {
    await axios.post(`/api/campaigns/join/${id}`)
    message.value = 'Successfully joined the campaign!'
    error.value = ''
  } catch (err) {
    error.value = err.response?.data?.detail || 'Failed to join.'
    message.value = ''
  }
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
  transition: transform 0.3s ease;
}
.card:hover {
  transform: scale(1.02);
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}
</style>
