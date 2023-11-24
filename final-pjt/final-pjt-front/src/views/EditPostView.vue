<template>
  <div class="create-post-container">
    <h1>Edit Post</h1>
    <form @submit.prevent="editPost" class="post-form">
      <div class="form-field">
        <label for="category">카테고리 : </label>
        <select id="category" v-model="selectedCategory" class="select">
          <option v-for="category in store.categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>

      <div class="form-field">
        <label for="title">제목 : </label>
        <input type="text" id="title" v-model.trim="title" class="input" placeholder="수정할 제목을 작성해주세요." />
      </div>

      <div class="form-field">
        <label for="content">내용 : </label>
        <textarea name="content" id="content" v-model.trim="content" class="input" placeholder="수정할 내용을 작성해주세요."></textarea>
      </div>

      <button type="submit">수정하기</button>
    </form>
    <button @click="deletePost" class="delete-btn">게시글 삭제</button>
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

    const deletePost = () => {
    console.log('포스트 삭제 완료')
    axios({
        method: 'delete',
        url: `${store.API_URL}/community/post_delete/${post_pk}/`,
        headers: {
            Authorization: `Token ${token}`
        }
    }).then((res) => {
        // Remove the deleted post from local storage
        const communityData = JSON.parse(localStorage.getItem('community')) || { posts: [], categories: [] };
        console.log(communityData)
        // Filter out the deleted post
        communityData.posts = communityData.posts.filter(post => post.id !== post_pk);

        // Update local storage
        localStorage.setItem('community', JSON.stringify(communityData));

        router.push({ name: 'Post' });
    })
}

</script>

<style scoped>
@import "@/views/CreatePostView.scss"

</style>
