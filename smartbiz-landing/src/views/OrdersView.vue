<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">🧾 Orders</h2>
      <div class="d-flex gap-2">
        <input
          type="text"
          class="form-control"
          placeholder="🔍 Search by customer or status"
          v-model="searchQuery"
          @input="filterOrders"
          style="min-width: 250px;"
        />
        <button class="btn btn-outline-secondary" @click="resetFilters">
          Reset
        </button>
      </div>
    </div>

    <!-- Orders List -->
    <div v-if="filteredOrders.length" class="table-responsive">
      <table class="table table-hover align-middle">
        <thead class="table-light">
          <tr>
            <th>Customer</th>
            <th>Amount (USD)</th>
            <th>Status</th>
            <th>Order Date</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in filteredOrders" :key="order.id">
            <td>{{ order.customerName }}</td>
            <td class="fw-bold text-primary">${{ order.amount }}</td>
            <td>
              <span
                :class="{
                  'badge bg-success': order.status === 'Paid',
                  'badge bg-warning text-dark': order.status === 'Pending',
                  'badge bg-danger': order.status === 'Cancelled'
                }"
              >
                {{ order.status }}
              </span>
            </td>
            <td class="text-muted">{{ order.orderDate }}</td>
            <td>
              <button class="btn btn-outline-primary btn-sm" @click="viewOrder(order.id)">
                View Details
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">No orders found.</h4>
      <p class="text-muted">Try adjusting your search filters.</p>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const orders = ref([])
const filteredOrders = ref([])
const searchQuery = ref('')

onMounted(() => {
  fetchOrders()
})

function fetchOrders() {
  const demoOrders = JSON.parse(localStorage.getItem('my_orders')) || [
    {
      id: 1,
      customerName: 'John Doe',
      amount: 150,
      status: 'Paid',
      orderDate: '2025-04-20'
    },
    {
      id: 2,
      customerName: 'Jane Smith',
      amount: 80,
      status: 'Pending',
      orderDate: '2025-04-22'
    },
    {
      id: 3,
      customerName: 'Ali Khan',
      amount: 220,
      status: 'Cancelled',
      orderDate: '2025-04-24'
    }
  ]

  orders.value = demoOrders
  filteredOrders.value = demoOrders
}

function filterOrders() {
  const query = searchQuery.value.toLowerCase()
  filteredOrders.value = orders.value.filter(order =>
    order.customerName.toLowerCase().includes(query) ||
    order.status.toLowerCase().includes(query)
  )
}

function resetFilters() {
  searchQuery.value = ''
  filteredOrders.value = orders.value
}

function viewOrder(id) {
  router.push(`/order-profile/${id}`)
}
</script>

<style scoped>
.table-hover tbody tr:hover {
  background-color: #f8f9fa;
}
</style>
