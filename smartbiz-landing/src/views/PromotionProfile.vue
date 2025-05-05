<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">📢 Promotion Details</h2>
      <button class="btn btn-outline-secondary" @click="goBack">
        ⬅️ Back to Scheduled Promotions
      </button>
    </div>

    <!-- Promotion Details -->
    <div v-if="promotion" class="card shadow-sm p-4 border-0">
      <div class="row g-4 mb-4">
        <div class="col-md-6">
          <h6 class="text-muted">Title</h6>
          <p class="fw-bold">{{ promotion.title }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Channel</h6>
          <p class="fw-bold">{{ promotion.channel }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Scheduled Date</h6>
          <p class="fw-bold">{{ promotion.date }} {{ promotion.time }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Status</h6>
          <p>
            <span
              :class="{
                'badge bg-success': promotion.status === 'Scheduled',
                'badge bg-secondary': promotion.status === 'Sent',
                'badge bg-danger': promotion.status === 'Failed'
              }"
            >
              {{ promotion.status }}
            </span>
          </p>
        </div>
      </div>

      <hr>

      <div>
        <h5 class="text-primary fw-bold mb-3">✉️ Message Content</h5>
        <div class="border rounded p-3" style="background-color: #f9f9f9;">
          <p class="mb-0">{{ promotion.message }}</p>
        </div>
      </div>
    </div>

    <!-- If Promotion Not Found -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">Promotion not found!</h4>
      <p class="text-muted">Please go back and try again.</p>
      <button class="btn btn-primary mt-3" @click="goBack">
        ⬅️ Back to Scheduled Promotions
      </button>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const promotion = ref(null)

onMounted(() => {
  const id = route.params.id
  const promotions = JSON.parse(localStorage.getItem('my_promotions')) || []

  const found = promotions.find(promo => promo.id == id)

  if (found) {
    promotion.value = found
  } else {
    promotion.value = null
  }
})

function goBack() {
  router.push('/scheduled-promotions')
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
