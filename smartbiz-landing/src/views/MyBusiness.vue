<template>
  <div class="container py-5">
    <!-- Section Title -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">🏢 My Business</h2>
      <button class="btn btn-success" @click="openAddModal">
        ➕ Add New Business
      </button>
    </div>

    <!-- Business List -->
    <div v-if="businesses.length" class="row g-4">
      <div class="col-md-6 col-lg-4" v-for="biz in businesses" :key="biz.id">
        <div 
          class="card h-100 shadow-sm border-0"
          :class="{'border-primary': biz.id === selectedBusinessId}"
          @click="selectBusiness(biz.id)"
          style="cursor: pointer;"
        >
          <div class="card-body text-center">
            <img 
              :src="biz.logo || defaultLogo" 
              alt="Logo" 
              class="rounded-circle mb-3 bg-light"
              style="width: 80px; height: 80px; object-fit: cover;"
            >
            <h5 class="card-title fw-bold">{{ biz.name }}</h5>
            <p class="text-muted small mb-2">{{ biz.type }}</p>
            <a :href="biz.website" target="_blank" class="small text-decoration-none">
              🌐 {{ biz.website }}
            </a>
          </div>
          <div class="card-footer bg-transparent border-top-0 text-center">
            <button class="btn btn-outline-primary btn-sm w-100" @click.stop="viewBusinessProfile(biz.id)">
              View Profile
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <h4 class="text-muted">No businesses linked yet.</h4>
      <button class="btn btn-primary mt-3" @click="openAddModal">
        ➕ Link a Business Now
      </button>
    </div>

    <!-- Add Business Modal -->
    <div class="modal fade" id="addBusinessModal" tabindex="-1" aria-labelledby="addBusinessModalLabel" aria-hidden="true" ref="addModal">
      <div class="modal-dialog">
        <div class="modal-content">
          <form @submit.prevent="submitNewBusiness">
            <div class="modal-header">
              <h5 class="modal-title" id="addBusinessModalLabel">Add New Business</h5>
              <button type="button" class="btn-close" @click="closeAddModal"></button>
            </div>
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Business Name</label>
                <input type="text" class="form-control" v-model="newBusiness.name" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Business Type</label>
                <input type="text" class="form-control" v-model="newBusiness.type" required>
              </div>
              <div class="mb-3">
                <label class="form-label">Website</label>
                <input type="url" class="form-control" v-model="newBusiness.website">
              </div>
              <div class="mb-3">
                <label class="form-label">Logo URL</label>
                <input type="url" class="form-control" v-model="newBusiness.logo">
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" @click="closeAddModal">Cancel</button>
              <button type="submit" class="btn btn-primary">Save Business</button>
            </div>
          </form>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const businesses = ref([])
const selectedBusinessId = ref(localStorage.getItem('business_id') || null)
const addModal = ref(null)

const newBusiness = ref({
  name: '',
  type: '',
  website: '',
  logo: ''
})

const defaultLogo = '/default-logo.png' // Customize path for default logo

onMounted(() => {
  fetchBusinesses()
})

// Fetch existing businesses from your API or localStorage (demo purpose)
function fetchBusinesses() {
  const demoBusinesses = JSON.parse(localStorage.getItem('my_businesses')) || []
  businesses.value = demoBusinesses
}

// Select a business and save to localStorage
function selectBusiness(id) {
  selectedBusinessId.value = id
  localStorage.setItem('business_id', id)
  alert('Switched to new business successfully!')
}

// Open the modal to add a new business
function openAddModal() {
  const modal = new bootstrap.Modal(addModal.value)
  modal.show()
}

// Close the modal
function closeAddModal() {
  const modal = bootstrap.Modal.getInstance(addModal.value)
  modal.hide()
}

// Submit new business
function submitNewBusiness() {
  const biz = { 
    id: Date.now(), 
    ...newBusiness.value 
  }
  businesses.value.push(biz)
  localStorage.setItem('my_businesses', JSON.stringify(businesses.value))
  closeAddModal()
  newBusiness.value = { name: '', type: '', website: '', logo: '' }
  alert('New business added successfully!')
}

// View full profile
function viewBusinessProfile(id) {
  router.push(`/business-profile/${id}`)
}
</script>

<style scoped>
.card:hover {
  transform: scale(1.03);
  transition: 0.3s;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
}
</style>
