<template>
  <div class="card p-4 border-0 shadow-sm">
    <h5 class="mb-3 text-primary">💬 Live Chat</h5>
    <div class="chat-box mb-3">
      <div v-for="(msg, i) in messages" :key="i" class="mb-1">
        <strong>{{ msg.user }}:</strong> {{ msg.text }}
      </div>
    </div>
    <form @submit.prevent="sendMessage">
      <div class="input-group">
        <input type="text" v-model="newMessage" class="form-control" placeholder="Type message..." />
        <button class="btn btn-primary">Send</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const messages = ref([])
const newMessage = ref('')
const ws = ref(null)

onMounted(() => {
  ws.value = new WebSocket(`ws://${window.location.host}/ws/live/chat`)
  ws.value.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data)
      messages.value.push(data)
    } catch {
      messages.value.push({ user: 'Guest', text: event.data })
    }
  }
})

onUnmounted(() => {
  if (ws.value) ws.value.close()
})

function sendMessage() {
  if (!newMessage.value.trim()) return
  const msg = { user: 'Me', text: newMessage.value }
  ws.value.send(JSON.stringify(msg))
  newMessage.value = ''
}
</script>

<style scoped>
.chat-box {
  max-height: 200px;
  overflow-y: auto;
  background: #f8f9fa;
  padding: 10px;
  border-radius: 8px;
}
</style>
