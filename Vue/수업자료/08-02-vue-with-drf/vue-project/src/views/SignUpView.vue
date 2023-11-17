<template>
  <div>
    <h1>Sing Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username"><br>

      <label for="password1">password : </label>
      <input type="password" name="password1" v-model.trim="password1"><br>

      <label for="password2">password confirmation : </label>
      <input type="password" name="password2" v-model.trim="password2">

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const store = useCounterStore()
// 컴포넌트에 사용자 입력 데이터를 저장 후 store의 singUp 함수를 호출하는 함수 작성
const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style>

</style>
