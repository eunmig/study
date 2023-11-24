<template>
    <div>
        <h3>게시판</h3>
        <hr>
        <table>
            <colgroup>
                <col style="width: 25%;"> <!-- Adjust the width as needed -->
                <col style="width: 25%;"> <!-- Adjust the width as needed -->
                <col style="width: 25%;"> <!-- Adjust the width as needed -->
                <col style="width: 25%;"> <!-- Adjust the width as needed -->
            </colgroup>
            <thead>
            <tr>
                <th>카테고리</th>
                <th>제목</th>
                <th>번호</th>
                <th>자세히보기</th>
            </tr>
            </thead>
        </table>

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

<style scoped>
h2 { 
    font-weight: border; 
}

</style>