<template>
  <div class="container-fluid py-4">
    <!-- Page Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="fw-bold text-primary d-flex align-items-center gap-2">
        <i class="bi bi-bar-chart-line-fill"></i> {{ $t("analytics") }}
      </h2>
      <div>
        <select v-model="selectedRange" class="form-select w-auto">
          <option value="today">Today</option>
          <option value="7days">Last 7 Days</option>
          <option value="30days">Last 30 Days</option>
          <option value="custom">Custom Range</option>
        </select>
      </div>
    </div>

    <!-- Stat Cards -->
    <div class="row g-4 mb-4">
      <div class="col-md-4" v-for="stat in stats" :key="stat.title">
        <div class="card shadow-sm rounded-3 border-0">
          <div class="card-body d-flex align-items-center gap-3">
            <div class="bg-primary bg-opacity-10 text-primary rounded-circle p-3 fs-4">
              {{ stat.icon }}
            </div>
            <div>
              <h6 class="mb-0 text-muted text-uppercase small">{{ $t(stat.title) }}</h6>
              <h4 class="fw-bold">{{ stat.value }}</h4>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Analytics Chart -->
    <div class="card shadow-sm border-0 rounded-3">
      <div class="card-body">
        <h5 class="card-title fw-bold text-primary mb-3">
          <i class="bi bi-graph-up-arrow me-2"></i> {{ $t('activity_trend') }}
        </h5>
        <div style="height: 400px">
          <canvas id="activityChart"></canvas>
        </div>
      </div>
    </div>

    <!-- Export Button -->
    <div class="text-end mt-4">
      <button class="btn btn-outline-primary" @click="exportData">
        <i class="bi bi-download me-2"></i> Export Data
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

const selectedRange = ref('7days')

const stats = [
  { title: 'messages_sent', value: '5,320', icon: '✉️' },
  { title: 'active_users', value: '1,287', icon: '👥' },
  { title: 'conversion_rate', value: '7.4%', icon: '⚡' },
]

const renderChart = () => {
  const ctx = document.getElementById('activityChart').getContext('2d')
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [
        {
          label: 'Messages',
          data: [530, 720, 610, 800, 1020, 940, 1100],
          fill: true,
          tension: 0.4,
          backgroundColor: 'rgba(13, 110, 253, 0.1)',
          borderColor: '#0d6efd',
          pointBackgroundColor: '#0d6efd',
          pointRadius: 5
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: true,
          labels: { color: '#6c757d' }
        }
      },
      scales: {
        x: {
          ticks: { color: '#6c757d' },
          grid: { display: false }
        },
        y: {
          ticks: { color: '#6c757d' },
          grid: { color: '#dee2e6' },
          beginAtZero: true
        }
      }
    }
  })
}

const exportData = () => {
  alert('Export initiated! This can later be integrated to download as CSV or PDF.')
}

onMounted(() => {
  renderChart()
})
</script>

<style scoped>
.card {
  background: #fff;
}
</style>
