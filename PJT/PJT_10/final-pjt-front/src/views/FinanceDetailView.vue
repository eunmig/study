<template>
  <h1 class="title">{{ item?.fin_prdt_nm }}</h1>
  <br>
  <h4 class="subtitle">{{ item?.kor_co_nm }}</h4>
  <br>
  <div>
    <table>
      <thead>
        <tr>
          <th>상품명</th>
          <th>은행명</th>
          <th>상품 설명</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{{ item?.fin_prdt_nm }}</td>
          <td>{{ item?.kor_co_nm }}</td>
          <td v-html="formattedEtcNote"></td>
        </tr>
        <br>
        <tr>
          <td colspan="3">
            <!-- 추가된 행에 OptionList 컴포넌트 추가 -->
            <OptionList :options="itemOption" />
          </td>
        </tr>
      </tbody>
    </table>
    <br>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useFinanceStore } from '../stores/finance';
import { useAuthStore } from '../stores/auth';
import OptionList from '../components/OptionList.vue';

const authStore = useAuthStore();
const token = authStore.token;
const financeStore = useFinanceStore();
const route = useRoute();
const router = useRouter();
const itemOption = ref([]);
const item = ref(null);
console.log('item', item)

const formattedEtcNote = computed(() => {
  return item.value?.etc_note ? item.value.etc_note.replace(/\n/g, '<br>') : '';
});

const fetchData = async () => {
  try {
    const optionsResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    itemOption.value = optionsResponse.data
    console.log('상품 옵션 res', optionsResponse.data)

    const productResponse = await axios.get(`${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${token}`
      }
    })
    item.value = productResponse.data;
    console.log('금융상품 res', productResponse.data)
  } catch (error) {
    console.error(error)
  }
}

onMounted(() => {
  fetchData()
  console.log('onMount: FinanceDetailView')
})


</script>


<style scoped>
@import "@/views/FinanceListView.scss"

</style>