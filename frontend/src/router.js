import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from './views/Dashboard.vue'
import AppointmentForm from './views/AppointmentForm.vue'

const routes = [
  { path: '/', component: Dashboard },
  { path: '/appointments/new', component: AppointmentForm }
]

export default createRouter({
  history: createWebHistory(),
  routes
})