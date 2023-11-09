<template>
    <div>
      <!-- Quiz 생성을 위한 Form -->
      <form @submit.prevent="handleSubmit">
        <!-- 문제 입력란 -->
        <label for="question">문제:</label>
        <textarea v-model="question" id="question" rows="4" cols="50"></textarea>
  
        <!-- 답안 입력란 -->
        <label for="answer">답안:</label>
        <input v-model="answer" type="text" id="answer" />
  
        <!-- 폼 제출 버튼 -->
        <button type="submit">퀴즈 생성</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits } from 'vue';
  
  const { updateQuiz } = defineProps(['updateQuiz']); // 부모 컴포넌트로부터 updateQuiz 속성을 받아옴
  const { emit } = defineEmits(); // 이벤트를 발생시키기 위한 emit 함수
  
  const question = ref(''); // 문제 입력값을 저장할 변수
  const answer = ref(''); // 답안 입력값을 저장할 변수
  
  const handleSubmit = () => {
    // 새로운 퀴즈 객체 생성
    const newQuiz = { question: question.value, answer: answer.value };
  
    // 부모 컴포넌트로 create-quiz 이벤트 발생
    emit('create-quiz', newQuiz);
  
    // 입력값 초기화
    question.value = '';
    answer.value = '';
  };
  </script>
  
  <style scoped>
  /* 필요한 스타일을 추가할 수 있습니다. */
  </style>
  