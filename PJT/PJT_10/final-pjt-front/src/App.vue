<template>
  <div id="main-page">
        <div class="login-status">
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
      </nav>
    </div>
  </div>
  <div class="main-content">
  <RouterView/>
  </div>
</template>

<script setup>
import 'bootstrap/dist/css/bootstrap.css'
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
/* Login status styles */
.login-status {
  position: fixed;
  top: 0;
  right: 10px;
  padding: 10px;
  background-color: #ffffff; /* White background */
  color: #0d0000; /* Text color */
  z-index: 1;
}

/* Navigation Styles */
nav {
  position: fixed;
  top: 40px;
  left: 0;
  right: 0;
  text-align: center;
  background-color: #fdfdfd; /* Google blue */
  padding: 10px 0;
  z-index: 1;
}

.link {
  color: #130000;
  text-decoration: none;
  padding: 10px 20px;
  margin: 0 10px;
  transition: background-color 0.3s ease;
}

.link:hover {
  background-color: #333; /* Light gray on hover */
}

.nav-image {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 10px; /* Adjust the distance from the navigation bar */
}

/* Main page styles */
.main-page {
  background-color: #ffffff; /* White background */
  color: #333; /* Text color */
  padding: 10px;
  margin: 0 auto;
  max-width: 1000px; /* Adjust the maximum width of the main page */
}

.main-content {
  padding-top: 60px; /* Adjust the padding to be equal to the height of your fixed navbar */
}
</style>