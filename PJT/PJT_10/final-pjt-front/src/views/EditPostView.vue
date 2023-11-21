<template>
    <div>
      <form @submit.prevent="editPost">
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
  
        <button type="submit">게시물 수정</button>
      </form>
    </div>
</template>
  
<script setup>
    import { onMounted, ref } from 'vue'
    import { useCommunityStore } from '@/stores/community'
    import { useRouter, useRoute } from 'vue-router'
    import axios from 'axios'
    import { useAuthStore } from '../stores/auth'

    const router = useRouter()
    const route = useRoute()
    const store = useCommunityStore()
    const authStore = useAuthStore()
    const title = ref(null)
    const content = ref(null)
    const selectedCategory = ref(null)
    const token = authStore.token
    const userData = authStore.userData
    const post_pk = route.params.post_pk
    console.log('update', post_pk)


    const editPost = function () {
    axios({
        method: 'put',
        url: `${store.API_URL}/community/post_UD/${post_pk}/`,
        headers: {
        Authorization: `Token ${token}`
        },
        data: {
        title: title.value,
        content: content.value
        },
    }).then(() => {
        router.push({ name: 'DetailView', params: { id: post_pk } })
    }).catch(err => console.log(err))
    }

</script>

<style scoped>

</style>
