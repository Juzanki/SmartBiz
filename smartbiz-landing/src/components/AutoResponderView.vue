<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold text-blue-900 mb-6">Auto Responders</h1>

    <div
      v-for="responder in responders"
      :key="responder.id"
      class="bg-white p-5 rounded-xl shadow border border-gray-200 mb-4"
    >
      <div class="flex justify-between items-center">
        <div>
          <h2 class="text-lg font-semibold text-blue-900">{{ responder.name }}</h2>
          <p class="text-sm text-gray-600">{{ responder.description }}</p>
        </div>

        <button
          @click="toggleResponder(responder.id)"
          :class="responder.active ? 'bg-green-600' : 'bg-gray-400'"
          class="text-white px-4 py-1 rounded-lg text-sm transition"
        >
          {{ responder.active ? 'Active' : 'Inactive' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const responders = reactive([
  {
    id: 1,
    name: "Welcome Bot",
    description: "Automatically greets new users.",
    active: true
  },
  {
    id: 2,
    name: "Follow Up Bot",
    description: "Sends follow-up messages after 24 hours.",
    active: false
  },
  {
    id: 3,
    name: "Promo Bot",
    description: "Shares promotions with your audience.",
    active: true
  }
]);

const toggleResponder = (id) => {
  const target = responders.find((r) => r.id === id);
  if (target) {
    target.active = !target.active;
  }
};
</script>
