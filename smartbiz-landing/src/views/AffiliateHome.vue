<template>
  <div class="container py-5">
    <div class="mb-4 d-flex justify-between items-center">
      <h2 class="text-primary fw-bold">🌟 Affiliate Center</h2>
      <span class="badge bg-info">Earn & Grow</span>
    </div>

    <!-- Summary Cards -->
    <div class="row g-4 mb-4">
      <div class="col-md-4">
        <div class="card text-center p-3 shadow-sm">
          <h6 class="text-muted">Total Earned</h6>
          <h4 class="text-success">{{ summary.earned }} TZS</h4>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card text-center p-3 shadow-sm">
          <h6 class="text-muted">Referrals</h6>
          <h4>{{ summary.referrals }}</h4>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card text-center p-3 shadow-sm">
          <h6 class="text-muted">Pending Payout</h6>
          <h4 class="text-warning">{{ summary.pending }} TZS</h4>
        </div>
      </div>
    </div>

    <!-- Referral Link -->
    <div class="card p-4 shadow-sm mb-5">
      <h5 class="mb-2">🔗 Your Referral Link</h5>
      <div class="input-group">
        <input type="text" class="form-control" :value="summary.link" readonly />
        <button class="btn btn-outline-secondary" @click="copyLink">📋 Copy</button>
      </div>
    </div>

    <!-- Campaigns Joined Preview -->
    <div class="card p-4 shadow-sm mb-4">
      <h5 class="mb-3 text-primary">📦 My Campaigns</h5>
      <ul class="list-group list-group-flush">
        <li v-for="c in joined.slice(0, 3)" :key="c.id" class="list-group-item">
          <strong>{{ c.title }}</strong> — {{ c.product.name }} ({{ c.commission_rate }}%)
        </li>
      </ul>
      <router-link to="/my-campaigns" class="btn btn-sm btn-link mt-2">View all</router-link>
    </div>

    <!-- Leaderboard Preview -->
    <div class="card p-4 shadow-sm">
      <h5 class="mb-3 text-primary">🏆 Top Promoters</h5>
      <ul class="list-group list-group-flush">
        <li v-for="(user, i) in leaderboard.slice(0, 5)" :key="user.username" class="list-group-item">
          <strong>#{{ i+1 }}</strong> {{ user.username }} — {{ user.earned }} TZS
        </li>
      </ul>
      <router-link to="/promoter-leaderboard" class="btn btn-sm btn-link mt-2">View leaderboard</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const summary = ref({ earned: 0, referrals: 0, pending: 0, link: '' })
const joined = ref([])
const leaderboard = ref([])

onMounted(async () => {
  const a = await axios.get('/api/affiliate/me')
  summary.value = {
    earned: a.data.total_earned,
    referrals: a.data.history.length,
    pending: a.data.pending_payout,
    link: a.data.link
  }
  const c = await axios.get('/api/campaigns/my')
  joined.value = c.data
  const l = await axios.get('/api/affiliate/leaderboard')
  leaderboard.value = l.data
})

function copyLink() {
  navigator.clipboard.writeText(summary.value.link)
  alert('Link copied!')
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
