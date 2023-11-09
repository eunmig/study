<template>
    <div>
      <h1>Quiz!</h1>
      <div>
        <QuizDetail
        v-for="(quiz, pk) in quizData"
        :key="pk"
        :pk="quiz.pk"
        :question="quiz.question"
        :answer="quiz.answer"
        />
  
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import QuizDetail from './QuizDetail.vue'
  
  
  const quizData = ref([
    {pk: 1, question:'정답은 flask', answer:'flask'},
    {pk: 2, question:'정답은 input', answer:'input'},
    {pk: 3, question:'정답은 post', answer:'post'},
    {pk: 4, question:'정답은 virtualenv', answer:'virtualenv'},
    {pk: 5, question:'정답은 html', answer:'html'},
  
  ])
  
  const router = useRouter()
  
  </script>
  
  <style lang="scss" scoped>
  
  </style>