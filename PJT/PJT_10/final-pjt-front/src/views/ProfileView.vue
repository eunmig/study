<template>
  <div>
    <h3>username: {{ userData.username }}</h3>
    <div>
      <p>이름: 
        <input v-model="userData.last_name" placeholder="성" />
        <input v-model="userData.first_name" placeholder="이름" />
      </p>
      <p>이메일: <input v-model="userData.email" placeholder="abc@efg.com" /></p>
      <p>연봉: <input v-model="userData.salary" placeholder="-" /></p>
      <button @click="submitChanges">회원 정보만 수정</button>
      <hr>
      <h2>내가 가입한 상품 목록</h2>
      <div v-for="product in liked_products" :key="product.fin_prdt_cd">
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
import { onMounted, ref } from 'vue'

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

const liked_products = ref([])

const get_likes = function () {
  axios({
    method: 'get',
    url: `${authStore.API_URL}/finance/liked_products/`,
    headers: {
      Authorization: `Token ${authStore.token}`
    }
  }).then((res) => {
    liked_products.value = res.data
  })
  .catch(err => console.log(err))
}


onMounted(() => {
  get_likes()
  console.log('onMount: ProfileView', liked_products)
})
</script>

<style scoped>
/* Add your styles if needed */
</style>
