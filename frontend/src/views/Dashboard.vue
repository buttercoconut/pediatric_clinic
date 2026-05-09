<template>
  <div>
    <h1>Dashboard</h1>
    <PatientDetails />
    <AppointmentList />
    <DoctorProfile />
  </div>
</template>

<script setup>
import PatientDetails from '../components/PatientDetails.vue'
import AppointmentList from '../components/AppointmentList.vue'
import DoctorProfile from '../components/DoctorProfile.vue'
</script>
