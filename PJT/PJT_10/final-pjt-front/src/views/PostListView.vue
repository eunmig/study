<template>
    <div>
        <h1>게시글 목록 페이지</h1>
        <RouterLink class="link" :to="{ name:'CreatePost' }">게시물 생성</RouterLink> 
        <hr>
        <PostList />
    </div>
</template>

<script setup>
import { onMounted , ref } from 'vue'
import { useCommunityStore } from '@/stores/community'
import { RouterLink, RouterView } from 'vue-router'
import PostList from '../components/PostList.vue'
import CreatePostView from './CreatePostView.vue'

const store = useCommunityStore()

onMounted(() => {
    store.getPosts()
})

</script>

<style scoped>

</style>