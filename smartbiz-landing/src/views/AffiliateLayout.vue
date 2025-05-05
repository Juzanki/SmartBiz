<template>
  <aside class="d-flex flex-column bg-dark text-white p-3" style="width: 240px; min-height: 100vh;">
    <div class="d-flex align-items-center mb-4">
      <img src="/logo-circle.png" alt="Logo" class="me-2" style="width: 40px; height: 40px; border-radius: 50%;">
      <span class="fs-5 fw-bold">Affiliate</span>
    </div>

    <hr class="border-light mb-3">

    <ul class="nav flex-column">
      <li class="nav-item mb-2">
        <router-link to="/affiliate" class="nav-link text-white" active-class="active">
          📊 Dashboard
        </router-link>
      </li>
      <li class="nav-item mb-2">
        <router-link to="/available-campaigns" class="nav-link text-white" active-class="active">
          📦 Available Campaigns
        </router-link>
      </li>
      <li class="nav-item mb-2">
        <router-link to="/my-campaigns" class="nav-link text-white" active-class="active">
          ✅ My Campaigns
        </router-link>
      </li>
      <li class="nav-item mb-2">
        <router-link to="/promoter-leaderboard" class="nav-link text-white" active-class="active">
          🏆 Leaderboard
        </router-link>
      </li>
    </ul>

    <div class="mt-auto small text-center text-muted">
      &copy; {{ new Date().getFullYear() }} SmartBiz
    </div>
  </aside>
</template>

<script setup>
// No special script needed
</script>

<style scoped>
.active {
  background-color: #ffc107;
  color: #212529 !important;
  font-weight: bold;
  border-radius: 0.5rem;
}
</style>
