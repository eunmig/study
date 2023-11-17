<template>
    <div>
      <h3>예적금 목록</h3>
      <hr>
  
      <table>
        <colgroup>
          <col style="width: 300px;"> <!-- Adjust the width as needed -->
          <col style="width: 600px;"> <!-- Adjust the width as needed -->
          <col style="width: 150px;"> <!-- Adjust the width as needed -->
        </colgroup>
        <thead>
          <tr>
            <th>은행</th>
            <th>상품명</th>
            <th>공시 일자</th>
            <!-- Add more headers if needed -->
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
  