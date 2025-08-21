<!-- src/pages/auth/Login.vue -->
<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow">
          <div class="card-body">
            <h3 class="text-center mb-4">Login</h3>
            <form @submit.prevent="login">
              <div class="mb-3">
                <label>Email</label>
                <input v-model="email" type="email" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Password</label>
                <input v-model="password" type="password" class="form-control" required />
              </div>
              <button type="submit" class="btn btn-primary w-100">Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return { email: "", password: "" };
  },
  methods: {
    async login() {
      alert(`Logging in with ${this.email}`);
      // Call backend API
    },
  },
};
</script>
