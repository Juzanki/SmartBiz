<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">💼 Affiliate Dashboard</h2>
      <span class="badge bg-info">Promote & Earn</span>
    </div>

    <!-- Referral Link Card -->
    <div class="card shadow-sm p-4 mb-4">
      <h5 class="text-primary mb-2">🔗 Your Smart Referral Link</h5>
      <div class="input-group">
        <input type="text" class="form-control" :value="referralLink" readonly>
        <button class="btn btn-outline-secondary" @click="copyLink">📋 Copy</button>
      </div>
      <small class="text-muted">Share this link on your social media, livestream, or chat groups.</small>
    </div>

    <!-- Commission Summary -->
    <div class="row g-4 mb-4">
      <div class="col-md-4">
        <div class="card p-3 text-center shadow-sm">
          <h6 class="text-muted">Total Earnings</h6>
          <h4 class="text-success">{{ earnings }} TZS</h4>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card p-3 text-center shadow-sm">
          <h6 class="text-muted">Referrals</h6>
          <h4>{{ referrals.length }}</h4>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card p-3 text-center shadow-sm">
          <h6 class="text-muted">Pending Payout</h6>
          <h4 class="text-warning">{{ pending }} TZS</h4>
        </div>
      </div>
    </div>

    <!-- Referral Activity -->
    <div class="card p-4 shadow-sm">
      <h5 class="text-primary mb-3">📊 Referral Activity</h5>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Product</th>
            <th>Buyer</th>
            <th>Commission</th>
            <th>Status</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in referrals" :key="r.id">
            <td>{{ r.product }}</td>
            <td>{{ r.buyer }}</td>
            <td>{{ r.amount }} TZS</td>
            <td>
              <span :class="r.status === 'paid' ? 'text-success' : 'text-warning'">
                {{ r.status }}
              </span>
            </td>
            <td>{{ formatDate(r.date) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const referralLink = ref('')
const referrals = ref([])
const earnings = ref(0)
const pending = ref(0)

onMounted(async () => {
  const res = await axios.get('/api/affiliate/me')
  referralLink.value = res.data.link
  referrals.value = res.data.history
  earnings.value = res.data.total_earned
  pending.value = res.data.pending_payout
})

function copyLink() {
  navigator.clipboard.writeText(referralLink.value)
  alert('Link copied!')
}

function formatDate(date) {
  return new Date(date).toLocaleDateString()
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
