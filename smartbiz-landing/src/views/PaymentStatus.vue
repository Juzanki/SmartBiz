<template>
  <DashboardLayout>
    <div class="status-card">
      <h2>Payment Status</h2>

      <div v-if="status === 'success'" class="success">
        <p>✅ Payment Successful!</p>
        <p>You are now subscribed to: <strong>{{ planName }}</strong></p>
        <router-link to="/dashboard">Go to Dashboard</router-link>
      </div>

      <div v-else-if="status === 'failed'" class="failed">
        <p>❌ Payment Failed.</p>
        <p>Please try again or use another payment method.</p>
        <router-link to="/checkout">Retry Payment</router-link>
      </div>

      <div v-else>
        <p>Loading status...</p>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import axios from 'axios'

export default {
  components: { DashboardLayout },
  data() {
    return {
      status: '',
      planName: ''
    }
  },
  async mounted() {
    const token = localStorage.getItem('access_token')
    const res = await axios.get('/payments/status', {
      headers: { Authorization: `Bearer ${token}` }
    })

    this.status = res.data.status
    this.planName = res.data.plan_name
  }
}
</script>

<style scoped>
.status-card {
  max-width: 500px;
  margin: auto;
  padding: 2rem;
  background: #f9f9f9;
  border-radius: 10px;
  text-align: center;
}
.success {
  color: green;
}
.failed {
  color: red;
}
</style>
