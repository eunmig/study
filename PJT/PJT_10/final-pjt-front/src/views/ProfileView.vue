<template>
  <!-- <div> -->
    <!-- <h3>username: {{ userData.username }}</h3>
    <div>
      <p>이름: 
        <input v-model="userData.last_name" placeholder="성" />
        <input v-model="userData.first_name" placeholder="이름" />
      </p>
      <p>이메일: <input v-model="userData.email" placeholder="abc@efg.com" /></p>
      <p>연봉: <input v-model="userData.salary" placeholder="-" /></p>
      <button @click="submitChanges">회원 정보만 수정</button> -->
  
  <div class="two alt-two">
    <h1>My Profile Page
        <span>   </span>
    </h1>
    <br>
  </div>

  <div class="profile-container">
    <hr>
    <h3>ID : {{ userData.username }}</h3>
    <div class="profile-form">
      <div class="form-field">
        <label for="last_name">이름: </label>
        <input v-model="userData.last_name" placeholder="성" id="last_name" class="input" />
        <input v-model="userData.first_name" placeholder="이름" class="input" />
      </div>

      <div class="form-field">
        <label for="email">E-mail: </label>
        <input v-model="userData.email" placeholder="abc@efg.com" id="email" class="input" />
      </div>

      <div class="form-field">
        <label for="salary">연봉: </label>
        <input v-model="userData.salary" placeholder="-" id="salary" class="input" />
      </div>    
      <hr>
      <br>

      <h2>내가 가입한 상품 목록</h2>
      <div>
        <button @click="toggleChart">그래프 열기</button>
        <div v-if="showChart">
          <Bar :data="chartData" :options="chartOptions"/>
        </div>
      </div>
        <div v-for="product in likedProducts" :key="product.fin_prdt_cd">
        <p>은행명: {{ product.kor_co_nm }}</p>
        <p>상품명: {{ product.fin_prdt_nm }}</p>

        <table>
          <thead>
            <tr>
              <th>기간</th>
              <th>저축금리</th>
              <th>최고우대금리</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="option in product.depositoptions_set" :key="option.id">
              <td>{{ option.save_trm }}개월</td>
              <td>{{ option.intr_rate }}</td>
              <td>{{ option.intr_rate2 }}</td>
            </tr>
          </tbody>
        </table>

        <hr>
        </div>
      <hr>
      <PasswordChangePopup />
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import PasswordChangePopup from '../components/PasswordChangePopup.vue'
import { useAuthStore } from '../stores/auth'
import { onMounted, ref, watch, computed } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const authStore = useAuthStore()
const userData = authStore.userData
const submitChanges = async () => {
  try {
    await axios({
      method: 'put',
      url: `${authStore.API_URL}/account/update_profile/${userData.id}/`,
      headers: {
        Authorization: `Token ${authStore.token}`
      },
      data: {
        last_name: userData.last_name || null,
        first_name: userData.first_name || null,
        email: userData.email || null,
        salary: userData.salary || null,
      }
    })
    // Optionally, you may want to update the user data in the store or take other actions upon successful submission.
  }
    catch (error) {
    console.error('Error updating profile:', error);
    // Handle error appropriately
  }
}

const likedProducts = ref([])

const get_likes = function () {
  axios({
    method: 'get',
    url: `${authStore.API_URL}/finance/liked_products/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  }).then((res) => {
    likedProducts.value = res.data
  })
  .catch(err => console.log(err))
}


onMounted(() => {
  get_likes()
  console.log('onMount: ProfileView', likedProducts)
})

const showChart = ref(false)
const chartOptions = ref({})
const chartData = ref({})

const toggleChart = () => {
  showChart.value = !showChart.value
  console.log(showChart.value)
  console.log('DATA', chartData)
  console.log('options', chartOptions)
}

// Watch for changes in showChart and fetch data when it becomes true
watch(showChart, (newVal) => {
  if (newVal) {
    updateChartData()
  }
})


const updateChartData = () => {
  chartData.value.active = true;

  chartData.value.labels = ' '

  chartData.value.datasets = likedProducts.value.flatMap((product, productIndex) =>
    product.depositoptions_set.flatMap((option, optionIndex) => {
      const randomColor = `rgba(${Math.random() * 255}, ${Math.random() * 255}, ${Math.random() * 255}, 0.5)`;

      const intrRateDataset = {
        label: `저축 ${product.fin_prdt_nm} ${option.save_trm}개월`,
        backgroundColor: randomColor,
        data: [option.intr_rate],
      };

      const intrRate2Dataset = {
        label: `최대 우대 ${product.fin_prdt_nm} ${option.save_trm}개월`,
        backgroundColor: randomColor,
        data: [option.intr_rate2]
      };

      return [intrRateDataset, intrRate2Dataset]
    })
  )

  chartOptions.value = {
    responsive: true,
    elements: {
      bar: {
        borderWidth: 1,
        borderColor: 'black',
      },
    },
  }
}

</script>


<style scoped>
@import "@/views/ProfileView.scss";

</style>