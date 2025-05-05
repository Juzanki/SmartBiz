// ================= Core Vue App Bootstrap =================
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// ================= Bootstrap CSS & JS ====================
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

// ================= Main Global Styles ====================
import './assets/main.css'

// =================== Multilingual (vue-i18n) ==============
import { createI18n } from 'vue-i18n'
import en from './locales/en.json'
import sw from './locales/sw.json'
import fr from './locales/fr.json'
// If you want to add more languages, add them here:
// import tr from './locales/tr.json'

const savedLang = localStorage.getItem('user_lang') || 'en'
const i18n = createI18n({
  legacy: false,
  locale: savedLang,
  fallbackLocale: 'en',
  messages: { en, sw, fr /* , tr */ },
})

// =================== Toast Notifications ==================
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'

// =============== Create & Configure App ===================
const app = createApp(App)

// ========== Attach Plugins: Router, i18n, Toast ===========
app.use(router)
app.use(i18n)
app.use(Toast, {
  // Customize toast options if needed
  position: 'top-right',
  timeout: 3500,
  closeOnClick: true,
  pauseOnHover: true,
  draggable: true,
})

// =============== Optional: Axios Global Config ============
// import axios from 'axios'
// axios.defaults.baseURL = 'http://localhost:8000'

// =============== Mount The App ============================
app.mount('#app')
