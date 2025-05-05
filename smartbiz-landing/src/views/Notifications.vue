<template>
  <div class="notifications">
    <h1 class="text-2xl font-bold mb-4">Notifications</h1>
    
    <div v-if="notifications.length === 0" class="text-gray-500">
      <p>No new notifications</p>
    </div>

    <ul v-else>
      <li v-for="notification in notifications" :key="notification.id" class="border-b py-2">
        <div class="flex justify-between">
          <span class="font-semibold">{{ notification.title }}</span>
          <span class="text-sm text-gray-400">{{ notification.date }}</span>
        </div>
        <p class="text-gray-600 mt-1">{{ notification.message }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notifications: [], // Data kwa ajili ya kudhihirisha taarifa
    };
  },
  created() {
    // Simulate fetching notifications
    this.fetchNotifications();
  },
  methods: {
    fetchNotifications() {
      // Hapa tunaweza kutuma request kwa backend kupata taarifa
      // Hapa ni mfano wa data inayoweza kurudi kutoka API
      this.notifications = [
        {
          id: 1,
          title: "New Order Placed",
          message: "A new order has been placed by a customer.",
          date: "2025-05-03 10:30",
        },
        {
          id: 2,
          title: "Account Update",
          message: "Your account has been successfully updated.",
          date: "2025-05-02 14:15",
        },
      ];
    },
  },
};
</script>

<style scoped>
.notifications {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
}

h1 {
  color: #333;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  background-color: #fff;
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 6px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}
</style>
