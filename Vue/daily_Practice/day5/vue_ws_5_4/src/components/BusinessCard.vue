<template>
    <div>
        <h3>보유 명함 목록</h3>
        <p v-if="businessCards.length==0">명함이 없습니다.</p>
        <p v-else>현재 보유중인 명함 수 : {{ businessCards.length }}</p>
        <BusinessCardDetail :businessCards="businessCards" @delete-card="deleteCard"/>
    </div>
</template>

<script setup>
import BusinessCardDetail from '@/components/businessCardDetail.vue';
import { ref } from 'vue'

const businessCards = ref([
    { name : '일론 머스크', title : '테슬라 테크노킹' },
    { name : '래리 엘리슨', title : '오라클 창업주' },
    { name : '빌 게이츠', title : '마이크로소프트 창업주' },
    { name : '래리 페이지', title : '구글 공동창업주' },
    { name : '세르게이 브린', title : '구글 공동창업주' },
])

const deleteCard = function (cardToDelete) {
        const index = businessCards.value.findIndex(card => card.name === cardToDelete.name);
        // 해당 인덱스의 명함을 배열에서 제거합니다.
        if (index > -1) {
            businessCards.value.splice(index, 1);
        }
    }
</script>

<style scoped>
h3, p {
    text-align: center;
}

</style>