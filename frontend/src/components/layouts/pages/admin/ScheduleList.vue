<template>
  <div>
    <h2 class="mb-3">Schedules</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Bus</th>
          <th>Date</th>
          <th>Time</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="schedule in schedules" :key="schedule.id">
          <td>{{ schedule.id }}</td>
          <td>{{ schedule.bus }}</td>
          <td>{{ schedule.date }}</td>
          <td>{{ schedule.time }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ScheduleList",
  data() {
    return {
      schedules: [
        { id: 1, bus: "Bus A", date: "2025-08-21", time: "10:00 AM" },
        { id: 2, bus: "Bus B", date: "2025-08-22", time: "02:00 PM" }
      ]
    }
  }
}
</script>
