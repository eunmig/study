<template>
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>예적금 목록</span>
        </h1>
        <br>
    </div>
    <FinanceList/>
    <br>
</template>

<script setup>
import FinanceList from '../components/FinanceList.vue'
import { RouterLink, RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { useFinanceStore } from '../stores/finance'

const store = useFinanceStore()

onMounted(()=> {
    store.getProducts()
    console.log('onMount: FinancialListView.vue')
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>