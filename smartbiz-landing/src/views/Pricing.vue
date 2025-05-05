<template>
  <DashboardLayout>
    <h2>Choose Your Plan</h2>

    <div class="plans">
      <div class="plan" v-for="plan in plans" :key="plan.name">
        <h3>{{ plan.name }}</h3>
        <p class="price">{{ plan.price }}</p>
        <ul>
          <li v-for="f in plan.features" :key="f">{{ f }}</li>
        </ul>
        <button @click="selectPlan(plan.id)">Select Plan</button>
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
      plans: [
        {
          id: 'free',
          name: 'Free Plan',
          price: 'TZS 0/mo',
          features: ['Basic Chatbot', 'Limited Usage', '1 Social Platform']
        },
        {
          id: 'pro',
          name: 'Pro Plan',
          price: 'TZS 30,000/mo',
          features: ['AI Assistant', 'Scheduling Tools', 'Up to 3 Platforms']
        },
        {
          id: 'business',
          name: 'Business Plan',
          price: 'TZS 65,000/mo',
          features: ['Analytics', 'Auto Promotions', '5+ Platforms', 'CRM']
        },
        {
          id: 'enterprise',
          name: 'Enterprise',
          price: 'TZS 125,000+',
          features: ['Custom Domain', 'Unlimited Access', 'Advanced Reports']
        }
      ]
    }
  },
  methods: {
    async selectPlan(planId) {
      const token = localStorage.getItem('access_token')
      await axios.post('/subscriptions/select', { plan_id: planId }, {
        headers: { Authorization: `Bearer ${token}` }
      })
      alert("Plan selected! You will be redirected to payment.")
      this.$router.push('/checkout')
    }
  }
}
</script>

<style scoped>
.plans {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  margin-top: 1rem;
}
.plan {
  flex: 1 1 250px;
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
  background: #f9f9f9;
}
.price {
  font-size: 1.2rem;
  font-weight: bold;
  margin: 10px 0;
}
button {
  background: #007bff;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
}
</style>
