<template>
    <div>
      <h1>Sign Up</h1>
      <form @submit.prevent="signUp">
        <label for="username">ID : </label>
        <input type="text" id="username" v-model.trim="username"><br>
  
        <label for="email">email : </label>
        <input type="text" id="email" v-model.trim="email"><br>

        <label for="password1">비밀번호: </label>
        <input type="password" name="password1" v-model.trim="password1"><br>
  
        <label for="password2">비밀번호 확인: </label>
        <input type="password" name="password2" v-model.trim="password2"><br>
 
        <label for="salary">연봉: </label>
        <input type="number" name="salary" v-model.trim="salary"><br>

        <input type="submit" value="SignUp">
      </form>
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
  
  <style>
  
  </style>
  