<template>
    <div>
        <h1>부모 페이지입니다.</h1>
        <ChildPage :children="children" @givemeAllowance="updateBalance"/>
    </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';
import { ref } from 'vue';

const children = ref([
    {name : '김하나', age : 30, balance : 100000},
    {name : '김두리', age : 20, balance : 10000},
    {name : '김서이', age : 10, balance : 1000},
])

const updateBalance = (childToUpdate) => {
    // children 배열에서 해당 자식을 찾음
    const child = children.value.find((child) => child.name === childToUpdate.name)

    if (child) {
        // 찾은 자식의 balance를 1000원 씩 증가시킴
        child.balance += 1000
    }
}</script>

<style scoped>
</style>

