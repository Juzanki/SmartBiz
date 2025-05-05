<template>
  <div class="min-h-screen bg-gray-100 p-6">
    <h2 class="text-2xl font-bold text-blue-800 mb-4">📍 Mahali katika Ramani</h2>
    <div id="map" class="w-full h-[500px] rounded-lg shadow-lg border border-gray-300"></div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

const GEOAPIFY_KEY = import.meta.env.VITE_GEOAPIFY_API_KEY

onMounted(() => {
  const map = L.map('map').setView([-6.7924, 39.2083], 13) // Default: Dar es Salaam

  // Tile Layer from Geoapify
  L.tileLayer(`https://maps.geoapify.com/v1/tile/osm-bright/{z}/{x}/{y}.png?apiKey=${GEOAPIFY_KEY}`, {
    attribution: '&copy; <a href="https://www.geoapify.com/">Geoapify</a>',
    maxZoom: 20,
  }).addTo(map)

  // Marker example
  const marker = L.marker([-6.7924, 39.2083]).addTo(map)
  marker.bindPopup('<b>Karibu SmartBiz!</b><br>Mahali hapa ni Dar es Salaam.').openPopup()
})
</script>

<style scoped>
/* Hakikisha Leaflet container haibadiliki size */
#map {
  width: 100%;
  height: 500px;
}
</style>
