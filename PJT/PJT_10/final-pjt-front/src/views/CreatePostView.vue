<template>
  <div class="create-post-container">
    <div><h1>Create Post</h1></div>
    <form @submit.prevent="createPost" class="post-form">
      <div class="form-field">
        <label for="category">카테고리: </label>
        <select id="category" v-model="selectedCategory" class="select">
          <option v-for="category in store.categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>

      <div class="form-field">
        <label for="title">제목: </label>
        <input type="text" id="title" v-model.trim="title" class="input" placeholder="제목을 입력하세요" />
      </div>

      <div class="form-field">
        <label for="content">내용: </label>
        <textarea name="content" id="content" v-model.trim="content" class="input" placeholder="내용을 입력하세요"></textarea>
      </div>

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
  const userData = authStore.userData

  onMounted(() => {
    store.getCategories()
  })
  
  const createPost = function () {
    axios({
      method: 'post',
      url: `${store.API_URL}/community/posts/${selectedCategory.value}/post/`,
      headers: {
        Authorization: `Token ${token}`
      },
      data: {
        title: title.value,
        content: content.value
      },
    }).then(() => {
      router.push({ name: 'Post' })
    }).catch(err => console.log(err))
  }

  </script>
  
<style scoped>
@import "@/views/CreatePostView.scss"

</style>
  