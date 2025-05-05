<template>
  <div class="container py-5">
    <!-- Top Section -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">👥 Customers</h2>
      <div class="d-flex gap-2">
        <input
          type="text"
          class="form-control"
          placeholder="🔍 Search by name, platform, or tag"
          v-model="searchQuery"
          @input="filterCustomers"
          style="min-width: 250px;"
        />
        <button class="btn btn-outline-secondary" @click="resetFilters">
          Reset
        </button>
      </div>
    </div>

    <!-- Customer List -->
    <div v-if="filteredCustomers.length" class="row g-4">
      <div
        class="col-md-6 col-lg-4"
        v-for="customer in filteredCustomers"
        :key="customer.id"
      >
        <div class="card h-100 shadow-sm border-0 hover-scale" style="cursor: pointer;">
          <div class="card-body text-center">
            <div class="fs-1 mb-3">{{ customer.platformIcon }}</div>
            <h5 class="card-title fw-bold">{{ customer.name }}</h5>
            <p class="text-muted small">{{ customer.platform }} - {{ customer.tag || 'General' }}</p>

            <div class="d-flex justify-content-between small text-muted my-3">
              <div>
                <strong>Last Msg:</strong><br /> {{ customer.lastMessage }}
              </div>
              <div>
                <strong>Orders:</strong><br /> {{ customer.totalOrders }}
              </div>
              <div>
                <strong>Loyalty:</strong><br /> {{ customer.loyaltyPoints }} pts
              </div>
            </div>
          </div>
          <div class="card-footer bg-transparent text-center">
            <button class="btn btn-outline-primary btn-sm w-100" @click="viewCustomer(customer.id)">
              View Details
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">No customers found.</h4>
      <p class="text-muted">Try adjusting your search or filters.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const customers = ref([])
const filteredCustomers = ref([])
const searchQuery = ref('')

onMounted(() => {
  fetchCustomers()
})

function fetchCustomers() {
  // For demo purposes, customers are fetched from localStorage
  // In production, replace this with API call
  const demoCustomers = JSON.parse(localStorage.getItem('my_customers')) || [
    {
      id: 1,
      name: 'John Doe',
      platform: 'WhatsApp',
      platformIcon: '📱',
      lastMessage: 'Need assistance',
      totalOrders: 5,
      loyaltyPoints: 120,
      tag: 'VIP'
    },
    {
      id: 2,
      name: 'Jane Smith',
      platform: 'Telegram',
      platformIcon: '✈️',
      lastMessage: 'Interested in your product',
      totalOrders: 2,
      loyaltyPoints: 40,
      tag: 'New'
    },
    {
      id: 3,
      name: 'Ali Khan',
      platform: 'SMS',
      platformIcon: '📲',
      lastMessage: 'Order delivered',
      totalOrders: 8,
      loyaltyPoints: 200,
      tag: 'Frequent'
    }
  ]

  customers.value = demoCustomers
  filteredCustomers.value = demoCustomers
}

function filterCustomers() {
  const query = searchQuery.value.toLowerCase()
  filteredCustomers.value = customers.value.filter(cust =>
    cust.name.toLowerCase().includes(query) ||
    cust.platform.toLowerCase().includes(query) ||
    (cust.tag && cust.tag.toLowerCase().includes(query))
  )
}

function resetFilters() {
  searchQuery.value = ''
  filteredCustomers.value = customers.value
}

function viewCustomer(id) {
  router.push(`/customer-profile/${id}`)
}
</script>

<style scoped>
.hover-scale:hover {
  transform: scale(1.03);
  transition: 0.3s;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.15);
}
</style>
