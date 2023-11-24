<template>
  <div class="two alt-two">
    <h1>My Profile Page</h1>
    <br>
  </div>

  <div class="profile-container">
    <hr>
    <h3>ID : {{ userData.username }}</h3>
    <div class="profile-form">
      <form action=""></form>
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
      <button @click="submitChanges">회원 정보 수정</button>
      <button class="password-pop" @click="togglePopup">비밀번호 변경</button>   

      <div v-if="popup">
        <PasswordChangePopup/>
      </div>

      <hr>
      <h2>내가 가입한 상품 목록</h2>
      <div>
        <h3>예금</h3>
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

        <div>
          <h3>적금</h3>
          <button @click="toggleChart2">그래프 열기</button>
          <div v-if="showChart2">
            <Bar :data="chartData2" :options="chartOptions2"/>
          </div>
        </div>
        <div v-for="product in likedSavings" :key="product.fin_prdt_cd">
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
              <tr v-for="option in product.savingoptions_set" :key="option.id">
                <td>{{ option.save_trm }}개월</td>
                <td>{{ option.intr_rate }}</td>
                <td>{{ option.intr_rate2 }}</td>
              </tr>
            </tbody>
          </table>
  
          <hr>
        </div>
    </div>

    <RouterLink class="button" :to="{ name : 'Car' }" >
      추천 차량 보러가기
      </RouterLink> 

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


// 회원정보 수정
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
    window.alert('정보 수정이 완료 되었습니다.')
  }
    catch (error) {
    console.error('Error updating profile:', error);
  }
}


// 비밀번호 변경 숨기기/띄우기
const togglePopup = function() {
  popup.value = !popup.value
}
const popup = ref(false)


// 좋아요 예금 상품 가져오기
const likedProducts = ref([])
const get_likes_D = function () {
  axios({
    method: 'get',
    url: `${authStore.API_URL}/finance/liked-products/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  }).then((res) => {
    get_likes_S()
    likedProducts.value = res.data
    console.log('D 완료')
  })
  .catch(err => console.log(err))
}

//좋아요 적금 상품 가져오기
const likedSavings = ref([])

const get_likes_S = function () {
  axios({
    method: 'get',
    url: `${authStore.API_URL}/finance/liked-saving/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  }).then((res) => {
    likedSavings.value = res.data
    console.log(likedSavings)
  })
  .catch(err => console.log(err))
}

onMounted(() => {
  get_likes_D()
  console.log('onMount: ProfileView', likedProducts)
})


// 차트 관련 코드
const showChart = ref(false)
const chartOptions = ref({})
const chartData = ref({})

const toggleChart = () => {
  showChart.value = !showChart.value
  console.log(showChart.value)
  console.log('DATA', chartData)
  console.log('options', chartOptions)
}


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

//차트2
const showChart2 = ref(false)
const chartOptions2 = ref({})
const chartData2 = ref({})

const toggleChart2 = () => {
  showChart2.value = !showChart2.value
  console.log(showChart2.value)
  console.log('DATA', chartData2)
  console.log('options', chartOptions2)
}

// Watch for changes in showChart and fetch data when it becomes true
watch(showChart2, (newVal) => {
  if (newVal) {
    updateChartData2()
  }
})


const updateChartData2 = () => {
  chartData2.value.active = true;

  chartData2.value.labels = ' '

  chartData2.value.datasets = likedSavings.value.flatMap((product, productIndex) =>
    product.savingoptions_set.flatMap((option, optionIndex) => {
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