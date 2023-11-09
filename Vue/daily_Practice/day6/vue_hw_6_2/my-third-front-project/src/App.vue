<template>
  <div>
    <MainPage />
    <RouterLink to="/">Some</RouterLink> |
    <RouterLink to="/other">Other</RouterLink>
    <RouterView></RouterView>

  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'
</script>

<style scoped>

</style>