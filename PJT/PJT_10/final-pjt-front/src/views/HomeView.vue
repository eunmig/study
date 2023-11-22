<template>
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
          <img src="@/assets/이벤트.png" alt="이벤트">
        </div>
        <div class="carousel-caption">
          <h3 class="text-black">OPEN</h3>
          <h1 class="fw-bold text-black">미리 준비하는</h1>
          <h1 class="fw-bold text-black">X-MAS 선물</h1>
          <a href="">바로가기</a>
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
  <div>
    <h1 class="content">자동차를 구매하자 🚗</h1>
      <br><br>
      <p>주어진 연봉 정보를 기반으로</p>
      <p>1. 금융상품과 금액 설정 -> 만기 시 해당하는 금액대의 자동차 추천</p>
      <p>2. 희망 자동차와 연봉 정보 -> 적절한 자동차 추천</p>
  </div>
</template>

<script setup>


</script>

<style scoped>
@import "@/views/HomeView.scss"

</style>