<template>
  <div class="container py-5">
    <div class="d-flex justify-between items-center mb-4">
      <h2 class="text-primary text-xl font-bold">📬 Support Inbox</h2>
    </div>

    <!-- Ticket Table -->
    <div class="card p-4 shadow-sm border-0">
      <table class="table table-striped">
        <thead class="table-light">
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Subject</th>
            <th>Type</th>
            <th>Status</th>
            <th>Submitted</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="ticket in tickets" :key="ticket.id">
            <td>{{ ticket.id }}</td>
            <td>{{ ticket.user_id }}</td>
            <td>{{ ticket.subject }}</td>
            <td>{{ ticket.type }}</td>
            <td>
              <span class="badge bg-success" v-if="ticket.status === 'open'">Open</span>
              <span class="badge bg-secondary" v-else>Closed</span>
            </td>
            <td>{{ formatDate(ticket.created_at) }}</td>
            <td>
              <button class="btn btn-sm btn-primary" @click="viewTicket(ticket)">View</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Ticket Modal -->
    <div v-if="selectedTicket" class="modal d-block bg-black bg-opacity-50">
      <div class="modal-dialog">
        <div class="modal-content p-4">
          <div class="modal-header">
            <h5 class="modal-title">Ticket #{{ selectedTicket.id }}</h5>
            <button class="btn-close" @click="selectedTicket = null"></button>
          </div>
          <div class="modal-body">
            <p><strong>Subject:</strong> {{ selectedTicket.subject }}</p>
            <p><strong>Type:</strong> {{ selectedTicket.type }}</p>
            <p><strong>Description:</strong><br /> {{ selectedTicket.description }}</p>
            <p v-if="selectedTicket.attachment">
              <strong>Attachment:</strong>
              <a :href="getAttachmentUrl(selectedTicket.attachment)" target="_blank">Download</a>
            </p>
          </div>
          <div class="modal-footer">
            <button class="btn btn-secondary" @click="selectedTicket = null">Close</button>
            <button class="btn btn-danger" @click="closeTicket(selectedTicket.id)">Close Ticket</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const tickets = ref([])
const selectedTicket = ref(null)

onMounted(async () => {
  const res = await axios.get('/api/admin/support')
  tickets.value = res.data
})

function viewTicket(ticket) {
  selectedTicket.value = ticket
}

function formatDate(dateStr) {
  return new Date(dateStr).toLocaleString()
}

function getAttachmentUrl(path) {
  return `/` + path
}

async function closeTicket(id) {
  await axios.put(`/api/admin/support/close/${id}`)
  selectedTicket.value = null
  tickets.value = tickets.value.map(t => t.id === id ? { ...t, status: 'closed' } : t)
}
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
  max-width: 600px;
  width: 100%;
}
.modal-content {
  border-radius: 1rem;
}
</style>
