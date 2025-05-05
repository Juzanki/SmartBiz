<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">📄 Order Details</h2>
      <button class="btn btn-outline-secondary" @click="goBack">
        ⬅️ Back to Orders
      </button>
    </div>

    <!-- Order Details -->
    <div v-if="order" class="card shadow-sm p-4 border-0">
      <div class="row g-4 mb-4">
        <div class="col-md-6">
          <h6 class="text-muted">Customer Name</h6>
          <p class="fw-bold">{{ order.customerName }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Order Status</h6>
          <p>
            <span
              :class="{
                'badge bg-success': order.status === 'Paid',
                'badge bg-warning text-dark': order.status === 'Pending',
                'badge bg-danger': order.status === 'Cancelled'
              }"
            >
              {{ order.status }}
            </span>
          </p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Order Amount</h6>
          <p class="fw-bold text-primary">${{ order.amount }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Order Date</h6>
          <p class="fw-bold">{{ order.orderDate }}</p>
        </div>
      </div>

      <hr>

      <div>
        <h5 class="text-primary fw-bold mb-3">🛒 Ordered Items</h5>

        <div v-if="order.items.length" class="table-responsive">
          <table class="table table-striped align-middle">
            <thead class="table-light">
              <tr>
                <th>Item</th>
                <th>Price (USD)</th>
                <th>Quantity</th>
                <th>Subtotal</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in order.items" :key="index">
                <td>{{ item.name }}</td>
                <td>${{ item.price }}</td>
                <td>{{ item.quantity }}</td>
                <td class="fw-bold">${{ (item.price * item.quantity).toFixed(2) }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div v-else class="text-center text-muted py-4">
          No items in this order.
        </div>
      </div>

      <div class="mt-4 text-end">
        <h4 class="fw-bold">
          Total: <span class="text-primary">${{ calculateTotalAmount(order.items) }}</span>
        </h4>
      </div>
    </div>

    <!-- If Order Not Found -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">Order not found!</h4>
      <p class="text-muted">Please go back and try again.</p>
      <button class="btn btn-primary mt-3" @click="goBack">
        ⬅️ Back to Orders
      </button>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const order = ref(null)

onMounted(() => {
  const id = route.params.id
  const orders = JSON.parse(localStorage.getItem('my_orders')) || []

  const found = orders.find(ord => ord.id == id)

  if (found) {
    // Fake items kwa demo
    found.items = [
      { name: 'Product A', price: 50, quantity: 2 },
      { name: 'Product B', price: 25, quantity: 1 }
    ]
    order.value = found
  } else {
    order.value = null
  }
})

function goBack() {
  router.push('/orders')
}

function calculateTotalAmount(items) {
  return items.reduce((total, item) => total + item.price * item.quantity, 0).toFixed(2)
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
