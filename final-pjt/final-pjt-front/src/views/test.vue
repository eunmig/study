<template>
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>예적금 목록</span>
        </h1>
        <br>
    </div>
    <div>
        
        <h2>적금</h2>
    <FinanceList2/>
    </div>

    <br>

</template>

<script setup>

import FinanceList2 from '../components/FinanceList2.vue'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '../stores/finance'

const store = useFinanceStore()


onMounted(()=> {
    store.getSavingsProducts()
    console.log('onMount: FinancialListView.vue')
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>