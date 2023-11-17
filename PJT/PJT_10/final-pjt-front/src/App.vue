<template>
  <div>
    <!-- 나중에 v-if 로  프로필 링크와 전환 -->
    <div class="login-status">
      로그인 상태
      <RouterLink class="link" :to="{ name:'SignUp' }">회원가입</RouterLink> | 
      <RouterLink class="link" :to="{ name:'LogIn' }">로그인</RouterLink> | 
    </div>
    <nav>
      <RouterLink class="link" :to="{ name:'Home' }">Home</RouterLink> | 
      <RouterLink class="link" :to="{ name:'Post' }">게시글</RouterLink> | 
      <RouterLink class="link" :to="{ name:'FinanceItems' }">예적금 리스트</RouterLink> | 
      <RouterLink class="link" :to="{ name:'Bank' }">은행 지도</RouterLink> | 

      
    </nav>
  </div>
  <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>