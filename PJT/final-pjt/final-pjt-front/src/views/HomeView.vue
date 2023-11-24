<template>
<div class="video-container" v-if="showVideo && isAuthenticated && count==0">
  <button @click="toggleVideo">skip</button>
  <video ref="myVideo" width="320" height="240" autoplay muted @ended="onVideoEnded">
    <source :src="videoSource" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

<div v-else>

  <div id="carouselExampleIndicators" class="carousel slide">
    <div class="carousel-indicators">
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 0"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 1"></button>
      <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 2"></button>
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
        <img src="@/assets/main2.jpg" class="d-block w-100" alt="main2">
        <div class="carousel-caption-img">
          <img src="@/assets/car.png" alt="car">
        </div>
        <div class="carousel-caption">
          <h3 class="text-black">BUY</h3>
          <h1 class="fw-bold text-black">미리 준비하는</h1>
          <h1 class="fw-bold text-black">자동차 적금</h1>
          <RouterLink :to="{ name: 'Car' }">바로가기</RouterLink>
        </div>
      </div>

      <div class="carousel-item">
        <img src="@/assets/main3.jpg" class="d-block w-100" alt="main3">
        <div class="carousel-caption-img">
          <img src="@/assets/map.png" alt="지도아이콘">
        </div>
        <div class="carousel-caption">
          <h3 class="text-black">Search</h3>
          <h1 class="fw-bold text-black">주변 은행을</h1>
          <h1 class="fw-bold text-black">찾으세요!</h1>
          <RouterLink :to="{ name: 'Bank' }">바로가기</RouterLink>
        </div>
      </div>
      
    </div>
  </div>

  <br><br>

  <div class="container">
  <div class="row">
    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h3 class="card-title">나에게 맞는 자동차를 구매하자 🚗💨</h3>
        </div>
        <div class="card-body">
          <ul>
            <p>주어진 연봉 정보를 기반으로</p>
            <li>금융상품과 금액 설정 -> 만기 시 해당하는 금액대의 자동차 추천</li>
            <li>희망 자동차와 연봉 정보 -> 적절한 자동차 추천</li>
          </ul>
          <br>
          <ul>
            <p>연봉별 자동차</p>
            <li>- 3,000만원 이하 : 스파크, 레이, 모닝 => 경차 (권장하지 않음😢)</li>
            <li>- 3,500만원 이하 : k3, 아반떼, 셀토스 => 경차 ~ 준중형</li>
            <li>- 4,000만원 이하 : 코나, 니로, k5</li>
            <li>- 6,000만원 이하 : 그랜져, 싼타페, G70</li>
            <li>- 8,000만원 이하 :  g80, gv80, 외제차</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="col-md-6">
      <div class="card">
        <div class="card-header">
          <h3 class="card-title">단리, 복리란 🧐?</h3>
        </div>
        <div class="card-body">
          <p>금리 계산방법의 종류</p>
          <ul>
            <li>단기 : 원금에 대해서만 이지가 붙는 방식</li>
            <li>복리 : '원금 + 이자'에 이자가 붙는 방식</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  </div>
</div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useVideoStore } from '../stores/video'

const authStore = useAuthStore()
const isAuthenticated = authStore.isAuthenticated
const videoStore = useVideoStore()

const showVideo = ref(true)
const toggleVideo = () => {
  showVideo.value = false
}
const videoSource = computed(() => '/src/assets/video/intro.mp4')

const count = ref(videoStore.count)
const onVideoEnded = () => {
  showVideo.value = false;
  videoStore.onVideoEnded()
}

onMounted(() => {

  console.log(authStore.isAuthenticated)
  console.log(videoStore.count)
})

</script>

<style scoped>
@import "@/views/HomeView.scss"

</style>