<!-- <template>
    <div  v-for="child in children" :key="child.name">
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ child.name }}</p>
        <p>나이 : {{ child.age }}</p>
        <p>용돈 : {{ child.balance }}</p>
        <button @click="givemeAllowance">용돈 주세요.</button>
    </div>
</template>

<script setup>
// defineEmits()를 사용하여 명시적으로 발신한 이벤트 선언
// script에서 $emit 메서드를 접근할 수 없기 때문
import { ref, defineProps, defineEmits } from 'vue'

const props = defineProps({
    children : Array,
    name : String,
    age : Number,
    balance : Number
})

const emit = defineEmits(['givemeAllowance'])

const givemeallowance = (child) => {
    // 이벤트를 발생시켜서 부모 컴포넌트에서 처리하도록 함
    emit('givemeAllowance', child)
}
</script>


<style scoped>

</style> -->

<template>
    <div v-for="child in children" :key="child.name">
      <h3>자식 페이지입니다.</h3>
      <p>이름: {{ child.name }}</p>
      <p>나이: {{ child.age }}</p>
      <p>용돈: {{ child.balance }}</p>
      <button @click="givemeAllowance(child)">용돈 주세요.</button>
    </div>
  </template>
  
  <script setup>
  import { ref, defineProps, defineEmits } from 'vue'
  
  const props = defineProps({
    children: Array,
  })
  
  const emit = defineEmits(['givemeAllowance'])
  
  const givemeAllowance = (child) => {
    // 이벤트를 발생시켜서 부모 컴포넌트에서 처리하도록 함
    emit('givemeAllowance', child)
  }
  </script>
  
  <style scoped>
  </style>