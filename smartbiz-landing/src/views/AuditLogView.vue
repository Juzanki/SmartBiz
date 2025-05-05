<template>
  <div class="container py-5">
    <!-- Page Header -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">📜 Audit Log History</h2>
    </div>

    <!-- Audit Table -->
    <div class="card p-4 shadow-sm border-0">
      <table class="table table-striped">
        <thead class="table-light">
          <tr>
            <th>#</th>
            <th>User ID</th>
            <th>Action</th>
            <th>Target</th>
            <th>Timestamp</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="log in logs" :key="log.id">
            <td>{{ log.id }}</td>
            <td>{{ log.user_id }}</td>
            <td>{{ log.action }}</td>
            <td>{{ log.target }}</td>
            <td>{{ formatDate(log.timestamp) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const logs = ref([])

onMounted(async () => {
  const res = await axios.get('/api/admin/audit')
  logs.value = res.data
})

function formatDate(ts) {
  return new Date(ts).toLocaleString()
}
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
