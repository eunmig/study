<template>
    <div>
        <ul class="nav bg-dark">
            <li class="nav-item">
                <RouterLink :to="{name: 'home'}" class="nav-link text-white">Home</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'search'}" class="nav-link text-white">Search</RouterLink>
            </li>
            <li class="nav-item">
                <RouterLink :to="{name: 'later'}" class="nav-link text-white">Later</RouterLink>
            </li>
            
        </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>