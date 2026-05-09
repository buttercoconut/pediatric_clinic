<template>
  <div>
    <h2>Appointment List</h2>
    <ul>
      <li v-for="appointment in appointments" :key="appointment.id">
        {{ appointment.date }} - {{ appointment.doctorName }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const appointments = ref([])

onMounted(async () => {
  const res = await fetch('/api/appointments')
  appointments.value = await res.json()
})
</script>
