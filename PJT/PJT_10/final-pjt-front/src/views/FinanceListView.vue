<template>
    <div>
        <h1>금융 아이템 목록 페이지</h1>
        <hr>
        <FinanceList/>
    </div>
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

</style>