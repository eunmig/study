<template>
    <div>
        <h1>학생 상세 정보 목록 입니다.</h1>
        <div v-for="student in students" :key="student.name">
            <p @click="goToStudentDetail(student.name)">{{ student.name }} 상세 정보 보기</p>        
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const students = [
    { name : '김하나' },
    { name : '김두리' },
    { name : '김서이' },
]

const router = useRouter()

// router/index.js/ 의 name과 동일하게 작성해야 동작
const goToStudentDetail = (studentName) => {
  router.push({ name: 'studentDetail', params: { name: studentName } })
}
</script>

<style scoped>

</style>