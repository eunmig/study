<template>
    <div class="quiz-card">
      <p class="quiz-question">문제{{ pk }}번 : {{ question }}</p>
      <p style="font-size: small;">정답 입력</p>
      <input class="quiz-input" type="text" :id="`input-${pk}`">
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps } from 'vue'
  
  const { pk, question, answer } = defineProps({
    pk: Number,
    question: String,
    answer: String
  })
  
  </script>
  
  <style scoped>
  .quiz-card {
    text-align: left;
    width: 600px;
    padding: 20px; /* Add some padding to center the text vertically */
    border-radius: 10px;
    background-color: antiquewhite;
    border: solid 2px rgb(252, 162, 27);
    margin: 20px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1)
  }
  
  .quiz-question {
    font-weight: bold;
  }
  .quiz-input{
    width: 590px;
    height: 25px;
  }
  </style>