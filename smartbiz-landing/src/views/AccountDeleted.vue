<template>
  <div class="min-vh-100 d-flex flex-column justify-content-center align-items-center bg-dark text-center text-light px-4">
    <div class="p-4 rounded-4 shadow-lg border border-danger" style="background:#1e1e2f; max-width: 460px;">
      <img src="@/assets/logo-circle.png" alt="SmartBiz Logo" class="mb-3 rounded-circle border border-warning" style="width:60px;height:60px;background:white;" />
      <h2 class="text-danger fw-bold mb-3">Account Deleted</h2>
      <p class="text-secondary small mb-4">
        Your account has been permanently removed from SmartBiz Assistance.<br>
        We're sorry to see you go.
      </p>
      <p class="text-light small mb-4">
        If this was a mistake or you’d like to return, feel free to <router-link to="/signup" class="text-warning fw-bold">create a new account</router-link> anytime.
      </p>
      <router-link to="/" class="btn btn-warning fw-bold rounded-pill px-4 py-2 shadow-sm">
        Return to Home
      </router-link>
    </div>
  </div>
</template>

<script setup>
// No complex logic needed here.
</script>

<style scoped>
.bg-dark {
  background-color: #181829 !important;
}
</style>
