<template>
  <b-navbar toggleable="lg" type="dark" variant="primary">
    <b-navbar-brand href="#">Bus Booking Admin</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/admin/dashboard">DashBoard</b-nav-item>
        <b-nav-item to="/admin/buses">Buses</b-nav-item>
        <b-nav-item to="/admin/schedules">Schedules</b-nav-item>
        <b-nav-item to="/admin/bookings">Bookings</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "AppNavbar"
}
</script>
