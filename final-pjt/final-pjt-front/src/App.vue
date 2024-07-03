<template>
  <div id="main-page">
    <div v-if="authStore.isAuthenticated" class="logout-container">
      <form @submit.prevent="authStore.logOut">
        <input type="submit" value="로그아웃" class="logout-button">
      </form>
    </div>
    <div v-else class="login-status">
      로그인 상태
      <RouterLink class="link" :to="{ name:'SignUp' }">회원가입</RouterLink> | 
      <RouterLink class="link" :to="{ name:'LogIn' }">로그인</RouterLink> | 
    </div>
    
    <div class="image-container">
      <nav>
        <RouterLink class="link" :to="{ name:'Home' }">Home</RouterLink> | 
        <RouterLink class="link" :to="{ name:'Post' }">게시글</RouterLink> | 
        <RouterLink class="link" :to="{ name:'FinanceItems' }">예적금 리스트</RouterLink> | 
        <RouterLink class="link" :to="{ name:'Bank' }">은행 지도</RouterLink> | 
        <RouterLink class="link" :to="{ name:'Exchange' }">환율</RouterLink> | 
        <RouterLink class="link" :to="{ name:'Profile' }">프로필</RouterLink> | 
      </nav>
    </div>
  </div>
  <br>
  <div class="main-content">
  <RouterView/>
  </div>
</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.css'
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/auth'



const authStore = useAuthStore()


</script>

<style lang="scss">
@import "@/App.scss";

body {
  width: 980px;
  height: 530px;
  margin: 0 auto;
  margin-top: 50px;
}

</style>
