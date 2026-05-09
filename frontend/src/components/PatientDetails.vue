<template>
  <div class="patient-details">
    <h2>{{ patient.name }}</h2>
    <p><strong>Age:</strong> {{ patient.age }}</p>
    <p><strong>Gender:</strong> {{ patient.gender }}</p>
    <p><strong>Allergies:</strong> {{ patient.allergies.join(', ') }}</p>
  </div>
</template>

<script setup>
import { defineProps } from 'vue';
const props = defineProps({
  patient: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
.patient-details {
  border: 1px solid #ccc;
  padding: 1rem;
  border-radius: 4px;
}
</style>
