<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">📦 My Joined Campaigns</h2>
    </div>

    <div v-if="joined.length" class="row g-4">
      <div v-for="c in joined" :key="c.id" class="col-md-4">
        <div class="card p-3 shadow-sm border-0 h-100">
          <h5 class="text-primary">{{ c.title }}</h5>
          <p class="mb-1 text-muted">{{ c.product.name }} - {{ c.product.price }} TZS</p>
          <p>Commission: {{ c.commission_rate }}%</p>
          <small class="text-muted">Ends: {{ formatDate(c.ends_at) }}</small>
        </div>
      </div>
    </div>

    <div v-else class="alert alert-info">You haven’t joined any campaigns yet.</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const joined = ref([])

onMounted(async () => {
  const res = await axios.get('/api/campaigns/my')
  joined.value = res.data
})

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
