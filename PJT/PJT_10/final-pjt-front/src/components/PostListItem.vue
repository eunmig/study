<template>
    <div>
        <p>{{ post.category.name }}</p>
        <p>{{ post.id }}번 글 | {{ post.title }}</p>
        <RouterLink :to="{ name: 'DetailView', params: { id: post.id } }">
            [DETAIL]
        </RouterLink>
      <hr>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router';
  
  defineProps({ post: Object })
  </script>
  
  <style scoped>

  </style>