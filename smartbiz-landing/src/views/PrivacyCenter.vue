<template>
  <DashboardLayout>
    <h2>Privacy Center</h2>

    <p>Download or delete your data.</p>

    <button @click="downloadData">Download My Data</button>
    <button @click="requestDeletion" class="danger">Delete My Account</button>
  </DashboardLayout>
</template>

<script>
import axios from 'axios'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

export default {
  components: { DashboardLayout },
  methods: {
    async downloadData() {
      const token = localStorage.getItem('access_token')
      const res = await axios.get('/privacy/data', {
        headers: { Authorization: `Bearer ${token}` },
        responseType: 'blob'
      })
      const url = window.URL.createObjectURL(new Blob([res.data]))
      const link = document.createElement('a')
      link.href = url
      link.download = 'my_data.zip'
      link.click()
    },
    async requestDeletion() {
      if (confirm("Are you sure you want to permanently delete your account?")) {
        const token = localStorage.getItem('access_token')
        await axios.post('/privacy/delete', {}, {
          headers: { Authorization: `Bearer ${token}` }
        })
        localStorage.clear()
        this.$router.push('/signup')
      }
    }
  }
}
</script>

<style scoped>
.danger {
  background: #e74c3c;
  color: white;
  margin-top: 1rem;
}
</style>
