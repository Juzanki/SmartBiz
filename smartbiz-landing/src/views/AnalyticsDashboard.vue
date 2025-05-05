<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">📊 Analytics Dashboard</h2>
      <small class="text-muted">{{ new Date().toDateString() }}</small>
    </div>

    <!-- Summary Cards -->
    <div class="row g-4 mb-5">
      <div class="col-md-3" v-for="card in summaryCards" :key="card.title">
        <div class="card shadow-sm border-0 p-4 text-center">
          <div class="fs-1">{{ card.icon }}</div>
          <h6 class="fw-bold mt-2">{{ card.title }}</h6>
          <p class="fs-4 text-primary mb-0">{{ card.value }}</p>
        </div>
      </div>
    </div>

    <!-- Section Title -->
    <h5 class="text-dark fw-bold mb-3">📈 Channel & Order Trends</h5>

    <!-- Charts: Channels, Orders, Growth -->
    <div class="row g-4 mb-5">
      <div class="col-md-4">
        <div class="card shadow-sm border-0 p-4">
          <h6 class="fw-bold text-primary mb-3">Messages Per Channel</h6>
          <apexchart width="100%" type="donut" :options="messageChartOptions" :series="messageChartSeries" />
        </div>
      </div>

      <div class="col-md-4">
        <div class="card shadow-sm border-0 p-4">
          <h6 class="fw-bold text-primary mb-3">Orders Over Time</h6>
          <apexchart width="100%" type="line" :options="orderChartOptions" :series="orderChartSeries" />
        </div>
      </div>

      <div class="col-md-4">
        <div class="card shadow-sm border-0 p-4">
          <h6 class="fw-bold text-primary mb-3">Weekly Growth</h6>
          <apexchart width="100%" type="area" :options="growthChartOptions" :series="growthChartSeries" />
        </div>
      </div>
    </div>

    <!-- Section Title -->
    <h5 class="text-dark fw-bold mb-3">📊 Feedback & Conversion Analysis</h5>

    <!-- Feedback + Conversion -->
    <div class="row g-4 mb-5">
      <div class="col-md-6">
        <div class="card shadow-sm border-0 p-4">
          <h6 class="fw-bold text-primary mb-3">Customer Feedback</h6>
          <apexchart width="100%" type="bar" :options="feedbackChartOptions" :series="feedbackChartSeries" />
        </div>
      </div>

      <div class="col-md-6">
        <div class="card shadow-sm border-0 p-4">
          <h6 class="fw-bold text-primary mb-3">Conversion Rate</h6>
          <apexchart width="100%" type="donut" :options="conversionChartOptions" :series="conversionChartSeries" />
        </div>
      </div>
    </div>

    <!-- Section Title -->
    <h5 class="text-dark fw-bold mb-3">📉 Sales & Messaging Trend</h5>

    <div class="row g-4">
      <div class="col-12">
        <div class="card shadow-sm border-0 p-4">
          <apexchart width="100%" type="line" :options="salesTrendOptions" :series="salesTrendSeries" />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ApexCharts from 'vue3-apexcharts'
defineExpose({ components: { apexchart: ApexCharts } })

const summaryCards = ref([
  { title: 'Total Customers', value: 120, icon: '👥' },
  { title: 'Messages Sent', value: 854, icon: '✉️' },
  { title: 'Orders Made', value: 223, icon: '🛒' },
  { title: 'Active Subscriptions', value: 75, icon: '🔄' }
])

const messageChartSeries = ref([400, 250, 150, 54])
const messageChartOptions = ref({
  labels: ['WhatsApp', 'Telegram', 'SMS', 'Email'],
  legend: { position: 'bottom' },
  colors: ['#00E396', '#775DD0', '#FEB019', '#FF4560']
})

const orderChartSeries = ref([
  { name: 'Orders', data: [10, 25, 15, 30, 20, 50, 60] }
])
const orderChartOptions = ref({
  chart: { toolbar: { show: false } },
  xaxis: { categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] },
  colors: ['#008FFB'],
  stroke: { curve: 'smooth' }
})

const growthChartSeries = ref([{ name: 'Growth', data: [5, 10, 8, 12, 15, 20, 25] }])
const growthChartOptions = ref({
  chart: { toolbar: { show: false } },
  xaxis: { categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] },
  colors: ['#00BFFF'],
  stroke: { curve: 'smooth' },
  fill: {
    type: 'gradient',
    gradient: { shadeIntensity: 1, opacityFrom: 0.4, opacityTo: 0.1 }
  }
})

// Feedback
const feedbackChartSeries = ref([{ name: 'Ratings', data: [80, 40, 20] }])
const feedbackChartOptions = ref({
  chart: { toolbar: { show: false } },
  xaxis: { categories: ['Positive', 'Neutral', 'Negative'] },
  colors: ['#00C851', '#FFBB33', '#ff4444']
})

// Conversion
const conversionChartSeries = ref([65, 35])
const conversionChartOptions = ref({
  labels: ['Converted', 'Unconverted'],
  colors: ['#28a745', '#d9534f'],
  legend: { position: 'bottom' }
})

// Sales + Messaging Trend
const salesTrendSeries = ref([
  {
    name: 'Sales',
    type: 'column',
    data: [20, 40, 35, 60, 50, 70, 90]
  },
  {
    name: 'Messages',
    type: 'line',
    data: [200, 180, 220, 240, 260, 280, 300]
  }
])
const salesTrendOptions = ref({
  chart: { toolbar: { show: false } },
  xaxis: { categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] },
  stroke: { curve: 'smooth' },
  colors: ['#17a2b8', '#6f42c1']
})
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
</style>
