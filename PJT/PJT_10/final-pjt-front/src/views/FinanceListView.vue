<template>
<<<<<<< HEAD
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>예적금 목록</span>
        </h1>
        <br>
=======
    <div>
        <h1>금융 아이템 목록 페이지</h1>
        <hr>
        <FinanceList/>
>>>>>>> 5f1367ace20c3b6af39823011830c3433fb7eb1b
    </div>
    <FinanceList/>
</template>

<script setup>
import FinanceList from '../components/FinanceList.vue'
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useFinanceStore } from '../stores/finance'

const store = useFinanceStore()

onMounted(()=> {
    store.getProducts()
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>