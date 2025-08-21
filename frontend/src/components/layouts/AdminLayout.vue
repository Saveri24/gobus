<template>
  <div>
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Bus Booking Admin</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/admin/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/admin/buses">Buses</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/admin/schedules">Schedules</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/admin/bookings">Bookings</router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Page content -->
    <div class="container mt-4">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminLayout"
}
</script>
