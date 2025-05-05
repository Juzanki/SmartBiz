<template>
  <div class="min-h-screen flex flex-col bg-gray-100 p-6">
    <!-- Header -->
    <div class="flex flex-col md:flex-row justify-between items-center mb-6 gap-3">
      <h1 class="text-2xl font-bold text-blue-900 flex items-center gap-2">
        <span>👥</span> Manage Users
      </h1>
      <div class="input-group w-full md:w-80">
        <input
          v-model="searchQuery"
          type="text"
          class="form-control bg-light rounded-pill px-4 py-2"
          placeholder="Search by name or email..."
        />
      </div>
    </div>

    <!-- Users Table -->
    <div class="bg-white shadow rounded-3xl overflow-hidden">
      <table class="table table-hover mb-0">
        <thead class="table-light">
          <tr>
            <th scope="col">#</th>
            <th scope="col">Full Name</th>
            <th scope="col">Email</th>
            <th scope="col">Role</th>
            <th scope="col">Status</th>
            <th scope="col" class="text-end">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(user, index) in filteredUsers" :key="user.id">
            <th>{{ index + 1 }}</th>
            <td>{{ user.full_name }}</td>
            <td>{{ user.email }}</td>
            <td>
              <span class="badge bg-primary text-uppercase">{{ user.role }}</span>
            </td>
            <td>
              <span
                class="badge"
                :class="user.is_active ? 'bg-success' : 'bg-danger'"
              >
                {{ user.is_active ? 'Active' : 'Suspended' }}
              </span>
            </td>
            <td class="text-end">
              <div class="btn-group">
                <button class="btn btn-sm btn-outline-info" @click="viewUser(user)">
                  View
                </button>
                <button class="btn btn-sm btn-outline-warning" @click="editRole(user)">
                  Edit Role
                </button>
                <button
                  class="btn btn-sm btn-outline-danger"
                  @click="suspendUser(user)"
                  v-if="user.is_active"
                >
                  Suspend
                </button>
                <button
                  class="btn btn-sm btn-outline-secondary"
                  @click="deleteUser(user)"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
          <tr v-if="filteredUsers.length === 0">
            <td colspan="6" class="text-center py-4 text-muted">
              No users found.
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useToast } from 'vue-toastification'
import axios from 'axios'

const toast = useToast()
const users = ref([])
const searchQuery = ref('')
const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

onMounted(async () => {
  await fetchUsers()
})

const fetchUsers = async () => {
  try {
    const res = await axios.get(`${API_BASE}/admin/users`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    users.value = res.data
  } catch (err) {
    toast.error('Failed to load users.')
  }
}

const filteredUsers = computed(() => {
  if (!searchQuery.value) return users.value
  return users.value.filter(u =>
    u.full_name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    u.email.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

const viewUser = (user) => {
  toast.info(`Viewing profile: ${user.full_name}`)
  // Optionally: navigate to user detail page
}

const editRole = async (user) => {
  const newRole = prompt(`Change role for ${user.full_name} (user/admin/owner):`, user.role)
  if (!newRole) return
  try {
    await axios.put(`${API_BASE}/admin/users/${user.id}`, { role: newRole }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    toast.success('Role updated successfully!')
    await fetchUsers()
  } catch (err) {
    toast.error('Failed to update role.')
  }
}

const suspendUser = async (user) => {
  if (!confirm(`Are you sure you want to suspend ${user.full_name}?`)) return
  try {
    await axios.put(`${API_BASE}/admin/users/${user.id}`, { is_active: false }, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    toast.success('User suspended.')
    await fetchUsers()
  } catch (err) {
    toast.error('Failed to suspend user.')
  }
}

const deleteUser = async (user) => {
  if (!confirm(`Permanently delete ${user.full_name}? This action cannot be undone.`)) return
  try {
    await axios.delete(`${API_BASE}/admin/users/${user.id}`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('access_token')}` }
    })
    toast.success('User deleted successfully.')
    await fetchUsers()
  } catch (err) {
    toast.error('Failed to delete user.')
  }
}
</script>

<style scoped>
.table > :not(caption) > * > * {
  vertical-align: middle;
}
</style>
