<template>
  <DashboardLayout>
    <h2>Live Drone Monitor</h2>

    <div v-if="missions.length">
      <table class="drone-table">
        <thead>
          <tr>
            <th>Drone ID</th>
            <th>Product</th>
            <th>Location</th>
            <th>Status</th>
            <th>ETA</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="mission in missions" :key="mission.id">
            <td>{{ mission.drone_id }}</td>
            <td>{{ mission.product_name }}</td>
            <td>{{ mission.destination }}</td>
            <td><span :class="mission.status">{{ mission.status }}</span></td>
            <td>{{ mission.eta }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p v-else>No drones in flight at the moment.</p>
  </DashboardLayout>
</template>

<script>
import axios from 'axios'
import DashboardLayout from '@/layouts/DashboardLayout.vue'

export default {
  components: { DashboardLayout },
  data() {
    return {
      missions: []
    }
  },
  async mounted() {
    await this.fetchMissions()
    // Optional: refresh every 30s
    setInterval(this.fetchMissions, 30000)
  },
  methods: {
    async fetchMissions() {
      const token = localStorage.getItem('access_token')
      const res = await axios.get('/drones/missions', {
        headers: { Authorization: `Bearer ${token}` }
      })
      this.missions = res.data
    }
  }
}
</script>

<style scoped>
.drone-table {
  width: 100%;
  border-collapse: collapse;
}
.drone-table th, .drone-table td {
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
.in-transit { color: orange; }
.delivered { color: green; }
.failed { color: red; }
</style>
