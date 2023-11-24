<template>
  <div>
    <div class="table-container">
      <table>
        <colgroup>
          <col style="width: 250px;">
          <col style="width: 400px;">
          <col style="width: 150px;">
        </colgroup>
        <tbody>
          <tr>
            <td style="width: 250px;">
                <RouterLink :to="{ name: 'CarDetail', params: { car_pk: car.id } }">
                    {{ car.car_name }}
                </RouterLink>
            </td>
            <td style="width: 400px;">{{ car.price }}만원</td>
            <td style="width: 150px;">{{ car.year }}</td>

          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({ car: Object})
</script>

<style scoped>

</style>