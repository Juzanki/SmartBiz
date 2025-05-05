<template>
  <div class="container py-5">
    <!-- Top Header -->
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h2 class="text-primary fw-bold">📅 Scheduled Promotions</h2>
      <button class="btn btn-success d-flex align-items-center gap-1" @click="showModal = true">
        <span class="fs-5">➕</span> Schedule New Promotion
      </button>
    </div>

    <!-- Promotions Card -->
    <div v-if="promotions.length" class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
      <div v-for="promo in promotions" :key="promo.id" class="col">
        <div class="card shadow-sm">
          <div class="card-body">
            <h5 class="card-title">{{ promo.title }}</h5>
            <p class="card-text">
              <strong>Channel:</strong> {{ promo.channel }}<br />
              <strong>Scheduled:</strong> {{ promo.date }} at {{ promo.time }}<br />
              <strong>Status:</strong>
              <span
                :class="{
                  'badge bg-success': promo.status === 'Scheduled',
                  'badge bg-secondary': promo.status === 'Sent',
                  'badge bg-danger': promo.status === 'Failed'
                }"
              >
                {{ promo.status }}
              </span>
            </p>
            <button class="btn btn-outline-primary btn-sm" @click="viewPromotion(promo.id)">
              View Details
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="text-center py-5">
      <img
        src="https://cdn-icons-png.flaticon.com/512/747/747310.png"
        alt="No data"
        style="max-width: 150px;"
        class="mb-3"
      />
      <h5 class="text-danger">No promotions scheduled</h5>
      <p class="text-muted">Plan your next campaign easily by clicking the green button above!</p>
    </div>

    <!-- Custom Vue Modal -->
    <transition name="fade">
      <div v-if="showModal" class="modal-backdrop">
        <div class="modal-content-box">
          <h5 class="mb-3 fw-bold text-primary">📝 Schedule New Promotion</h5>
          <form @submit.prevent="submitNewPromotion">
            <div class="mb-2">
              <label class="form-label">Title</label>
              <input type="text" class="form-control" v-model="newPromotion.title" required />
            </div>
            <div class="mb-2">
              <label class="form-label">Message</label>
              <textarea class="form-control" v-model="newPromotion.message" rows="3" required></textarea>
            </div>
            <div class="mb-2">
              <label class="form-label">Channel</label>
              <select class="form-select" v-model="newPromotion.channel" required>
                <option value="">-- Select --</option>
                <option>WhatsApp</option>
                <option>Telegram</option>
                <option>SMS</option>
                <option>Email</option>
              </select>
            </div>
            <div class="mb-2">
              <label class="form-label">Scheduled Date</label>
              <input type="date" class="form-control" v-model="newPromotion.date" required />
            </div>
            <div class="mb-3">
              <label class="form-label">Scheduled Time</label>
              <input type="time" class="form-control" v-model="newPromotion.time" required />
            </div>
            <div class="d-flex justify-content-between">
              <button class="btn btn-secondary" type="button" @click="showModal = false">Cancel</button>
              <button class="btn btn-primary" type="submit">Save</button>
            </div>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const promotions = ref([]) // Array to hold promotions
const showModal = ref(false) // To control modal visibility

const newPromotion = ref({
  title: '',
  message: '',
  channel: '',
  date: '',
  time: '',
  status: 'Scheduled'
})

onMounted(() => {
  fetchPromotions() // Fetch promotions on component mount
})

function fetchPromotions() {
  const saved = JSON.parse(localStorage.getItem('my_promotions')) || [] // Retrieve stored promotions
  promotions.value = saved
}

function isDateValid(dateStr, timeStr) {
  const now = new Date()
  const scheduled = new Date(`${dateStr}T${timeStr}`)
  return scheduled > now // Ensures the date is not in the past
}

function submitNewPromotion() {
  if (!isDateValid(newPromotion.value.date, newPromotion.value.time)) {
    alert('You cannot schedule a promotion in the past.')
    return
  }

  const promo = {
    id: Date.now(),
    ...newPromotion.value
  }

  promotions.value.push(promo)
  localStorage.setItem('my_promotions', JSON.stringify(promotions.value)) // Store updated promotions
  showModal.value = false // Close the modal
  newPromotion.value = { title: '', message: '', channel: '', date: '', time: '', status: 'Scheduled' } // Reset form
  alert('✅ Promotion scheduled successfully!')
}

function viewPromotion(id) {
  router.push(`/promotion-profile/${id}`)
}
</script>

<style scoped>
.table-hover tbody tr:hover {
  background-color: #f9f9f9;
}

.card {
  border-radius: 1rem;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1050;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content-box {
  background: white;
  padding: 2rem;
  width: 90%;
  max-width: 500px;
  border-radius: 1rem;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
}
</style>
