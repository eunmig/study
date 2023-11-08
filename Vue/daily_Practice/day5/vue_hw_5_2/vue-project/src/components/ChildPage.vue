<template>
    <div  v-for="child in children" :key="child.name">
        <h3>자식 페이지입니다.</h3>
        <p>이름 : {{ child.name }}</p>
        <p>나이 : {{ child.age }}</p>
    </div>
</template>

<script setup>
import { ref, defineProps } from 'vue'

const props = defineProps({
    children : Array
})
</script>

<style scoped>
div {
    border: 1px solid;
    margin: 10px;
    padding: 10px;
}
</style>