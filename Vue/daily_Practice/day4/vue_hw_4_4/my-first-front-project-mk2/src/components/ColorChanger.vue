<template>
    <div>
        <!-- v-model -> 양방향, class -> 단방향 -->
        <input v-model="colorClass" @input="updateColor">
        <p :class="colorClass"> {{ message }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const colorClass = ref('')
const message = ref('입력창에 올바른 색상 명을 입력하면 글자색이 바껴요')

function undateColor() {
    if (colorClass.value === 'red' || colorClass.value === 'blue' || colorClass.value === 'green') {
        message.value = ""
    }
}
</script>

<style scoped>
.red {
    color: red;
}

.blue {
    color: blue;
}

.green {
    color: green;
}
</style>