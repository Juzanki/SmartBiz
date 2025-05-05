<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div class="max-w-6xl mx-auto bg-white rounded-xl shadow p-8">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold text-blue-900">User Management</h1>
        <button
          class="bg-blue-900 text-white px-6 py-2 rounded-lg hover:bg-blue-800"
        >
          + Add User
        </button>
      </div>

      <!-- Search -->
      <div class="mb-6">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search users..."
          class="w-full p-3 border border-gray-300 rounded-lg"
        />
      </div>

      <!-- Users Table -->
      <div class="overflow-x-auto">
        <table class="w-full border">
          <thead class="bg-gray-50 text-left">
            <tr>
              <th class="py-3 px-4 text-sm text-gray-600">Name</th>
              <th class="py-3 px-4 text-sm text-gray-600">Email</th>
              <th class="py-3 px-4 text-sm text-gray-600">Role</th>
              <th class="py-3 px-4 text-sm text-gray-600">Status</th>
              <th class="py-3 px-4 text-sm text-gray-600">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="user in filteredUsers"
              :key="user.id"
              class="border-t hover:bg-gray-50"
            >
              <td class="py-3 px-4">{{ user.name }}</td>
              <td class="py-3 px-4">{{ user.email }}</td>
              <td class="py-3 px-4">{{ user.role }}</td>
              <td class="py-3 px-4">
                <span
                  :class="user.active ? 'text-green-600' : 'text-red-500'"
                  class="font-semibold"
                >
                  {{ user.active ? 'Active' : 'Inactive' }}
                </span>
              </td>
              <td class="py-3 px-4 flex gap-2">
                <button
                  class="text-blue-900 hover:underline"
                  @click="viewUser(user)"
                >
                  View
                </button>
                <button
                  class="text-yellow-600 hover:underline"
                  @click="toggleStatus(user)"
                >
                  {{ user.active ? 'Suspend' : 'Activate' }}
                </button>
                <button
                  class="text-red-600 hover:underline"
                  @click="deleteUser(user.id)"
                >
                  Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'UsersView'
})

import { ref, computed } from 'vue'

const searchQuery = ref('')

const users = ref([
  {
    id: 1,
    name: 'Jane Doe',
    email: 'jane@company.com',
    role: 'Admin',
    active: true
  },
  {
    id: 2,
    name: 'John Smith',
    email: 'john@company.com',
    role: 'Editor',
    active: false
  },
  {
    id: 3,
    name: 'Linda Brown',
    email: 'linda@company.com',
    role: 'Viewer',
    active: true
  }
])

const filteredUsers = computed(() => {
  return users.value.filter((user) =>
    user.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    user.email.toLowerCase().includes(searchQuery.value.toLowerCase())
  )
})

const toggleStatus = (user) => {
  user.active = !user.active
}

const deleteUser = (id) => {
  users.value = users.value.filter((u) => u.id !== id)
}

const viewUser = (user) => {
  alert(`User details:\nName: ${user.name}\nEmail: ${user.email}\nRole: ${user.role}`)
}
</script>

<style scoped>
/* You can add animation or status colors here */
</style>
