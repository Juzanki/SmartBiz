<template>
  <div class="container py-5">
    <!-- Top Section -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">🛍️ Products & Services</h2>
      <div class="d-flex gap-2">
        <input
          type="text"
          class="form-control"
          placeholder="🔍 Search by name or category"
          v-model="searchQuery"
          @input="filterProducts"
          style="min-width: 250px;"
        />
        <button class="btn btn-outline-success" @click="openAddModal">
          ➕ Add Product
        </button>
      </div>
    </div>

    <!-- Products List -->
    <div v-if="filteredProducts.length" class="row g-4">
      <div
        class="col-md-6 col-lg-4"
        v-for="product in filteredProducts"
        :key="product.id"
      >
        <div class="card h-100 shadow-sm border-0 hover-scale" style="cursor: pointer;">
          <img
            :src="product.image || defaultImage"
            class="card-img-top"
            alt="Product Image"
            style="height: 180px; object-fit: cover;"
          >
          <div class="card-body">
            <h5 class="card-title fw-bold">{{ product.name }}</h5>
            <p class="text-muted small mb-2">{{ product.category || 'Uncategorized' }}</p>
            <div class="d-flex justify-content-between">
              <span class="fw-bold text-primary">${{ product.price }}</span>
              <span class="badge bg-secondary">{{ product.stock }} left</span>
            </div>
          </div>
          <div class="card-footer bg-transparent text-center">
            <button class="btn btn-outline-primary btn-sm w-100" @click.stop="viewProduct(product.id)">
              View Details
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <h4 class="text-danger">No products available.</h4>
      <p class="text-muted">Try adding a new product.</p>
    </div>

    <!-- Add Product Modal -->
    <div class="modal fade" id="addProductModal" tabindex="-1" aria-labelledby="addProductModalLabel" aria-hidden="true" ref="addModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent="submitNewProduct">
            <div class="modal-header">
              <h5 class="modal-title" id="addProductModalLabel">Add New Product</h5>
              <button type="button" class="btn-close" @click="closeAddModal"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Product Name</label>
                <input type="text" class="form-control" v-model="newProduct.name" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Category</label>
                <input type="text" class="form-control" v-model="newProduct.category">
              </div>
              <div class="mb-3">
                <label class="form-label">Price (USD)</label>
                <input type="number" class="form-control" v-model="newProduct.price" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Stock Quantity</label>
                <input type="number" class="form-control" v-model="newProduct.stock" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Image URL</label>
                <input type="url" class="form-control" v-model="newProduct.image">
              </div>
              <div class="mb-3">
                <label class="form-label">Short Description</label>
                <textarea class="form-control" rows="3" v-model="newProduct.description"></textarea>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="closeAddModal">Cancel</button>
              <button type="submit" class="btn btn-primary">Save Product</button>
            </div>
          </form>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const products = ref([])
const filteredProducts = ref([])
const searchQuery = ref('')
const addModal = ref(null)

const defaultImage = '/default-product.png'

const newProduct = ref({
  name: '',
  category: '',
  price: '',
  stock: '',
  image: '',
  description: ''
})

onMounted(() => {
  fetchProducts()
})

function fetchProducts() {
  const demoProducts = JSON.parse(localStorage.getItem('my_products')) || []
  products.value = demoProducts
  filteredProducts.value = demoProducts
}

function filterProducts() {
  const query = searchQuery.value.toLowerCase()
  filteredProducts.value = products.value.filter(prod =>
    prod.name.toLowerCase().includes(query) ||
    (prod.category && prod.category.toLowerCase().includes(query))
  )
}

function resetFilters() {
  searchQuery.value = ''
  filteredProducts.value = products.value
}

function openAddModal() {
  const modal = new bootstrap.Modal(addModal.value)
  modal.show()
}

function closeAddModal() {
  const modal = bootstrap.Modal.getInstance(addModal.value)
  modal.hide()
}

function submitNewProduct() {
  const product = {
    id: Date.now(),
    ...newProduct.value
  }
  products.value.push(product)
  localStorage.setItem('my_products', JSON.stringify(products.value))
  closeAddModal()
  newProduct.value = { name: '', category: '', price: '', stock: '', image: '', description: '' }
  alert('New product added successfully!')
}

function viewProduct(id) {
  router.push(`/product-profile/${id}`)
}
</script>

<style scoped>
.hover-scale:hover {
  transform: scale(1.03);
  transition: 0.3s;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.15);
}
.card {
  border-radius: 1rem;
}
</style>
