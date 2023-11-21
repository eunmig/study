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
      <PasswordChangePopup />

    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import PasswordChangePopup from '../components/PasswordChangePopup.vue'
import { useAuthStore } from '../stores/auth'
import { ref } from 'vue'

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
</script>

<style scoped>
/* Add your styles if needed */
</style>
