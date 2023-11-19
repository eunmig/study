<template>
    <div>
        <main>
        <h1> 자동차를 사자 </h1>
        <p class="sub-head">
            주어진 연봉 정보를 기반으로
        </p>
        <p>1. 금융상품과 금액 설정 -> 만기 시 해당하는 금액대의 자동차 추천</p>
        <p>2. 희망 자동차와 연봉 정보 -> 적절한 자동차 추천</p>
        </main>
    </div>
</template>

<script setup>


</script>

<style scoped>
body {
  font-family: 'Arial', sans-serif;
  background-color: #f8f9fa; /* Light gray background */
  margin: 0;
}

main {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
  background-color: #fff; /* White background */
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Light shadow */
}


h1 {
  color: #343a40; /* Dark gray text color */
}

.sub-head {
  color: #6c757d; /* Medium gray text color */
}

p {
  margin-bottom: 15px;
  line-height: 1.5;
  color: #495057; /* Dark gray text color */
}
</style>