<template>
  <div class="appointment-list">
    <h2>Upcoming Appointments</h2>
    <ul>
      <li v-for="appointment in appointments" :key="appointment.id">
        {{ appointment.date }} - {{ appointment.doctor_name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const appointments = ref([]);

onMounted(async () => {
  const response = await axios.get('/api/appointments');
  appointments.value = response.data;
});
</script>

<style scoped>
.appointment-list {
  margin: 1rem;
}
</style>
