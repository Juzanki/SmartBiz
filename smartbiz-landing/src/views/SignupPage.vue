 <template>
  <div class="min-vh-100 d-flex align-items-center justify-content-center bg-dark">
    <div
      class="card shadow-lg p-4 rounded-4 border-2 border-warning"
      style="background:#181829; max-width:390px; width:100%;"
    >
      <!-- LOGO Centered -->
      <div class="d-flex flex-column align-items-center mb-4 mt-2">
        <img
          src="@/assets/logo-circle.png"
          alt="SmartBiz Logo"
          class="rounded-circle border border-warning mb-3 shadow"
          style="width:64px;height:64px;object-fit:contain;background:#fff;"
        />
        <h2 class="fw-bold text-warning text-center mb-0" style="font-size:1.45rem;">Create Your Account</h2>
      </div>
      <hr class="mb-4 border-warning opacity-75"/>
      <form @submit.prevent="onSignup" autocomplete="off">
        <div class="mb-3">
          <label class="form-label text-warning small" for="fullname">Full Name</label>
          <input type="text" id="fullname" v-model.trim="form.full_name" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="60" autocomplete="name" placeholder="e.g. Julius Zakayo" />
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small" for="username">Username</label>
          <input type="text" id="username" v-model.trim="form.username" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="30" autocomplete="username" placeholder="Unique username" />
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small" for="email">Email Address</label>
          <input type="email" id="email" v-model.trim="form.email" class="form-control bg-[#232338] text-light border-0"
                 required maxlength="100" autocomplete="email" placeholder="your@email.com" />
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small" for="password">Password</label>
          <input type="password" id="password" v-model="form.password" class="form-control bg-[#232338] text-light border-0"
                 required minlength="8" autocomplete="new-password" placeholder="Strong password" />
          <div v-if="form.password && !isStrongPassword(form.password)" class="text-danger small mt-1">
            Password must be at least 8 characters, use upper/lowercase, a number & a symbol.
          </div>
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small">Phone Number</label>
          <div class="d-flex gap-2">
            <select v-model="form.country_code" class="form-select w-auto bg-[#232338] text-light border-0" required>
              <option v-for="code in countryCodes" :key="code.value" :value="code.value">{{ code.label }}</option>
            </select>
            <input type="tel" v-model="form.phone_number" required pattern="^[1-9][0-9]{7,13}$"
                   class="form-control bg-[#232338] text-light border-0 flex-grow-1"
                   maxlength="13" autocomplete="tel" placeholder="712345678" />
          </div>
          <span class="form-text small text-secondary mt-1">
            Start without 0 (e.g. <span class="text-warning">712345678</span>)
          </span>
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small">Preferred Language</label>
          <select class="form-select bg-[#232338] text-light border-0" v-model="form.language" required>
            <option value="sw">Kiswahili</option>
            <option value="en">English</option>
            <option value="fr">Français</option>
            <option value="ar">العربية</option>
          </select>
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small">Business Name <span class="text-xs text-secondary">(Optional)</span></label>
          <input type="text" class="form-control bg-[#232338] text-light border-0"
                 v-model="form.business_name" maxlength="60" />
        </div>
        <div class="mb-3">
          <label class="form-label text-warning small">Business Type <span class="text-xs text-secondary">(Optional)</span></label>
          <select class="form-select bg-[#232338] text-light border-0" v-model="form.business_type">
            <option value="">Select Business Type (optional)</option>
            <option value="Retail">Retail</option>
            <option value="Service">Service</option>
            <option value="Wholesale">Wholesale</option>
            <option value="Education">Education</option>
            <option value="Other">Other</option>
          </select>
        </div>
        <!-- CHECKBOX (imetengenezwa) -->
        <div class="form-check d-flex align-items-center gap-2 mb-3">
          <input
            type="checkbox"
            id="terms"
            v-model="agreed"
            required
            class="form-check-input bg-[#232338] border-warning"
            style="accent-color:#ffd700; width:1.15em; height:1.15em; margin-top:0.25em; cursor:pointer;"
          />
          <label for="terms" class="form-check-label small text-light" style="cursor:pointer">
            I agree to the <a href="#" class="text-warning text-decoration-underline">terms and conditions</a>
          </label>
        </div>
        <button class="btn btn-warning w-100 fw-bold py-2 rounded-3" :disabled="loading || !canSubmit">
          <span v-if="loading"><span class="spinner-border spinner-border-sm me-1"></span> Signing Up...</span>
          <span v-else>Sign Up</span>
        </button>
      </form>
      <div class="text-center mt-4 text-secondary small">
        Already have an account?
        <router-link to="/login" class="text-warning fw-bold ms-1 text-decoration-underline">Login</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useToast } from 'vue-toastification'

const countryCodes = [
  { value: '+255', label: '🇹🇿 +255 (TZ)' },
  { value: '+254', label: '🇰🇪 +254 (KE)' },
  { value: '+256', label: '🇺🇬 +256 (UG)' },
  { value: '+250', label: '🇷🇼 +250 (RW)' },
  { value: '+257', label: '🇧🇮 +257 (BI)' },
  { value: '+211', label: '🇸🇸 +211 (SS)' },
  { value: '+27',  label: '🇿🇦 +27 (ZA)' },
  { value: '+234', label: '🇳🇬 +234 (NG)' },
  { value: '+233', label: '🇬🇭 +233 (GH)' },
  { value: '+20',  label: '🇪🇬 +20 (EG)' },
  { value: '+1',   label: '🇺🇸 +1 (US)' },
  { value: '+44',  label: '🇬🇧 +44 (UK)' },
  { value: '+91',  label: '🇮🇳 +91 (IN)' }
]
const toast = useToast()
const router = useRouter()
const loading = ref(false)
const agreed = ref(false)

const form = ref({
  full_name: '',
  username: '',
  email: '',
  password: '',
  country_code: '+255',
  phone_number: '',
  language: 'sw',
  business_name: '',
  business_type: ''
})

const isStrongPassword = (password) =>
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/.test(password)

const canSubmit = computed(() =>
  form.value.full_name &&
  form.value.username &&
  form.value.email &&
  form.value.password &&
  form.value.phone_number &&
  agreed.value &&
  isStrongPassword(form.value.password)
)

const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

const onSignup = async () => {
  if (!canSubmit.value) {
    toast.error('Please fill all required fields correctly!')
    return
  }
  loading.value = true
  try {
    const payload = { ...form.value }
    payload.phone_number = `${form.value.country_code}${form.value.phone_number}`
    const response = await axios.post(`${API_BASE}/auth/register`, payload)
    toast.success('🎉 Signup successful! Please login.')
    router.push('/login')
  } catch (err) {
    toast.error(
      err.response?.data?.detail ||
      err.response?.data?.message ||
      err.message ||
      '❌ Signup failed. Please try again.'
    )
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
  border: 2px solid #ffd700 !important;
}
input.form-control,
select.form-select,
.form-check-input {
  background: #232338 !important;
  color: #fff !important;
  border: none !important;
}
input.form-control::placeholder,
select.form-select,
.form-check-label {
  color: #aaa !important;
  opacity: 1;
}
input:focus,
select:focus {
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
.text-warning { color: #ffd700 !important; }
/* --------- FIX CHECKBOX ----------- */
.form-check-input {
  accent-color: #ffd700 !important;
  width: 1.15em;
  height: 1.15em;
  margin-top: 0.25em;
  cursor: pointer;
  border: 2px solid #ffd700 !important;
  appearance: auto !important;
  -webkit-appearance: auto !important;
}
.form-check-label { cursor: pointer; }
</style>
