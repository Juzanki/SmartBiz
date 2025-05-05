<template>
  <div class="p-6 max-w-2xl">
    <h1 class="text-2xl font-bold text-blue-900 mb-6">User Settings</h1>

    <form @submit.prevent="updateSettings" class="space-y-6 bg-white p-6 rounded-xl shadow border border-gray-200">
      <!-- Name -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
        <input
          v-model="user.name"
          type="text"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <!-- Email -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input
          v-model="user.email"
          type="email"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <!-- Password -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">New Password</label>
        <input
          v-model="user.password"
          type="password"
          placeholder="Leave blank to keep current"
          class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <!-- Notifications -->
      <div class="flex items-center gap-2">
        <input
          v-model="user.notifications"
          type="checkbox"
          id="notifications"
          class="w-4 h-4 text-blue-600"
        />
        <label for="notifications" class="text-sm text-gray-700">Enable Email Notifications</label>
      </div>

      <!-- Submit -->
      <div class="pt-2">
        <button
          type="submit"
          class="bg-blue-900 text-white px-6 py-2 rounded-lg hover:bg-blue-800 transition"
        >
          Save Changes
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive } from "vue";

const user = reactive({
  name: "Jane Doe",
  email: "jane@example.com",
  password: "",
  notifications: true
});

const updateSettings = () => {
  console.log("Updated Settings:", user);
  alert("Settings saved successfully!");
  // Baadaye tumia Axios au fetch kupeleka kwa backend
};
</script>
