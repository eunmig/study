<template>
    <div class="two alt-two">
        <h1>게시글 목록 페이지
            <span>   </span>
        </h1>
        <br>
    </div>
    <RouterLink class="create-post" :to="{ name:'CreatePost' }">게시물 생성</RouterLink> 
    <PostList />
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
    console.log('onMounted: PostList')
    console.log('남은 게시글.', store.posts)

})

</script>

<style lang="scss">
@import "@/views/PostListView.scss";

</style>