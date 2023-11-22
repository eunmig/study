<template>
  <div>
    <div class="bankSelect">
      <label for="bankSelect">은행: </label>
      <select id="bankSelect" v-model="selectedBank" class="pl">
        <option value="">-- 선택 안함 --</option>
        <option v-for="bank in uniqueBanks" :key="bank" :value="bank">
          {{ bank }}
        </option>
      </select>
    </div>
    
  <table>
    <colgroup>
      <col style="width: 250px;"> <!-- Adjust the width as needed -->
      <col style="width: 400px;"> <!-- Adjust the width as needed -->
      <col style="width: 150px;"> <!-- Adjust the width as needed -->
      <col style="width: 350px;"> <!-- Adjust the width as needed -->
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
    v-for="product in filteredProducts"
    :key="product.fin_prdt_cd"
    :product="product"
    />
  </div>
</template>
  
<script setup>
import FinanceListItem from './FinanceListItem.vue'
import { useFinanceStore } from '@/stores/finance'
import { computed, ref } from 'vue'

const store = useFinanceStore()

// Computed property to get unique bank names from products
const uniqueBanks = computed(() => {
  const banks = new Set()
  store.products.forEach((product) => {
    banks.add(product.kor_co_nm)
  })
  return Array.from(banks)
})

// Reactive variable to store the selected bank for filtering
const selectedBank = ref('')

// Computed property to filter products based on the selected bank
const filteredProducts = computed(() => {
  if (!selectedBank.value) {
    return store.products
  }
  return store.products.filter((product) => product.kor_co_nm === selectedBank.value)
})
</script>

<style>
@import "@/components/FinanceList.scss"

</style>
  