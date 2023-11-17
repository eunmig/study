<template>
    <div>
        <h3>Post List</h3>
        <hr>
        <PostListItem
        v-for="post in store.posts"
        :key="post.id"
        :post="post"
        />

    </div>
</template>

<script setup>
import { useCommunityStore } from '@/stores/community'
import PostListItem from '@/components/PostListItem.vue'

const store = useCommunityStore()
</script>
