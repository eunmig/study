<!-- OptionDetail.vue -->
<template>
    <div>
      <h3>상품 종류</h3>
      <ul>
        <li v-for="option in options" :key="option.id">
          {{ option.save_trm }}개월 - {{ option.intr_rate_type_nm }} - {{ option.intr_rate }}
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>

  const props = defineProps(['options']);
  </script>
  
  <style scoped>

  </style>
  