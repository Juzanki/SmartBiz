<template>
  <div class="unauthorized">
    <h1>403 - Unauthorized</h1>
    <router-link to="/login">Login Again</router-link>
  </div>
</template>

<script setup>
</script>

<style scoped>
.unauthorized {
  text-align: center;
  margin-top: 100px;
}
</style>
