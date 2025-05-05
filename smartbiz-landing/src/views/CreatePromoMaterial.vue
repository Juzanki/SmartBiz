<template>
  <div class="container py-5">
    <h2 class="text-primary fw-bold mb-4">🎯 Create Promo Material</h2>

    <!-- Select Campaign -->
    <div class="mb-4">
      <label class="form-label">Choose Campaign</label>
      <select v-model="selectedCampaign" class="form-select">
        <option v-for="c in campaigns" :key="c.id" :value="c.id">
          {{ c.title }} — {{ c.product.name }}
        </option>
      </select>
    </div>

    <!-- Referral Link + QR -->
    <div v-if="selectedCampaign" class="mb-4">
      <label class="form-label">Your Promo Link</label>
      <div class="input-group mb-2">
        <input class="form-control" :value="promoLink" readonly />
        <button class="btn btn-outline-secondary" @click="copyLink">📋 Copy</button>
      </div>
      <div class="text-center">
        <qrcode-vue :value="promoLink" :size="150" />
      </div>
    </div>

    <!-- HTML Embed with Preview -->
    <div v-if="selectedCampaign" class="card p-4 shadow-sm mt-4">
      <h5 class="text-muted mb-3">📍 Embed This Banner:</h5>
      <div class="text-center mb-3">
        <img :src="bannerPreview" alt="Promo Preview" class="img-fluid rounded shadow-sm" style="max-width: 320px;">
        <div class="form-text">Preview of what others will see.</div>
      </div>
      <pre class="bg-light p-2 rounded border">
&lt;a href=&quot;{{ promoLink }}&quot; target=&quot;_blank&quot;&gt;
  &lt;img src=&quot;{{ bannerPreview }}&quot; alt=&quot;Promote {{ selectedTitle }}&quot; style=&quot;width:300px; border-radius:12px;&quot; /&gt;
&lt;/a&gt;
      </pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import QrcodeVue from 'qrcode.vue'

const campaigns = ref([])
const selectedCampaign = ref('')
const username = localStorage.getItem('user_name') || 'affiliate'

onMounted(async () => {
  const res = await axios.get('/api/campaigns/my')
  campaigns.value = res.data
})

const selectedTitle = computed(() => {
  const match = campaigns.value.find(c => c.id === selectedCampaign.value)
  return match?.title || ''
})

const promoLink = computed(() => {
  if (!selectedCampaign.value) return ''
  return `https://smartbiz.com/ref/${username}?campaign=${selectedCampaign.value}`
})

const bannerPreview = computed(() => {
  return '/banners/default-banner.jpg' // can be dynamic per campaign
})

function copyLink() {
  navigator.clipboard.writeText(promoLink.value)
  alert('Promo link copied!')
}
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-break: break-word;
  font-size: 0.875rem;
}
</style>
