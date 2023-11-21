<template>
  <div>
    <h3 class="title">상품 종류</h3>
    <table>
      <thead>
        <tr>
          <th>저장 기간</th>
          <th>이자율 종류</th>
          <th>이자율</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="option in options" :key="option.id">
          <td>{{ option.save_trm }}개월</td>
          <td>{{ option.intr_rate_type_nm }}</td>
          <td>{{ option.intr_rate }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>  
  <script setup>

  const props = defineProps(['options']);
  </script>
  
  <style>
  @import "@/components/KakaoMap.scss"

  </style>
  