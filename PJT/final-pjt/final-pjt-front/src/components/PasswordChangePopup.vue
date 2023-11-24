<template>
  <div>
    <div class="popup-content">
      <br>
      <h2>비밀번호 변경하기</h2>
      <br>

      <form @submit.prevent="changePW">
        <label for="new_password1">New Password : </label>
        <input v-model="newPassword1" type="password" id="new_password1" name="new_password1" required>
        <br>
        <label for="new_password2">Confirm Password : </label>
        <input v-model="newPassword2" type="password" id="new_password2" name="new_password2" required>
        
        <!-- Display error messages if passwords don't match or other validation issues -->
        <div v-if="passwordsDoNotMatch">Passwords do not match</div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'
import axios from 'axios'

const newPassword1 = ref('')
const newPassword2 = ref('')
const passwordsDoNotMatch = ref(false)

const authStore = useAuthStore()
const token = authStore.token

const changePW = function () {
  if (newPassword1.value !== newPassword2.value) {
    passwordsDoNotMatch.value = true
    return
  }

  axios({
    method: 'post',
    url: `${authStore.API_URL}/accounts/password/change/`,
    headers: {
      Authorization: `Token ${token}`,
    },
    data: {
      new_password1: newPassword1.value,
      new_password2: newPassword2.value,
    },
  })
    .then((res) => {
      // Handle success, e.g., show a success message
      console.log('Password changed successfully')
      window.alert('새로운 비밀번호로 다시 로그인 해주세요')
      authStore.logOut()
    })
    .catch((err) => {
      // Handle errors, e.g., show an error message to the user
      console.error('Error changing password', err)
    })
}
</script>

<style scoped>
@import "@/components/PasswordChangePopup.scss"

</style>
