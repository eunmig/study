<template>
  <div>
  <table>
    <colgroup>
      <col style="width: 250px;">
      <col style="width: 400px;">
      <col style="width: 150px;">
      <col style="width: 350px;">
    </colgroup>
    <thead>
      <tr>
        <th>은행</th>
        <th>상품명</th>
        <th>공시 일자</th>
        <th>저축금리 / 저축 기간</th>
      </tr>
    </thead>

  </table>
    <FinanceListItem
        v-for="product in store.products"
        :key="product.fin_prdt_cd"
        :product="product"
    />
  </div>
</template>
  
<script setup>
import FinanceListItem from './FinanceListItem.vue';
import { useFinanceStore } from '@/stores/finance'

const store = useFinanceStore()

// console.log(store.products)
</script>

<style>

</style>
  