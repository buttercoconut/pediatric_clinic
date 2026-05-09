<template>
  <div class="appointment-form">
    <h2>New Appointment</h2>
    <form @submit.prevent="submitForm">
      <label>Patient ID:</input type="number" v-model="patientId" /</label>
      <label>Doctor ID:</input type="number" v-model="doctorId" /</label>
      <label>Date:</input type="datetime-local" v-model="date" /</label>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const patientId = ref("")
const doctorId = ref("")
const date = ref("")

const submitForm = async () => {
  const payload = {
    patientId: Number(patientId.value),
    doctorId: Number(doctorId.value),
    date: date.value
  }
  await fetch('/api/appointments', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  alert('Appointment created')
}
</script>
