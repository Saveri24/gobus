<template>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="/">GoBus</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <!-- User Links -->
        <b-nav-item to="/">Home</b-nav-item>
        <b-nav-item to="/search">Search</b-nav-item>
        <b-nav-item to="/my-bookings">My Bookings</b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <!-- Admin Links -->
        <b-nav-item-dropdown text="Admin" right>
          <b-dropdown-item to="/admin/dashboard">Dashboard</b-dropdown-item>
          <b-dropdown-item to="/admin/buses">Buses</b-dropdown-item>
          <b-dropdown-item to="/admin/schedules">Schedules</b-dropdown-item>
          <b-dropdown-item to="/admin/bookings">Bookings</b-dropdown-item>
        </b-nav-item-dropdown>

        <!-- Auth -->
        <b-nav-item to="/login">Login</b-nav-item>
        <b-nav-item to="/register">Register</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
};
</script>
