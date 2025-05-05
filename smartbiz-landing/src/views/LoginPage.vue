 <template>
  <div class="min-vh-100 d-flex align-items-center justify-content-center bg-dark">
    <div
      class="card shadow-lg p-4 rounded-4 border-2 border-warning"
      style="background:#181829; max-width:350px; width:100%;"
    >
      <!-- LOGO Centered -->
      <div class="d-flex flex-column align-items-center mb-4 mt-2">
        <img
          src="@/assets/logo-circle.png"
          alt="SmartBiz Logo"
          class="rounded-circle border border-warning mb-3 shadow"
          style="width:64px;height:64px;object-fit:contain;background:#fff;"
        />
        <h2 class="fw-bold text-warning text-center mb-0" style="font-size:1.55rem;">Login to SmartBiz</h2>
      </div>

```
  <hr class="mb-4 border-warning opacity-75"/>

  <form @submit.prevent="handleLogin" autocomplete="off">
    <div class="mb-3 input-group bg-[#232338] rounded-3 overflow-hidden">
      <span class="input-group-text bg-transparent border-0 text-warning"><i class="bi bi-person-fill"></i></span>
      <input
        v-model="form.identifier"
        type="text"
        class="form-control bg-transparent border-0 text-white"
        placeholder="Enter Username, Email, or Phone"
        autocomplete="username"
        required
        style="font-size:1rem;"
      />
    </div>
    <div class="mb-3 input-group bg-[#232338] rounded-3 overflow-hidden">
      <span class="input-group-text bg-transparent border-0 text-warning"><i class="bi bi-lock-fill"></i></span>
      <input
        v-model="form.password"
        type="password"
        class="form-control bg-transparent border-0 text-white"
        placeholder="Enter Password"
        autocomplete="current-password"
        required
        style="font-size:1rem;"
      />
    </div>
    <button
      type="submit"
      class="btn btn-warning w-100 fw-bold mb-2 py-2 rounded-3"
      :disabled="loading"
    >
      <span v-if="!loading">Login</span>
      <span v-else>
        <i class="bi bi-arrow-repeat spinner-border spinner-border-sm"></i>
        Logging in...
      </span>
    </button>
  </form>

  <!-- Signup & Forgot Links -->
  <div class="d-flex flex-column align-items-center gap-1 mt-2 text-sm">
    <div>
      <span class="text-light">Don't have an account?</span>
      <router-link to="/signup" class="text-warning fw-bold ms-1">Signup</router-link>
    </div>
    <router-link to="/forgot-password" class="text-info">Forgot Password?</router-link>
  </div>
</div>
```

  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useToast } from 'vue-toastification'
import { useRouter } from 'vue-router'

const toast = useToast()
const router = useRouter()
const loading = ref(false)

const form = ref({
  identifier: '',
  password: ''
})

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const handleLogin = async () => {
  loading.value = true
  try {
    const params = new URLSearchParams()
    params.append('username', form.value.identifier)
    params.append('password', form.value.password)

    const res = await axios.post(`${API_BASE}/auth/login`, params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })

const accessToken = res.data.access_token;
const userRole = res.data.role || 'user';    // Hakikisha backend irudishe role
const userName = res.data.name || '';
const userLang = res.data.language || 'en';

// Hifadhi kwenye localStorage mara moja
localStorage.setItem('access_token', accessToken);
localStorage.setItem('user_role', userRole);
localStorage.setItem('user_name', userName);
localStorage.setItem('user_lang', userLang);

// Set Authorization header kwa Axios kwa future requests zote
axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`;

toast.success('✅ Login successful! Welcome!');

// Smart Redirection kulingana na Role
const roleDashboardRoutes = {
  admin: '/dashboard/admin',
  owner: '/dashboard/owner',
  user: '/dashboard/user'    // default route
};

await router.push(roleDashboardRoutes[userRole] || '/dashboard/user');



    localStorage.setItem('access_token', accessToken)
    localStorage.setItem('user_role', userRole)

    // Set Authorization Header kwa future requests
    axios.defaults.headers.common['Authorization'] = `Bearer ${accessToken}`

    toast.success('✅ Login successful! Welcome!')

    // Smart Redirection based on role
    if (userRole === 'admin') {
      await router.push('/dashboard/admin')
    } else if (userRole === 'owner') {
      await router.push('/dashboard/owner')
    } else {
      await router.push('/dashboard/user') // default kwa user wa kawaida
    }
  } catch (err) {
    if (err.response?.status === 401) {
      toast.error('❌ Invalid credentials. Please check your username/email/phone and password.')
    } else {
      toast.error('❌ Login failed. Please try again.')
    }
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.bg-dark {
  background: #202228 !important;
}
.card {
  box-shadow: 0 6px 36px 0 #0005, 0 0 0 2px #ffd70033;
}
input.form-control,
.input-group-text {
  background: #232338 !important;
  color: #fff !important;
  border: none !important;
}
input.form-control::placeholder {
  color: #aaa !important;
  opacity: 1;
}
input:focus {
  outline: none !important;
  box-shadow: 0 0 0 2px #ffd70077 !important;
}
hr {
  border-top: 2px solid #ffd700 !important;
}
.btn-warning {
  background-color: #ffd700 !important;
  color: #181829 !important;
  border: none !important;
  font-weight: 600;
}
.btn-warning:active, .btn-warning:focus {
  background: #ffec80 !important;
}
</style>
