<template>
  <div class="min-vh-100 bg-white text-dark dark:bg-dark dark:text-white">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow py-2">
      <div class="container align-items-center">
        <!-- Logo + Brand -->
        <router-link to="/" class="navbar-brand d-flex align-items-center gap-2 fw-bold fs-3">
          <img
            src="@/assets/logo-circle.png"
            alt="SmartBiz Logo"
            class="rounded-circle shadow-sm"
            style="width:38px; height:38px; object-fit:contain; background: #fff; border: 2px solid #FFD700;"
          />
          <span class="d-none d-md-inline" style="letter-spacing: -1px;">SmartBiz</span>
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#mainNavbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-end" id="mainNavbar">
          <ul class="navbar-nav me-4 mb-2 mb-lg-0 gap-2">
            <li class="nav-item">
              <a class="nav-link" href="#features">Features</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#pricing">Pricing</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#contact">Contact</a>
            </li>
          </ul>
          <button @click="toggleTheme" class="btn btn-sm btn-light me-2">
            {{ isDark ? '☀️ Light' : '🌙 Dark' }}
          </button>
          <router-link to="/login" class="btn btn-outline-light me-2 fw-semibold">
            Login
          </router-link>
          <router-link to="/signup" class="btn btn-warning fw-bold text-primary">
            Sign Up
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-primary to-info text-white py-5 text-center">
      <div class="container animate-fade-in">
        <h1 class="display-4 fw-bold mb-3">
          Automate Messaging Across All Platforms
        </h1>
        <p class="lead mb-4">
          Connect WhatsApp, Telegram, SMS, and Email in one powerful dashboard.
        </p>
        <div class="d-flex flex-column flex-md-row justify-content-center gap-3">
          <router-link
            to="/signup"
            class="btn btn-warning btn-lg fw-bold text-primary"
          >
            Get Started Free (1 Month)
          </router-link>
          <button class="btn btn-outline-light btn-lg" @click="scrollToDemo">
            Watch Demo
          </button>
        </div>
      </div>
    </section>

    <!-- Onboarding Animation / Video -->
    <section class="py-5 bg-light dark:bg-dark px-3">
      <div class="container text-center">
        <h2 class="fs-2 fw-bold mb-3">See How It Works</h2>
        <video
          class="w-100 rounded shadow-lg mb-3"
          controls
          src="https://www.w3schools.com/html/mov_bbb.mp4"
        ></video>
        <p class="text-secondary">
          A quick tour on how SmartBiz automates your messaging workflow in real time.
        </p>
      </div>
    </section>

    <!-- Features -->
    <section id="features" class="py-5 bg-white dark:bg-dark">
      <div class="container">
        <h2 class="fs-2 fw-bold text-center mb-5 text-primary dark:text-warning">Platform Features</h2>
        <div class="row g-4">
          <div
            v-for="feature in features"
            :key="feature.id"
            class="col-12 col-md-6 col-lg-4"
          >
            <div class="card h-100 border-0 shadow-lg hover-shadow-sm transition">
              <div class="card-body text-center">
                <div class="fs-1 mb-3 text-warning">{{ feature.icon }}</div>
                <h5 class="card-title fw-bold mb-2">{{ feature.title }}</h5>
                <p class="card-text">{{ feature.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials Carousel -->
    <section class="py-5 bg-light dark:bg-secondary text-center px-3">
      <div class="container">
        <h2 class="fs-2 fw-bold mb-4 text-primary dark:text-warning">What Our Users Say</h2>
        <div class="card border-0 shadow-lg mx-auto" style="max-width: 500px;">
          <div class="card-body">
            <p class="fs-5 fst-italic mb-2">“SmartBiz helped me automate WhatsApp replies while I sleep. I’ve tripled my customer response rate!”</p>
            <p class="fw-bold mb-0">— Asha, Business Owner</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Slot for footer/pricing -->
    <slot />
  </div>
</template>

<script>
export default {
  name: "LandingPageView",
  data() {
    return {
      features: [
        { id: 1, icon: "📱", title: "WhatsApp Automation", desc: "Auto-reply and broadcast to clients on WhatsApp." },
        { id: 2, icon: "🤖", title: "Telegram Bots", desc: "Engage users with customizable Telegram bots." },
        { id: 3, icon: "✉️", title: "SMS Campaigns", desc: "Send bulk promotions and OTPs via SMS." },
        { id: 4, icon: "📧", title: "Email Sequences", desc: "Automate marketing emails with rich templates." },
        { id: 5, icon: "📊", title: "Unified Analytics", desc: "Get insights across all messaging channels." },
        { id: 6, icon: "🔌", title: "API & Webhooks", desc: "Easily connect with your CRM or ERP." }
      ],
      isDark: false
    }
  },
  mounted() {
    this.isDark = document.documentElement.classList.contains("dark")
  },
  methods: {
    toggleTheme() {
      this.isDark = !this.isDark
      document.documentElement.classList.toggle("dark", this.isDark)
    },
    scrollToDemo() {
      const videoSection = document.querySelector("video");
      if (videoSection) videoSection.scrollIntoView({ behavior: "smooth" });
    }
  }
}
</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 1s ease-in-out;
}
@keyframes fadeIn {
  0% { opacity: 0; transform: translateY(10px);}
  100% { opacity: 1; transform: translateY(0);}
}
.bg-primary { background-color: #1E40AF !important; }
.bg-info { background-color: #0B89B1 !important; }
.text-primary { color: #1E40AF !important; }
.text-warning { color: #FF9E0B !important; }
.hover-shadow-sm:hover { box-shadow: 0 0.5rem 1rem rgba(30, 64, 175, 0.15) !important; }
.transition { transition: box-shadow .2s; }
.dark .bg-dark { background: #0b1120 !important; }
.dark .text-warning { color: #FFD600 !important; }
</style>
