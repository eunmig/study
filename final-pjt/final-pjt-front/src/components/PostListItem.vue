<template>
  <div>
    <table>
      <colgroup>
        <col style="width: 25%;"> <!-- Adjust the width as needed -->
        <col style="width: 25%;"> <!-- Adjust the width as needed -->
        <col style="width: 25%;"> <!-- Adjust the width as needed -->
        <col style="width: 25%;"> <!-- Adjust the width as needed -->
      </colgroup>
      <tbody>
        <tr>
          <td>{{ post.category.name }}</td>
          <td>{{ post.title }}</td>
          <td>{{ post.id }}번 글</td>
          <td>
            <RouterLink :to="{ name: 'DetailView', params: { id: post.id } }">
              [DETAIL]
            </RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
    <p v-if="post.length === 0">게시글이 없습니다.</p>
  </div>
</template>
  
<script setup>
import { RouterLink } from 'vue-router';

defineProps({ post: Object })
</script>
  
<style scoped>

</style>