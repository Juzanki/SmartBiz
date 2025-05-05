<template>
  <aside class="fixed inset-y-0 left-0 w-64 bg-blue-900 text-white p-4">
    <!-- Logo -->
    <div class="text-2xl font-bold mb-8">SmartBiz</div>

    <!-- Navigation -->
    <nav class="space-y-2">
      <router-link
        v-for="link in navLinks"
        :key="link.name"
        :to="link.path"
        class="flex items-center gap-3 p-3 rounded-lg hover:bg-blue-800 transition-colors"
      >
        <span>{{ link.icon }}</span>
        {{ link.name }}
      </router-link>
    </nav>
  </aside>
</template>

<script setup>
const navLinks = [
  { name: "Dashboard", path: "/dashboard", icon: "🏠" },
  { name: "Autoresponder", path: "/autoresponder", icon: "🤖" },
  { name: "Analytics", path: "/analytics", icon: "📊" },
  { name: "Billing", path: "/billing", icon: "💳" },
  { name: "Settings", path: "/settings", icon: "⚙️" }
];
</script>
