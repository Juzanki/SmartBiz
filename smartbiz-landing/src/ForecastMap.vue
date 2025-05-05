<template>
  <DashboardLayout>
    <h2>AI Forecast Map</h2>
    <div id="map" style="height: 600px;"></div>
  </DashboardLayout>
</template>

<script>
import L from 'leaflet'
import DashboardLayout from '@/layouts/DashboardLayout.vue'
import axios from 'axios'

export default {
  components: { DashboardLayout },
  data() {
    return {
      map: null
    }
  },
  async mounted() {
    this.map = L.map('map').setView([-6.8, 39.28], 7) // TZ default

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: 'SAM AI Map'
    }).addTo(this.map)

    const res = await axios.get('/forecast/zones')
    res.data.forEach(zone => {
      const marker = L.circle([zone.lat, zone.lng], {
        radius: 10000,
        color: zone.weather === 'sunny' ? 'orange' : 'blue'
      }).addTo(this.map)

      marker.bindPopup(`
        <strong>${zone.city}</strong><br/>
        Weather: ${zone.weather}<br/>
        Recommended: ${zone.recommendation}
      `)
    })
  }
}
</script>
