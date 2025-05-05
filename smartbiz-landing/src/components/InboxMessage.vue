<template>
  <div class="message-box">
    <div class="top">
      <strong>{{ message.sender_name || 'Unknown' }}</strong>
      <span class="platform">{{ message.platform }}</span>
    </div>
    <p>{{ message.message }}</p>
    <small>{{ formatDate(message.received_at) }}</small>

    <form @submit.prevent="sendReply">
      <input v-model="replyText" placeholder="Type your reply..." />
      <button type="submit">Reply</button>
    </form>

    <div v-if="status">{{ status }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['message'],
  data() {
    return {
      replyText: '',
      status: ''
    }
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleString()
    },
    async sendReply() {
      try {
        const payload = {
          chat_id: this.message.chat_id,
          platform: this.message.platform,
          message: this.replyText
        }

        const res = await axios.post('/send-reply', payload, {
          headers: { Authorization: 'Bearer ' + localStorage.getItem('access_token') }
        })

        this.status = res.data.message || "Sent!"
        this.replyText = ''
      } catch (err) {
        this.status = "Failed to send"
      }
    }
  }
}
</script>

<style scoped>
.message-box {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 8px;
}
form {
  margin-top: 0.5rem;
  display: flex;
  gap: 8px;
}
input {
  flex: 1;
  padding: 5px;
}
</style>
