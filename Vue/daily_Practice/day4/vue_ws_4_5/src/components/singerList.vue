<template>
    <div>
        <h1 class="title">가수 목록</h1>
    </div>
    <div class="card-container">
        <!-- <SingerDetail /> <SingerDetail /> -->
        <!-- :singer="singer" 부분은 SingerDetail 컴포넌트에 데이터를 전달하는 부분 -->
        <!-- :key를 사용하여 컴포넌트를 고유하게 식별 -->
        <SingerDetail v-for="singer in singers" :key="singer.name" :singer="singer" />
    </div>
</template>

<script setup>
// import SingerDetail from './singers/SingerDetail.vue';
import SingerDetail from './singers/SingerDetail.vue';

const singers = [
    { name : 'adele'},
    { name : 'maroon 5'},
    { name : 'Dua Lipa'}
]
</script>

<style scoped>
div {
    display: flex;
    align-items: center;
    justify-content: center;
}

.title {
    text-align: center;
    color: orange;
}

.card-container {
    display: flex; /* 카드를 가로로 나란히 배치하기 위한 스타일 */
    flex-wrap: wrap; /* 화면 크기에 맞게 자동 줄 바꿈 */
}
</style>