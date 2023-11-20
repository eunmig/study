<template>
  <div id="main-page">
    <div v-if="authStore.isAuthenticated">
      <form @submit.prevent="authStore.logOut">
        <input type="submit" value="로그아웃">
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

      </nav>
    </div>
  </div>

  <div id="carouselExampleIndicators" class="carousel slide">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="@/assets/main1.jpg" class="d-block w-100" alt="main1">
      <div class="carousel-caption-img">
        <img src="@/assets/환율.png" alt="환율">
      </div>
        <div class="carousel-caption">
        <h3 class="text-black">환전이 처음이라면</h3>
        <h1 class="fw-bold text-black">환율우대</h1>
        <h1 class="fw-bold text-black">최대 100% 혜택!</h1>
        <RouterLink :to="{ name: 'Exchange' }">바로가기</RouterLink>
      </div>
    </div>

    <div class="carousel-item">
      <div class="carousel-item active">
        <img src="@/assets/main2.jpg" class="d-block w-100" alt="main2">
      </div>
      <div class="carousel-caption-img">
        <img src="@/assets/이벤트.png" alt="이벤트">
      </div>
      <div class="carousel-caption">
        <h3 class="text-black">OPEN</h3>
        <h1 class="fw-bold text-black">미리 준비하는</h1>
        <h1 class="fw-bold text-black">X-MAS 선물</h1>
        <a href="">바로가기</a>
      </div>
    </div>

    <!-- 3번째 이미지만 출력되지않아 디버깅 필요 -->
    <!-- <div class="carousel-item">
      <div class="carousel-item active">
        <img src="@/assets/main3.jpg" class="d-block w-100" alt="main3">
      </div>
      <div class="carousel-caption-img">
        <img src="@/assets/map.jpg" alt="map">
      </div>
      <div class="carousel-caption">
        <h3 class="text-black">두둥</h3>
        <h1 class="fw-bold text-black">주변 은행을</h1>
        <h1 class="fw-bold text-black">찾아라</h1>
        <RouterLink :to="{ name: 'Bank' }">바로가기</RouterLink>
      </div>
    </div> -->


  </div>

  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>



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
}

.carousel-item img {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
  }

</style>