<template>
  <div class="container py-5">
    <!-- Top Section -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">👤 Customer Profile</h2>
      <button class="btn btn-outline-secondary" @click="goBack">
        ⬅️ Back to Customers
      </button>
    </div>

    <!-- Customer Details -->
    <div v-if="customer" class="card shadow-sm p-4 border-0">
      <div class="text-center mb-4">
        <div class="fs-1 mb-2">{{ customer.platformIcon }}</div>
        <h3 class="fw-bold">{{ customer.name }}</h3>
        <p class="text-muted small">{{ customer.platform }} - {{ customer.tag || 'General' }}</p>
      </div>

      <hr>

      <div class="row g-4">
        <div class="col-md-6">
          <h6 class="text-muted">Name</h6>
          <p class="fw-bold">{{ customer.name }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Platform</h6>
          <p class="fw-bold">{{ customer.platform }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Tag</h6>
          <p class="fw-bold">{{ customer.tag || 'None' }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Total Orders</h6>
          <p class="fw-bold">{{ customer.totalOrders }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Loyalty Points</h6>
          <p class="fw-bold">{{ customer.loyaltyPoints }} pts</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Last Message</h6>
          <p>{{ customer.lastMessage }}</p>
        </div>
      </div>

      <div class="mt-4">
        <h5 class="text-primary fw-bold mb-3">📜 Interaction History</h5>

        <div v-if="customer.history.length" class="list-group">
          <div 
            v-for="(interaction, index) in customer.history" 
            :key="index" 
            class="list-group-item list-group-item-action"
          >
            <div class="d-flex justify-content-between">
              <div>
                <strong>{{ interaction.message }}</strong>
                <div class="text-muted small">{{ interaction.date }}</div>
              </div>
              <div class="badge bg-primary">{{ interaction.platform }}</div>
            </div>
          </div>
        </div>

        <div v-else class="text-center text-muted py-4">
          No interaction history available.
        </div>
      </div>
    </div>

    <!-- If Customer Not Found -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">Customer not found!</h4>
      <p class="text-muted">Please go back and try again.</p>
      <button class="btn btn-primary mt-3" @click="goBack">
        ⬅️ Back to Customers
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const customer = ref(null)

onMounted(() => {
  const id = route.params.id
  const customers = JSON.parse(localStorage.getItem('my_customers')) || []

  const found = customers.find(cust => cust.id == id)

  if (found) {
    // Fake interaction history kwa demo
    found.history = [
      { message: 'Asked about product', date: '2025-04-20', platform: found.platform },
      { message: 'Placed an order', date: '2025-04-22', platform: found.platform },
      { message: 'Requested support', date: '2025-04-25', platform: found.platform }
    ]
    customer.value = found
  } else {
    customer.value = null
  }
})

function goBack() {
  router.push('/customers')
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
