<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script setup>
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

createApp(App).use(router).use(store).mount('#app')
</script>
