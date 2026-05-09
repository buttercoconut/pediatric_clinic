<template>
  <div class="doctor-profile">
    <h2>Dr. {{ doctor.name }}</h2>
    <p>Specialty: {{ doctor.specialty }}</p>
    <p>Experience: {{ doctor.years_of_experience }} years</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  doctor: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.doctor-profile {
  border: 1px solid #ddd;
  padding: 1rem;
  border-radius: 4px;
}
</style>
