<template>
  <div id="app">
    <Navbar />
    <b-container class="mt-3">
      <router-view />
    </b-container>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>
