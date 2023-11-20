<template>
  <div class="login-container">
    <div class="image-container">
      <img src="@/assets/login.png" alt="login" />
    </div>

    <div class="form-container">
      <form action="/login" method="post">
        <div class="form-field">
          <label for="username">ID : </label>
          <input type="text" id="username" name="username" v-model.trim="username" class="input" />
        </div>

        <div class="form-field">
          <label for="password">비밀번호: </label>
          <input type="password" name="password" v-model.trim="password" class="input" />
        </div>

        <div class="submit-button">
          <button @click.prevent="login">로그인</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '../stores/auth'

const store = useAuthStore()

const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  console.log(payload)
  store.logIn(payload)
}
</script>

<style lang="scss">
@import "@/views/LogInView.scss"

</style>
