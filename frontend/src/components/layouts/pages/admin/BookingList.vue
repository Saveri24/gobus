<template>
  <div>
    <h2 class="mb-3">Bookings</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Passenger</th>
          <th>Bus</th>
          <th>Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="booking in bookings" :key="booking.id">
          <td>{{ booking.id }}</td>
          <td>{{ booking.passenger }}</td>
          <td>{{ booking.bus }}</td>
          <td>{{ booking.date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "BookingList",
  data() {
    return {
      bookings: [
        { id: 1, passenger: "Alice", bus: "Bus A", date: "2025-08-21" },
        { id: 2, passenger: "Bob", bus: "Bus B", date: "2025-08-22" }
      ]
    }
  }
}
</script>
