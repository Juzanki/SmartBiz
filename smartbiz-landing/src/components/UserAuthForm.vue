<template>
  <div class="auth-form">
    <h2>{{ formTitle }}</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" required />
      </div>

      <div class="form-group">
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" required />
      </div>

      <button type="submit">{{ isLogin ? 'Login' : 'Register' }}</button>
    </form>

    <p @click="toggleForm" class="form-toggle">
      {{ isLogin ? "Don't have an account? Register" : "Already have an account? Login" }}
    </p>
  </div>
</template>

<script>
export default {
  name: "UserAuthForm", // ✅ Multi-word name

  data() {
    return {
      isLogin: true,
      email: "",
      password: ""
    };
  },

  computed: {
    formTitle() {
      return this.isLogin ? "Login" : "Register";
    }
  },

  methods: {
    handleSubmit() {
      if (this.isLogin) {
        console.log("Logging in with:", this.email, this.password);
        // Fanya API call ya login hapa
      } else {
        console.log("Registering with:", this.email, this.password);
        // Fanya API call ya register hapa
      }
    },

    toggleForm() {
      this.isLogin = !this.isLogin;
    }
  }
};
</script>

<style scoped>
.auth-form {
  max-width: 400px;
  margin: auto;
  padding: 2rem;
  border-radius: 8px;
  background: #f9f9f9;
}

.form-group {
  margin-bottom: 1rem;
}

input {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.25rem;
}

button {
  width: 100%;
  padding: 0.6rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
}

.form-toggle {
  margin-top: 1rem;
  color: #007bff;
  cursor: pointer;
  text-align: center;
}
</style>
