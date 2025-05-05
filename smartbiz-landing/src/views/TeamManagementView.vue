<template>
  <div class="container py-5">
    <!-- Header -->
    <div class="d-flex justify-between items-center mb-6">
      <h2 class="text-primary text-xl font-bold">👥 Team Management</h2>
      <button class="btn btn-primary" @click="showAddModal = true">➕ Add Staff</button>
    </div>

    <!-- Staff Table -->
    <div class="card p-4 shadow-sm border-0">
      <table class="table table-hover">
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Role</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="staff in staffList" :key="staff.id">
            <td>{{ staff.fullName }}</td>
            <td>{{ staff.email }}</td>
            <td>{{ staff.role }}</td>
            <td>
              <span class="badge bg-success" v-if="staff.active">Active</span>
              <span class="badge bg-secondary" v-else>Pending</span>
            </td>
            <td>
              <button class="btn btn-sm btn-outline-primary" @click="editStaff(staff)">Edit</button>
              <button class="btn btn-sm btn-outline-danger" @click="removeStaff(staff.id)">Remove</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Add/Edit Staff Modal -->
    <div v-if="showAddModal" class="modal d-block bg-black bg-opacity-50">
      <div class="modal-dialog">
        <div class="modal-content p-4">
          <div class="modal-header">
            <h5 class="modal-title text-primary">{{ isEditing ? 'Edit Staff' : 'Add Staff Member' }}</h5>
            <button class="btn-close" @click="closeModal"></button>
          </div>

          <div class="modal-body">
            <form @submit.prevent="handleSave">
              <div class="mb-3">
                <label class="form-label">Full Name</label>
                <input type="text" v-model="form.fullName" class="form-control" required />
              </div>
              <div class="mb-3">
                <label class="form-label">Email</label>
                <input type="email" v-model="form.email" class="form-control" required />
              </div>
              <div class="mb-3">
                <label class="form-label">Role</label>
                <select v-model="form.role" class="form-select">
                  <option value="viewer">Viewer</option>
                  <option value="agent">Agent</option>
                  <option value="manager">Manager</option>
                </select>
              </div>
              <div class="form-check mb-3">
                <input type="checkbox" v-model="form.sendInvite" class="form-check-input" id="inviteCheck" />
                <label for="inviteCheck" class="form-check-label">Send Invite Email</label>
              </div>
              <div class="text-end">
                <button type="submit" class="btn btn-success">💾 Save</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const showAddModal = ref(false)
const isEditing = ref(false)
const staffList = ref([])

const form = ref({
  id: null,
  fullName: '',
  email: '',
  role: 'viewer',
  sendInvite: true
})

function fetchStaff() {
  axios.get('/api/team').then(res => {
    staffList.value = res.data
  })
}

function handleSave() {
  const payload = { ...form.value }
  if (isEditing.value) {
    axios.put(`/api/team/${payload.id}`, payload).then(() => {
      fetchStaff()
      closeModal()
    })
  } else {
    axios.post('/api/team', payload).then(() => {
      fetchStaff()
      closeModal()
    })
  }
}

function editStaff(staff) {
  form.value = { ...staff, sendInvite: false }
  isEditing.value = true
  showAddModal.value = true
}

function removeStaff(id) {
  if (confirm('Are you sure you want to remove this staff member?')) {
    axios.delete(`/api/team/${id}`).then(() => fetchStaff())
  }
}

function closeModal() {
  showAddModal.value = false
  isEditing.value = false
  form.value = {
    id: null,
    fullName: '',
    email: '',
    role: 'viewer',
    sendInvite: true
  }
}

fetchStaff()
</script>

<style scoped>
.card {
  border-radius: 1rem;
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1050;
}
.modal-dialog {
  max-width: 500px;
  width: 100%;
}
.modal-content {
  border-radius: 1rem;
}
</style>
