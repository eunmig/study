<template>
    <h1 class="title">금융 상품 목록</h1>
    <h3 class="subtitle">예적금 목록</h3>
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
    console.log('onMount: FinancialListView.vue')
})
</script>

<style>
@import "@/views/FinanceDetailView.scss"

</style>