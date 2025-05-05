<template>
  <div class="container py-5">
    <!-- Title + New -->
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="fw-bold text-primary d-flex gap-2 items-center">
        <i class="bi bi-robot"></i>
        Smart Autoresponders
      </h2>
      <button class="btn btn-outline-primary" @click="showModal = true">
        <i class="bi bi-plus-circle me-1"></i> New Rule
      </button>
    </div>

    <!-- Info Card -->
    <div class="card mb-4 border-0 shadow-sm rounded-4">
      <div class="card-body">
        <h5 class="fw-semibold mb-2 text-dark">How It Works</h5>
        <p class="text-muted small">
          Define triggers and responses for customer messages on WhatsApp, Telegram, or SMS.
          SmartBiz will automatically respond based on keywords.
        </p>
      </div>
    </div>

    <!-- Rules Table -->
    <div class="card border-0 shadow-sm rounded-4">
      <div class="card-body">
        <h5 class="text-secondary fw-semibold mb-3">Active Rules</h5>
        <div class="table-responsive">
          <table class="table table-hover align-middle">
            <thead class="table-light">
              <tr>
                <th>Platform</th>
                <th>Keyword</th>
                <th>Response</th>
                <th>Status</th>
                <th class="text-end">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(rule, index) in rules" :key="index">
                <td>{{ rule.platform }}</td>
                <td><span class="badge bg-secondary">{{ rule.keyword }}</span></td>
                <td>{{ rule.response }}</td>
                <td>
                  <span class="badge" :class="rule.active ? 'bg-success' : 'bg-danger'">
                    {{ rule.active ? 'Active' : 'Inactive' }}
                  </span>
                </td>
                <td class="text-end">
                  <button class="btn btn-sm btn-outline-info me-2" @click="editRule(index)">
                    <i class="bi bi-pencil"></i>
                  </button>
                  <button class="btn btn-sm btn-outline-danger" @click="deleteRule(index)">
                    <i class="bi bi-trash"></i>
                  </button>
                </td>
              </tr>
              <tr v-if="rules.length === 0">
                <td colspan="5" class="text-center text-muted py-4">No autoresponders yet.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal fade show d-block" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content shadow rounded-4">
          <div class="modal-header">
            <h5 class="modal-title">{{ isEditing ? 'Edit Rule' : 'New Rule' }}</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <form @submit.prevent="saveRule">
            <div class="modal-body">
              <div class="mb-3">
                <label class="form-label">Platform</label>
                <select class="form-select" v-model="form.platform" required>
                  <option value="WhatsApp">WhatsApp</option>
                  <option value="Telegram">Telegram</option>
                  <option value="SMS">SMS</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label">Trigger Keyword</label>
                <input type="text" class="form-control" v-model="form.keyword" required placeholder="e.g. order" />
              </div>
              <div class="mb-3">
                <label class="form-label">Response Message</label>
                <textarea rows="3" class="form-control" v-model="form.response" required></textarea>
              </div>
              <div class="form-check">
                <input type="checkbox" class="form-check-input" id="activeCheck" v-model="form.active" />
                <label class="form-check-label" for="activeCheck">Mark as Active</label>
              </div>
            </div>
            <div class="modal-footer">
              <button class="btn btn-secondary" type="button" @click="closeModal">Cancel</button>
              <button class="btn btn-primary" type="submit">{{ isEditing ? 'Update' : 'Save' }}</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const rules = ref([
  { platform: 'WhatsApp', keyword: 'price', response: 'Our price is 50,000 TZS.', active: true },
  { platform: 'Telegram', keyword: 'hours', response: 'We’re open Mon–Sat, 8–6.', active: true },
])

const showModal = ref(false)
const isEditing = ref(false)
const editIndex = ref(null)

const form = ref({
  platform: 'WhatsApp',
  keyword: '',
  response: '',
  active: true
})

function openModal() {
  showModal.value = true
}
function closeModal() {
  showModal.value = false
  isEditing.value = false
  resetForm()
}

function resetForm() {
  form.value = {
    platform: 'WhatsApp',
    keyword: '',
    response: '',
    active: true
  }
}

function saveRule() {
  if (isEditing.value) {
    rules.value[editIndex.value] = { ...form.value }
    isEditing.value = false
  } else {
    rules.value.push({ ...form.value })
  }
  closeModal()
}

function editRule(index) {
  form.value = { ...rules.value[index] }
  isEditing.value = true
  editIndex.value = index
  showModal.value = true
}

function deleteRule(index) {
  if (confirm('Are you sure?')) {
    rules.value.splice(index, 1)
  }
}
</script>

<style scoped>
.modal {
  background-color: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(3px);
}
</style>
