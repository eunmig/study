<template>
    <div>
        <!-- 기본 이벤트 동작 막기 -->
        <form @submit.prevent="createCardFunc" class="form-box">
            <label for="text">이름 : </label>
            <input type="text" id="name" v-model="name">

            <label for="text">직함 : </label>
            <input type="text" id="title" v-model="title">

            <button type="submit">명함 추가</button>
        </form>
    </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue'

const name = ref('')
const title = ref('')
const newCard = ref(null)

const emit = defineEmits(['createCardEvent'])

const createCardFunc = () => {
    const cardInfo = { name : name.value, title : title.value }
    newCard.value = cardInfo
    emit('createCardEvent', cardInfo)
    // 이름과 직함 빈칸으로 세팅
    name.value = ''
    title.value = ''
}
</script>

<style scoped>
.form-box {
    display: flex;
    justify-content: center;

}
</style>