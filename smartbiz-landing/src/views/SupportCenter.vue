<template>
  <div class="container mt-5 max-w-3xl">
    <!-- Hii ni heading ya sehemu ya msaada -->
    <h2 class="fw-bold text-primary mb-2">🎧 {{ $t('support_center') }}</h2>
    <p class="text-muted mb-4">{{ $t('support_intro') }}</p>

    <!-- Kadi ya kuingiza tiketi ya msaada -->
    <div class="card p-4 shadow border-0">
      <form @submit.prevent="submitTicket">
        <!-- Sehemu ya kuingiza somo la tiketi -->
        <div class="mb-3">
          <label for="subject" class="form-label">{{ $t('subject') }}</label>
          <input v-model="form.subject" id="subject" type="text" class="form-control" required placeholder="Ingiza shida yako" />
        </div>

        <!-- Sehemu ya kuingiza maelezo ya shida -->
        <div class="mb-3">
          <label for="description" class="form-label">{{ $t('description') }}</label>
          <textarea v-model="form.description" id="description" rows="5" class="form-control" required placeholder="Eleza shida yako"></textarea>
        </div>

        <!-- Sehemu ya kupakia faili -->
        <div class="mb-3">
          <label for="file" class="form-label">{{ $t('attachment') }}</label>
          <input @change="handleFileUpload" type="file" class="form-control" id="file" />
        </div>

        <!-- Kitufe cha kutuma tiketi -->
        <div class="d-flex justify-content-end">
          <button type="submit" class="btn btn-primary">
            <span v-if="loading" class="spinner-border spinner-border-sm me-2"></span>
            {{ $t('submit_ticket') }}
          </button>
        </div>
      </form>

      <!-- Ujumbe wa mafanikio unapokatika tiketi -->
      <div v-if="successMessage" class="alert alert-success mt-3" role="alert">
        {{ successMessage }}
      </div>
    </div>
  </div>
</template>

<script setup>
// Hapa tunatangaza variables zinazohusika na fomu ya msaada
import { ref } from 'vue'
import axios from 'axios'

// Fomu ya tiketi
const form = ref({
  subject: '', // Somo la tiketi
  description: '', // Maelezo ya shida
  file: null // Faili la kuambatanisha
})

// Hali ya kuonyesha spinner wakati tiketi inatumwa
const loading = ref(false)

// Ujumbe wa mafanikio baada ya kutuma tiketi
const successMessage = ref('')

// Hii ni kazi ya kushughulikia kupakia faili
const handleFileUpload = (event) => {
  const file = event.target.files[0]
  form.value.file = file
}

// Hii ni kazi ya kutuma tiketi ya msaada
const submitTicket = async () => {
  loading.value = true
  successMessage.value = ''

  // Kuunda FormData kwa ajili ya kutuma tiketi
  const formData = new FormData()
  formData.append('subject', form.value.subject)
  formData.append('description', form.value.description)
  if (form.value.file) {
    formData.append('attachment', form.value.file)
  }

  try {
    // Kupata token kutoka kwa localStorage kwa ajili ya uthibitisho
    const token = localStorage.getItem('access_token')

    // Kutuma data kwa backend kupitia axios
    const response = await axios.post('/api/support', formData, {
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'multipart/form-data'
      }
    })

    // Ujumbe wa mafanikio
    successMessage.value = '✅ Tiketi imetumwa kwa mafanikio!'
    // Safisha fomu baada ya kutuma tiketi
    form.value.subject = ''
    form.value.description = ''
    form.value.file = null
  } catch (error) {
    // Ujumbe wa kosa ikiwa kutumwa hakukufaulu
    alert('Imeshindikana kutuma tiketi. Tafadhali jaribu tena.')
  } finally {
    // Weka loading kuwa false baada ya kumaliza
    loading.value = false
  }
}
</script>

<style scoped>
/* Hii ni mtindo wa kadi kwa fomu ya msaada */
.container {
  max-width: 720px;
}

/* Mtindo wa kadi ya msaada */
.card {
  border-radius: 1rem;
}

/* Spinner ya kuonyesha wakati wa kutuma tiketi */
.spinner-border {
  border-color: #fff;
}

/* Mtindo wa ujumbe wa mafanikio */
.alert {
  border-radius: 1rem;
}
</style>
