<template>
  <div>
    <h2 class="mb-3">Buses</h2>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Route</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="bus in buses" :key="bus.id">
          <td>{{ bus.id }}</td>
          <td>{{ bus.name }}</td>
          <td>{{ bus.route }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "BusList",
  data() {
    return {
      buses: [
        { id: 1, name: "Bus A", route: "City A - City B" },
        { id: 2, name: "Bus B", route: "City C - City D" }
      ]
    }
  }
}
</script>
