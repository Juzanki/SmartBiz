<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">🛒 Product Profile</h2>
      <button class="btn btn-outline-secondary" @click="goBack">
        ⬅️ Back to Products
      </button>
    </div>

    <!-- Product Details -->
    <div v-if="product" class="card shadow-sm p-4 border-0">
      <div class="text-center mb-4">
        <img
          :src="product.image || defaultImage"
          alt="Product Image"
          class="rounded mb-3"
          style="width: 200px; height: 200px; object-fit: cover; background-color: #f8f9fa;"
        >
        <h3 class="fw-bold">{{ product.name }}</h3>
        <p class="text-muted">{{ product.category || 'Uncategorized' }}</p>
      </div>

      <hr>

      <div class="row g-4">
        <div class="col-md-6">
          <h6 class="text-muted">Product Name</h6>
          <p class="fw-bold">{{ product.name }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Category</h6>
          <p class="fw-bold">{{ product.category || 'N/A' }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Price</h6>
          <p class="fw-bold text-primary">${{ product.price }}</p>
        </div>
        <div class="col-md-6">
          <h6 class="text-muted">Stock Available</h6>
          <p class="fw-bold">{{ product.stock }} pcs</p>
        </div>
        <div class="col-12">
          <h6 class="text-muted">Short Description</h6>
          <p>{{ product.description || 'No description provided yet.' }}</p>
        </div>
      </div>
    </div>

    <!-- If Product Not Found -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">Product not found!</h4>
      <p class="text-muted">Please go back and try again.</p>
      <button class="btn btn-primary mt-3" @click="goBack">
        ⬅️ Back to Products
      </button>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const product = ref(null)
const defaultImage = '/default-product.png'

onMounted(() => {
  const id = route.params.id
  const products = JSON.parse(localStorage.getItem('my_products')) || []

  const found = products.find(prod => prod.id == id)

  if (found) {
    product.value = found
  } else {
    product.value = null
  }
})

function goBack() {
  router.push('/products')
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
