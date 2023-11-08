<template>
    <div v-for="card in businessCards" :key="card.name">
        <h4>이름 : {{ card.name }}</h4>
        <p>직함 : {{ card.title }}</p>
        <button @click="deleteCardEvent(card)">명함 삭제</button>
    </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'

const props = defineProps({
    businessCards : Array,
    name : String,
    title : String,
})

const emit = defineEmits(['deleteCard'])

const deleteCardEvent = (card) => {
    emit('deleteCard', card)
}
</script>

<style scoped>
div {
    background-color: #e9e8e8; /* 회색 배경 */
    display: inline-block;
    text-align: center;
    width: 40%;
    margin: 20px;
    padding: 20px;
    border-radius: 10px;
}
</style>