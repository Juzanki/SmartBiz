<template>
  <div class="relative h-screen w-screen overflow-hidden bg-black">
    <!-- Camera View -->
    <video ref="videoRef" autoplay playsinline class="absolute inset-0 object-cover w-full h-full z-0"></video>

    <!-- Overlay: Top Controls -->
    <div class="absolute top-3 left-3 right-3 flex justify-between items-center z-10 px-4">
      <div class="flex items-center gap-2">
        <span class="bg-green-500 text-white text-xs font-bold px-2 py-1 rounded">LIVE</span>
        <button @click="leaveStream" class="bg-red-600 text-white px-3 py-1 rounded">Leave</button>
      </div>
      <button @click="switchCamera" class="bg-gray-700 text-white px-2 py-1 rounded">Switch Cam</button>
    </div>

    <!-- Flying Gift Animations -->
    <transition-group name="gift-fly" tag="div" class="fixed top-0 left-0 w-full h-full pointer-events-none z-40">
      <div
        v-for="g in animatedGifts"
        :key="g.uid"
        class="absolute"
        :style="g.style"
      >
        <img :src="g.image" :alt="g.name" class="w-20 h-20 object-contain animate__animated animate__fadeInDown" />
        <div class="text-center text-white font-bold text-sm mt-1 bg-black bg-opacity-50 px-2 py-1 rounded">
          {{ g.name }}
        </div>
      </div>
    </transition-group>

    <!-- Floating Product -->
    <transition name="fade">
      <div v-if="currentProduct" :class="['absolute z-20', positionClass]">
        <div class="bg-white bg-opacity-90 rounded shadow p-3 animate-bounce">
          <img :src="currentProduct.image" class="w-16 h-16 object-cover rounded mb-2" />
          <div class="text-sm font-semibold">{{ currentProduct.name }}</div>
          <div class="text-green-600 font-bold text-sm">TZS {{ currentProduct.price }}</div>
          <button @click="placeOrder(currentProduct)" class="mt-1 text-xs text-white bg-green-500 px-2 py-1 rounded">Buy Now</button>
        </div>
      </div>
    </transition>

    <!-- Bottom Controls -->
    <div class="absolute bottom-0 left-0 right-0 p-4 flex flex-col items-center z-10">
      <div class="flex gap-3">
        <button @click="startStream" class="bg-pink-600 text-white font-semibold px-4 py-2 rounded">Go Live</button>
        <button @click="openProductModal" class="bg-blue-500 text-white px-4 py-2 rounded">Set Product</button>
        <button @click="sendGift" class="bg-yellow-400 text-black px-4 py-2 rounded">Send Gift</button>
      </div>
    </div>

    <!-- Chat Section -->
    <div class="absolute right-2 bottom-24 w-72 h-64 overflow-y-auto bg-white bg-opacity-20 text-white text-sm rounded p-2 z-10">
      <div v-for="msg in chatMessages" :key="msg.id" class="mb-1">
        <strong>{{ msg.user }}</strong>: {{ msg.text }}
      </div>
    </div>

    <!-- Product Modal -->
    <div v-if="showProductModal" class="fixed inset-0 z-30 bg-black bg-opacity-50 flex items-center justify-center">
      <div class="bg-white w-96 p-6 rounded shadow">
        <h3 class="text-lg font-bold mb-4">Set Product</h3>
        <input v-model="product.name" type="text" placeholder="Product Name" class="input mb-2 w-full" />
        <input v-model="product.price" type="number" placeholder="Price (TZS)" class="input mb-2 w-full" />
        <input type="file" @change="handleImageUpload" class="mb-2" />
        <select v-model="product.position" class="input mb-2 w-full">
          <option value="top">Top</option>
          <option value="center">Center</option>
          <option value="bottom">Bottom</option>
        </select>
        <div class="flex justify-between">
          <button @click="showProductModal = false" class="btn btn-secondary">Cancel</button>
          <button @click="setProduct" class="btn btn-primary">Set</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const videoRef = ref(null)
const chatMessages = ref([
  { id: 1, user: 'Alice', text: 'How much is it?' },
  { id: 2, user: 'Bob', text: 'I want that bag!' }
])

const showProductModal = ref(false)
const product = ref({ name: '', price: '', image: '', position: 'bottom' })
const currentProduct = ref(null)
const animatedGifts = ref([])
let counter = 0

const positionClass = computed(() => {
  switch (product.value.position) {
    case 'top': return 'top-10 left-1/2 transform -translate-x-1/2'
    case 'center': return 'top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2'
    case 'bottom': return 'bottom-10 left-1/2 transform -translate-x-1/2'
    default: return ''
  }
})

function startStream() {
  navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
      videoRef.value.srcObject = stream
    })
}

function leaveStream() {
  const tracks = videoRef.value?.srcObject?.getTracks()
  tracks?.forEach(track => track.stop())
  videoRef.value.srcObject = null
}

function switchCamera() {
  alert("Switch camera logic would go here")
}

function openProductModal() {
  showProductModal.value = true
}

function handleImageUpload(e) {
  const file = e.target.files[0]
  if (file) {
    product.value.image = URL.createObjectURL(file)
  }
}

function setProduct() {
  currentProduct.value = { ...product.value }
  showProductModal.value = false
}

function placeOrder(product) {
  alert(`Order placed for: ${product.name}`)
}

function sendGift() {
  const gift = {
    name: 'Phoenix Spirit',
    image: '/assets/gifts/phoenix.png'
  }
  launchGiftAnimation(gift)
}

function launchGiftAnimation(gift) {
  const uid = counter++
  const style = {
    top: `${Math.random() * 70 + 10}%`,
    left: `${Math.random() * 70 + 10}%`,
    transition: 'transform 3s ease-in-out',
    animation: 'flyGift 3s ease-in-out forwards',
  }
  animatedGifts.value.push({ ...gift, uid, style })
  setTimeout(() => {
    animatedGifts.value = animatedGifts.value.filter(g => g.uid !== uid)
  }, 3000)
}
</script>

<style scoped>
.input {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
}
.btn {
  padding: 8px 12px;
  border-radius: 4px;
}
.btn-primary {
  background-color: #2563eb;
  color: white;
}
.btn-secondary {
  background-color: #6b7280;
  color: white;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

@keyframes flyGift {
  0% {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
  50% {
    transform: translateY(-200px) scale(1.2);
    opacity: 0.8;
  }
  100% {
    transform: translateY(-400px) scale(1.5);
    opacity: 0;
  }
}
</style>
