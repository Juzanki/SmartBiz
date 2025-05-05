<template>
  <div class="container py-5">
    <!-- Top Section -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">🏢 Business Profile</h2>
      <button class="btn btn-outline-secondary" @click="goBack">
        ⬅️ Back
      </button>
    </div>

    <div v-if="business" class="card shadow-sm border-0 p-4">
      <div class="text-center mb-4">
        <img 
          :src="business.logo || defaultLogo" 
          alt="Business Logo" 
          class="rounded-circle mb-3"
          style="width: 120px; height: 120px; object-fit: cover; background-color: #f8f9fa;"
        >
        <h3 class="fw-bold">{{ business.name }}</h3>
        <p class="text-muted">{{ business.type }}</p>
        <a :href="business.website" target="_blank" class="small text-decoration-none">
          🌐 Visit Website
        </a>
      </div>

      <hr>

      <div class="row g-3">
        <div class="col-md-6">
          <h6 class="text-muted">Business Name</h6>
          <p class="fw-bold">{{ business.name }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Business Type</h6>
          <p class="fw-bold">{{ business.type }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Website</h6>
          <p>
            <a :href="business.website" target="_blank" class="text-primary small">
              {{ business.website }}
            </a>
          </p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Established</h6>
          <p class="fw-bold">{{ business.createdAt || 'N/A' }}</p>
        </div>
        <div class="col-12">
          <h6 class="text-muted">Business Description</h6>
          <p>{{ business.description || 'No description provided yet.' }}</p>
        </div>
      </div>
    </div>

    <!-- If Business Not Found -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">Business not found!</h4>
      <p class="text-muted">Maybe the link is broken or the business was deleted.</p>
      <button class="btn btn-primary mt-3" @click="goBack">
        ⬅️ Return to Dashboard
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const business = ref(null)
const defaultLogo = '/default-logo.png'

onMounted(() => {
  const id = route.params.id
  const businesses = JSON.parse(localStorage.getItem('my_businesses')) || []

  const found = businesses.find(biz => biz.id == id)

  if (found) {
    business.value = found
  } else {
    business.value = null
  }
})

// Go Back function
function goBack() {
  router.push('/dashboard/user')
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
