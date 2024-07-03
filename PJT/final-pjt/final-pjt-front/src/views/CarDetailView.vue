<template>
    <div>
      <div v-if="carInfo" class="car-info-container">
        <h1 class="car-title">{{ carInfo.car_name }}</h1>
        <img :src="imageroute" alt="아직 준비되지 않았습니다" class="car-image">
        <h2 class="car-price">{{ carInfo.price }}만원</h2>
        <p>출시 연도: {{ carInfo.year }}</p>
        <p>나의 연봉: {{ user.salary }}</p>
      </div>
      <div v-else>
        <p>Loading...</p>
      </div>
    </div>
    <hr>
      <h2>추천 예금</h2>
      <table>
        <thead>
          <tr>
            <th>은행명</th>
            <th>상품이름</th>
            <th>최고 우대 금리</th>
            <th>기간</th>

          </tr>
        </thead>
        <tbody>
          <tr v-for="(recommendation, index) in bestProduct.recommendations" :key="index">
            <td>{{ recommendation.deposit_product.kor_co_nm }}</td>
            <td>              
                <RouterLink :to="{ name: 'FinanceItemDetail', params: { id: recommendation.deposit_product.fin_prdt_cd } }">
                {{ recommendation.deposit_product.fin_prdt_nm }}
                 </RouterLink>
            </td>
            <td>{{ recommendation.options.intr_rate }}%</td>
            <td>{{ recommendation.options.save_trm }} 개월</td>
  
          </tr>
        </tbody>
      </table>
      <hr>
      <h2>추천 적금</h2>
      <div class="input-box">
        <label for="monthlyInvestment">고정 적금 금액: </label>
        <input v-model="monthlyInvestment" type="number" id="monthlyInvestment" />
      </div>
      <table>
        <thead>
          <tr>
            <th>은행명</th>
            <th>상품이름</th>
            <th>최고 우대 금리</th>
            <th>기간</th>
            <th>예상 최대 금액</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(recommendation, index) in bestSaving.recommendations" :key="index">
            <td>{{ recommendation.deposit_product.kor_co_nm }}</td>
            <td>              
                <RouterLink :to="{ name: 'FinanceItemDetail2', params: { id: recommendation.deposit_product.fin_prdt_cd } }">
                {{ recommendation.deposit_product.fin_prdt_nm }}
                 </RouterLink>
            </td>
            <td>{{ recommendation.options.intr_rate }}%</td>
            <td>{{ recommendation.options.save_trm }} 개월</td>
            <td>{{ calculateEarning(recommendation.options.save_trm, recommendation.options.intr_rate) }}만원</td>
          </tr>
        </tbody>
      </table>

</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, computed } from 'vue'
import { useAuthStore } from '../stores/auth'
import { useRoute } from 'vue-router'
import { RouterLink } from 'vue-router'

const authStore = useAuthStore()
const user = authStore.userData
const route = useRoute()

const carInfo = ref([])
const imageroute = computed(() => `../src/assets/${carInfo.value.car_name}.png`)

const oneCar = function() {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/account/car/${route.params.car_pk}`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
        carInfo.value = res.data
    })
    .catch(err => console.log(err))
}

const bestProduct = ref([])
const recProducts = function() {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/finance/deposit-products/top_rate/`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
        bestProduct.value = res.data
        recSaving()
    })
    .catch(err => console.log(err))
}

const bestSaving = ref([])
const recSaving = function() {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/finance/saving-products/top_rate/`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
      bestSaving.value = res.data
    })
    .catch(err => console.log(err))
}

const monthlyInvestment = ref(100);

const calculateEarning = (saveTrm, intrRate) => {
  const monthlyPay = monthlyInvestment.value || 100;
  const originalMoney = monthlyPay * saveTrm;
  const intrMoney = originalMoney * (intrRate / 100);
  const finalResult = (originalMoney + intrMoney) - intrMoney * 0.154;
  return finalResult.toFixed(2); // Adjust the number of decimal places as needed
}
onMounted(() => {
    oneCar()
    recProducts()
})

</script>

<style scoped>
@import "@/views/CarDetailView.scss"

</style>