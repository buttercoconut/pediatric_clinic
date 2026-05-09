<template>
  <div>
    <h2>Doctor Profile</h2>
    <div v-if="doctor">
      <p>Name: {{ doctor.name }}</p>
      <p>Specialty: {{ doctor.specialty }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const doctor = ref(null)

onMounted(async () => {
  const res = await fetch('/api/doctors/1')
  doctor.value = await res.json()
})
</script>
