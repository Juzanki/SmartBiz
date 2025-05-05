<template>
  <DashboardLayout>
    <div class="product-header">
      <h2>My Products & Services</h2>
      <button @click="showForm = true">➕ Add New</button>
    </div>

    <ProductForm v-if="showForm" @close="showForm = false" @refresh="fetchProducts" />

    <div v-if="products.length === 0">No products yet.</div>

    <div v-else class="product-list">
      <div v-for="p in products" :key="p.id" class="product-card">
        <h3>{{ p.name }}</h3>
        <p>{{ p.description }}</p>
        <p><strong>Price:</strong> {{ p.price }}</p>
        <p><strong>Stock:</strong> {{ p.stock }}</p>
        <p><strong>Type:</strong> {{ p.is_service ? 'Service' : 'Product' }}</p>
        <button @click="editProduct(p)">Edit</button>
        <button @click="deleteProduct(p.id)">Delete</button>
      </div>
    </div>
  </DashboardLayout>
</template>

<script>
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import ProductForm from '@/components/ProductForm.vue'
import axios from 'axios'

export default {
  components: { DashboardLayout, ProductForm },
  data() {
    return {
      products: [],
      showForm: false
    }
  },
  methods: {
    async fetchProducts() {
      const res = await axios.get('/products', this.auth())
      this.products = res.data
    },
    async deleteProduct(id) {
      if (confirm('Delete this product?')) {
        await axios.delete(`/products/${id}`, this.auth())
        this.fetchProducts()
      }
    },
    editProduct(product) {
      this.$refs.formRef.loadProduct(product)
      this.showForm = true
    },
    auth() {
      return { headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') } }
    }
  },
  mounted() {
    this.fetchProducts()
  }
}
</script>

<style scoped>
.product-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
.product-card {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
}
</style>
