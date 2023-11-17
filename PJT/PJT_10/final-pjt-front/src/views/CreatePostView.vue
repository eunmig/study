<template>
    <div>
      <form @submit.prevent="createPost">
        <label for="category">카테고리: </label>
        <select id="category" v-model="selectedCategory">
          <option v-for="category in store.categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select><br>
  
        <label for="title">제목: </label>
        <input type="text" id="title" v-model.trim="title" /><br>
  
        <label for="content">내용: </label>
        <textarea name="content" id="content" v-model.trim="content"></textarea><br>
  
        <button type="submit">게시물 작성</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useCommunityStore } from '@/stores/community'
  import { useRouter } from 'vue-router'
  import axios from 'axios'
  import { useAuthStore } from '../stores/auth'

  const router = useRouter()
  const store = useCommunityStore()
  const authStore = useAuthStore()
  const title = ref(null)
  const content = ref(null)
  const selectedCategory = ref(null)
  const token = authStore.token
  
  onMounted(() => {
    store.getCategories()
  });
  
  const createPost = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/api/v1/posts/${selectedCategory.value}/post/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: {
        title: title.value,
        content: content.value
      },
    }).then(() => {
      router.push({ name: 'Home' })
    }).catch(err => console.log(err))
  };
  </script>
  
  <style scoped>
  
  </style>
  