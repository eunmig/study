<template>
    <div class="two alt-two">
        <h1>금융 아이템 목록 페이지
            <span>예금 목록</span>
        </h1>
        <br>
    </div>
    <div>
    <span class="link2">예금 리스트</span>
    <RouterLink class="link" :to="{ name:'FinanceItems2' }">적금 리스트</RouterLink> 
    </div>  
    <FinanceList/>

    <br>

</template>

<script setup>
import FinanceList from '../components/FinanceList.vue'
import FinanceList2 from '../components/FinanceList2.vue'
import { onMounted, ref } from 'vue'
import { useFinanceStore } from '../stores/finance'
import { RouterLink } from 'vue-router'


const store = useFinanceStore()


onMounted(()=> {
    store.getProducts()
    console.log('onMount: FinancialListView.vue')
})
</script>

<style scoped>
@import "@/views/FinanceListView.scss"

</style>