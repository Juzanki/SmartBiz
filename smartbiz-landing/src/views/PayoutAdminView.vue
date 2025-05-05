<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">💸 Referral Payouts</h2>
      <span class="badge bg-warning">Admin Panel</span>
    </div>

    <!-- Payout Table -->
    <div class="card p-4 shadow-sm border-0">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>#</th>
            <th>Promoter</th>
            <th>Product</th>
            <th>Buyer</th>
            <th>Amount</th>
            <th>Date</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in payouts" :key="r.id">
            <td>{{ r.id }}</td>
            <td>{{ r.promoter }}</td>
            <td>{{ r.product }}</td>
            <td>{{ r.buyer }}</td>
            <td>{{ r.amount }} TZS</td>
            <td>{{ formatDate(r.date) }}</td>
            <td>
              <button class="btn btn-sm btn-success" @click="markPaid(r.id)">✅ Mark as Paid</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const payouts = ref([])

onMounted(async () => {
  const res = await axios.get('/api/payouts/pending')
  payouts.value = res.data
})

function formatDate(date) {
  return new Date(date).toLocaleString()
}

async function markPaid(id) {
  await axios.post(`/api/payouts/pay/${id}`)
  payouts.value = payouts.value.filter(p => p.id !== id)
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
