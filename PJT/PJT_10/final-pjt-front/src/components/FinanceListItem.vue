<template>
  <div>
    <div class="table-container">
      <table>
        <colgroup>
          <col style="width: 300px;">
          <col style="width: 600px;">
          <col style="width: 150px;">
        </colgroup>
        <tbody>
          <tr>
            
            <td>{{ product.kor_co_nm }}</td>
            <td>
              <RouterLink :to="{ name: 'FinanceItemDetail', params: { id: product.fin_prdt_cd } }">
                {{ product.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td>{{ product.dcls_strt_day }}</td>

          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
console.log('여기까진 잘나옴')

defineProps({ product: Object });
</script>

<style scoped>
.table-container {
  width: 100%;
  margin: 0 auto;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: auto;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>
