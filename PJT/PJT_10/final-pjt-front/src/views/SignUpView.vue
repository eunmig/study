<template>
  <div class="signup-container">
    <div class="image-container">
      <img src="@/assets/signup.png" alt="signup" />
    </div>

    <div class="form-container">
      <form action="/sign-up" method="post">
        <div class="form-field">
          <label for="username">ID : </label>
          <input type="text" id="username" name="username" v-model.trim="username" class="input" />
        </div>

        <div class="form-field">
          <label for="email">email : </label>
          <input type="text" id="email" name="email" v-model.trim="email" class="input" />
        </div>

        <div class="form-field">
          <label for="password1">비밀번호: </label>
          <input type="password" name="password1" v-model.trim="password1" class="input" />
        </div>

        <div class="form-field">
          <label for="password2">비밀번호 확인: </label>
          <input type="password" name="password2" v-model.trim="password2" class="input" />
        </div>

        <div class="form-field">
          <label for="salary">연봉: </label>
          <input type="number" name="salary" v-model.trim="salary" class="input" />
        </div>

        <div class="submit-button">
          <button @click.prevent="signUp">가입하기</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const store = useAuthStore()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const salary = ref(null)

const signUp = function() {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    salary: salary.value
  }
  console.log(payload)
  store.signUp(payload)
}
</script>

<style lang="scss">
@import "@/views/SignUpView.scss"

</style>
