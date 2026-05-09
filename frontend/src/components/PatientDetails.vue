<template>
  <div>
    <h2>Patient List</h2>
    <ul>
      <li v-for="patient in patients" :key="patient.id">
        {{ patient.name }} ({{ patient.age }}세)
      </li>
    </ul>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const patients = computed(() => store.getters['patient/allPatients'])

onMounted(() => {
  store.dispatch('patient/fetchPatients')
})
</script>
