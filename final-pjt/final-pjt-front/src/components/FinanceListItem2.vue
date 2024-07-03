<template>
  <div>
    <div class="table-container">
      <table>
        <colgroup>
          <col style="width: 250px;">
          <col style="width: 400px;">
          <col style="width: 150px;">
          <col style="width: 350px;">
        </colgroup>
        <tbody>
          <tr>
            <td style="width: 250px;">{{ product.kor_co_nm }}</td>
            <td style="width: 400px;">
              <RouterLink :to="{ name: 'FinanceItemDetail2', params: { id: product.fin_prdt_cd } }">
                {{ product.fin_prdt_nm }}
              </RouterLink>
            </td>
            <td style="width: 150px;">{{ product.dcls_strt_day }}</td>
            <td style="width: 350px;">
              <div v-for="option in product.savingoptions_set">
                {{ option.intr_rate }} / {{ option.save_trm }}
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({ product: Object });

</script>

<style>
@import "@/components/FinanceListItem.scss"

</style>
