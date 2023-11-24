<template>
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>적금 목록</span>
        </h1>
        <br>
    </div>
    <div>
    <RouterLink class="link" :to="{ name:'FinanceItems' }">예금 리스트</RouterLink> 
    <span class="link2">적금 리스트</span>
    
    </div>  
    <FinanceList2/>
    <br>

</template>

<script setup>
import FinanceList2 from '../components/FinanceList2.vue'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '../stores/finance'
import { RouterLink } from 'vue-router'
const store = useFinanceStore()


onMounted(()=> {
    store.getSavingsProducts()
    console.log('onMount: FinancialListView.vue')
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>