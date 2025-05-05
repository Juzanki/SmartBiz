<template>
  <div class="product-form">
    <h3>{{ editing ? 'Edit Product' : 'Add New Product or Service' }}</h3>

    <form @submit.prevent="handleSubmit">
      <input v-model="form.name" type="text" placeholder="Name" required />
      <textarea v-model="form.description" placeholder="Description"></textarea>
      <input v-model.number="form.price" type="number" placeholder="Price" required />
      <input v-model.number="form.stock" type="number" placeholder="Stock" />
      
      <label>
        <input type="checkbox" v-model="form.is_service" />
        This is a service
      </label>

      <input v-model="form.category" type="text" placeholder="Category" />

      <button type="submit">{{ editing ? 'Update' : 'Save' }}</button>
      <button type="button" @click="close">Cancel</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  emits: ['close', 'refresh'],
  data() {
    return {
      editing: false,
      form: {
        id: null,
        name: '',
        description: '',
        price: 0,
        stock: 0,
        is_service: false,
        category: ''
      }
    }
  },
  methods: {
    loadProduct(product) {
      this.form = { ...product }
      this.editing = true
    },
    async handleSubmit() {
      const headers = { Authorization: 'Bearer ' + localStorage.getItem('access_token') }

      if (this.editing) {
        await axios.put(`/products/${this.form.id}`, this.form, { headers })
      } else {
        await axios.post('/products', this.form, { headers })
      }

      this.$emit('refresh')
      this.close()
    },
    close() {
      this.editing = false
      this.form = { id: null, name: '', description: '', price: 0, stock: 0, is_service: false, category: '' }
      this.$emit('close')
    }
  }
}
</script>

<style scoped>
.product-form {
  background: var(--bg-color);
  padding: 1rem;
  border: 1px solid #ccc;
  margin: 1rem 0;
  border-radius: 8px;
}
.product-form form {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
.product-form input,
.product-form textarea {
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
}
</style>
