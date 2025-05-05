<template>
  <DashboardLayout>
    <h2>Confirm Your Subscription</h2>

    <div class="checkout-card" v-if="plan">
      <h3>{{ plan.name }}</h3>
      <p class="price">{{ plan.price }}</p>
      <ul>
        <li v-for="f in plan.features" :key="f">{{ f }}</li>
      </ul>

      <label>Select Payment Method:</label>
      <select v-model="method">
        <option value="mpesa">M-PESA</option>
        <option value="paypal">PayPal</option>
        <option value="card">Credit/Debit Card</option>
      </select>

      <button @click="confirmPayment">Confirm & Pay</button>
    </div>

    <p v-else>Loading...</p>
  </DashboardLayout>
</template>

<script>
import axios from 'axios'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

export default {
  components: { DashboardLayout },
  data() {
    return {
      plan: null,
      method: 'mpesa'
    }
  },
  methods: {
    async fetchPlan() {
      const token = localStorage.getItem('access_token')
      const res = await axios.get('/subscriptions/selected', {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.plan = res.data
    },
    async confirmPayment() {
      const token = localStorage.getItem('access_token')
      const res = await axios.post('/payments/initiate', {
        plan_id: this.plan.id,
        method: this.method
      }, {
        headers: { Authorization: `Bearer ${token}` }
      })

      alert("Payment initiated! Follow instructions on your phone or PayPal.")
      this.$router.push('/dashboard')
    }
  },
  mounted() {
    this.fetchPlan()
  }
}
</script>

<style scoped>
.checkout-card {
  max-width: 500px;
  background: #f1f1f1;
  padding: 1.5rem;
  border-radius: 8px;
  margin: auto;
}
.price {
  font-size: 1.2rem;
  font-weight: bold;
}
</style>
