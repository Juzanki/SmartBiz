<template>
  <DashboardLayout>
    <h2>Smart Atmospheric Deployment</h2>

    <div class="deploy-form">
      <label>Enter City/Location:</label>
      <input v-model="city" placeholder="Mfano: Dodoma" />
      <button @click="fetchSuggestions">Get Suggested Products</button>
    </div>

    <div v-if="products.length">
      <h3>Suggested Products for {{ city }}</h3>
      <div v-for="product in products" :key="product.id" class="product-card">
        <h4>{{ product.name }}</h4>
        <p>{{ product.description }}</p>
        <p><strong>TZS {{ product.price }}</strong></p>
        <p>Weather: {{ product.weather_type }} | Time: {{ product.preferred_time_start }} - {{ product.preferred_time_end }}</p>
        <button @click="dispatchDrone(product.id)">Deploy Now</button>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import axios from 'axios'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

export default {
  components: { DashboardLayout },
  data() {
    return {
      city: '',
      products: []
    }
  },
  methods: {
    async fetchSuggestions() {
      const token = localStorage.getItem('access_token')
      const res = await axios.get(`/deploy/now?city=${this.city}`, {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.products = res.data
    },
    async dispatchDrone(productId) {
      const token = localStorage.getItem('access_token')
      await axios.post(`/drone/dispatch/${productId}`, {}, {
        headers: { Authorization: `Bearer ${token}` }
      })
      alert("Drone dispatched successfully!")
    }
  }
}
</script>

<style scoped>
.deploy-form {
  margin-bottom: 1rem;
}
.product-card {
  background: #f1f1f1;
  padding: 1rem;
  border-radius: 8px;
  margin-bottom: 1rem;
}
button {
  background: #007bff;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 6px;
}
</style>
