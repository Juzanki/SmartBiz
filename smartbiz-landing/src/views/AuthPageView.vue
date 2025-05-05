<template>
  <div class="min-h-screen bg-gray-50 flex items-center justify-center p-4">
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <!-- Logo & Title -->
      <div class="text-center mb-8">
        <h1 class="text-3xl font-bold text-blue-900 mb-2">SmartBiz</h1>
        <p class="text-gray-600">
          {{ isLogin ? "Welcome back!" : "Start your free trial" }}
        </p>
      </div>

      <!-- Social Login Buttons -->
      <div class="grid grid-cols-2 gap-4 mb-8">
        <button
          class="flex items-center justify-center gap-2 bg-gray-100 text-gray-700 p-3 rounded-lg hover:bg-gray-200"
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M12.24 10.285V14.4h6.806c-.275 1.765-2.056 5.174-6.806 5.174-4.095 0-7.439-3.389-7.439-7.574s3.345-7.574 7.439-7.574c2.33 0 3.891.989 4.785 1.849l3.254-3.138C18.189 1.186 15.479 0 12.24 0c-6.635 0-12 5.365-12 12s5.365 12 12 12c6.926 0 11.52-4.869 11.52-11.726 0-.788-.085-1.39-.189-1.989H12.24z"
            />
          </svg>
          Google
        </button>
        <button
          class="flex items-center justify-center gap-2 bg-gray-100 text-gray-700 p-3 rounded-lg hover:bg-gray-200"
        >
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
            <path
              d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"
            />
          </svg>
          Facebook
        </button>
      </div>

      <!-- Divider -->
      <div class="flex items-center mb-8">
        <div class="flex-1 border-t border-gray-300"></div>
        <span class="px-4 text-gray-500 text-sm">OR</span>
        <div class="flex-1 border-t border-gray-300"></div>
      </div>

      <!-- Form -->
      <form @submit.prevent="handleSubmit">
        <div v-if="!isLogin" class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">
            Company Name
          </label>
          <input
            v-model="form.company"
            type="text"
            required
            class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2">
            Email
          </label>
          <input
            v-model="form.email"
            type="email"
            required
            class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <div class="mb-6">
          <label class="block text-gray-700 text-sm font-bold mb-2">
            Password
          </label>
          <input
            v-model="form.password"
            type="password"
            required
            class="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-900 text-white p-3 rounded-lg font-bold hover:bg-blue-800 mb-4"
        >
          {{ isLogin ? "Login" : "Sign Up Free" }}
        </button>

        <p class="text-center text-gray-600">
          {{ isLogin ? "Don't have an account?" : "Already have an account?" }}
          <a
            href="#"
            @click.prevent="toggleForm"
            class="text-blue-900 hover:underline"
          >
            {{ isLogin ? "Sign Up" : "Login" }}
          </a>
        </p>
      </form>
    </div>
  </div>
</template>

<script setup>
defineOptions({
  name: 'AuthPageView'
})

import { ref } from "vue";

const isLogin = ref(false);
const form = ref({
  company: "",
  email: "",
  password: ""
});

const handleSubmit = () => {
  if (isLogin.value) {
    console.log("Logging in with:", form.value);
  } else {
    console.log("Signing up with:", form.value);
  }
};

const toggleForm = () => {
  isLogin.value = !isLogin.value;
};
</script>

<style scoped>
input:focus {
  outline: none;
  box-shadow: 0 0 0 2px #d4af37;
}
</style>
