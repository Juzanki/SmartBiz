<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-950 to-gray-800 text-white py-6 px-4">
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-3xl font-bold">SmartBiz Gift Shop</h1>
      <RouterLink to="/live-stream" class="bg-blue-600 px-4 py-2 text-sm font-semibold rounded hover:bg-blue-700 transition">
        Back to LiveStreamHub
      </RouterLink>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-6">
      <div
        v-for="gift in gifts"
        :key="gift.id"
        class="bg-gray-900 rounded-2xl p-4 text-center shadow-md border border-gray-700 hover:border-yellow-500 hover:scale-[1.04] transition-all duration-300"
      >
        <img :src="gift.image" alt="Gift Image" class="w-20 h-20 mx-auto mb-3 rounded-full object-cover shadow-lg" />
        <h2 class="text-md font-semibold text-white mb-1">{{ gift.name }}</h2>
        <p class="text-yellow-400 font-bold text-sm">
          {{ gift.coins }} {{ gift.coinType }}
        </p>
        <button
          @click="sendGift(gift)"
          class="mt-2 px-4 py-1 bg-pink-600 hover:bg-pink-700 text-white text-xs font-semibold rounded"
        >
          Send Gift
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const gifts = ref([])
const coinTypes = ['SmartCoin', 'JuzankiCoin', 'MegaGem', 'StreamPoint']

for (let i = 1; i <= 100; i++) {
  const coin = coinTypes[i % coinTypes.length]
  gifts.value.push({
    id: i,
    name: `${coin} Gift #${i}`,
    coins: (Math.floor(Math.random() * 100) + 1) * i,
    coinType: coin,
    image: `/assets/gifts/gift${(i % 12) + 1}.png` // 12 image placeholders
  })
}

function sendGift(gift) {
  alert(`You sent: ${gift.name} (${gift.coins} ${gift.coinType})`)
}
</script>

<style scoped>
/* You can enhance hover, transitions, and animations here */
</style>
