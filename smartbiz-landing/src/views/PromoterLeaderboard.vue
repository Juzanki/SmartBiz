<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">🏆 Promoter Leaderboard</h2>
      <span class="badge bg-success">Top Earners</span>
    </div>

    <div class="card p-4 shadow-sm border-0">
      <table class="table table-striped">
        <thead>
          <tr>
            <th>Rank</th>
            <th>Username</th>
            <th>Total Earned</th>
            <th>Referrals</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in leaderboard" :key="user.username">
            <td>{{ index + 1 }}</td>
            <td>{{ user.username }}</td>
            <td>{{ user.earned }} TZS</td>
            <td>{{ user.total_referrals }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const leaderboard = ref([])

onMounted(async () => {
  const res = await axios.get('/api/affiliate/leaderboard')
  leaderboard.value = res.data
})
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
