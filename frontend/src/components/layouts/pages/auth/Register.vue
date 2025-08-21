<!-- src/pages/auth/Register.vue -->
<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card shadow">
          <div class="card-body">
            <h3 class="text-center mb-4">Register</h3>
            <form @submit.prevent="register">
              <div class="mb-3">
                <label>Name</label>
                <input v-model="name" type="text" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Email</label>
                <input v-model="email" type="email" class="form-control" required />
              </div>
              <div class="mb-3">
                <label>Password</label>
                <input v-model="password" type="password" class="form-control" required />
              </div>
              <button type="submit" class="btn btn-success w-100">Register</button>
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
    return { name: "", email: "", password: "" };
  },
  methods: {
    async register() {
      alert(`Registering ${this.name}`);
      // Call backend API
    },
  },
};
</script>
