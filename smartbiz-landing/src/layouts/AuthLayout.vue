<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-tr from-black to-gray-900 px-2 py-8">
    <div
      class="w-full max-w-md bg-[#181829] rounded-2xl shadow-2xl p-8 md:p-10 space-y-8 text-white border-2 border-yellow-400 animate-fade-in"
    >
      <!-- Logo ya duara, na border ya premium -->
      <div class="flex justify-center mb-2">
        <img
          src="@/assets/logo.svg"
          alt="SmartBiz Logo"
          class="h-20 w-20 rounded-full shadow-lg border-4 border-yellow-400 bg-white object-contain"
        />
      </div>

      <!-- Slot: Content goes here -->
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: 'AuthLayout'
}
</script>

<style scoped>
/* Animation ya fade-in (UnoCSS/Tailwind compatible pia) */
.animate-fade-in {
  animation: fadeIn 0.5s cubic-bezier(.4,0,.2,1) both;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(24px) scale(0.97);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* Custom dark bg, works well with dark+UnoCSS, color #181829 ni ya premium */
.bg-[#181829] {
  background-color: #181829 !important;
}

/* Border color premium ya yellow-gold */
.border-yellow-400 {
  border-color: #ffd700 !important;
}
</style>
