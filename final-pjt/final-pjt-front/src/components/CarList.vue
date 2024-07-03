<template>
    <div>
    <table>
        <colgroup>
        <col style="width: 250px;"> <!-- Adjust the width as needed -->
        <col style="width: 400px;"> <!-- Adjust the width as needed -->
        <col style="width: 150px;"> <!-- Adjust the width as needed -->
        </colgroup>
        <thead>
        <tr>
            <th>차량 종류</th>
            <th>금액대</th>
            <th>출시 연도</th>
        </tr>
        </thead>
    </table>

    <div v-if="showCar">
    <button @click="toggleCar">추천 차량</button>
        <CarRecommand
        v-for="car in myCar"
        :key="car.id"
        :car="car"
        />
    </div>

    <div v-else>
    <button @click="toggleCar">전체 차량</button>
        <CarRecommand
        v-for="car in allCar"
        :key="car.id"
        :car="car"
        />
    </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useAuthStore } from '../stores/auth'
import CarRecommand from '../components/CarRecommand.vue'
import axios from 'axios';

const authStore = useAuthStore()
const allCar = authStore.allCar
const myCar = ref([])
const user = authStore.userData

const toggleCar = () => {
    showCar.value = !showCar.value
    recMyCar()
}
const showCar = ref(false)
const recMyCar = function () {
    axios({
        method: 'get',
        url: `${authStore.API_URL}/account/my_cars/${user.salary_level}`,
        headers: {
            Authorization: `Token ${authStore.token}`
        }
    })
    .then((res) => {
        myCar.value = res.data
    })
    .catch(err => console.log(err))
}

onMounted(() => {
    authStore.getCar()
})
</script>

<style scoped>
button {
    height: 36px;
    margin-top: 10px;
    margin-left: 20px;
    padding: 0 15px;
    border: none;
    border-radius: 5px;
    background-color: #007BFF;
    color: #fff;
    cursor: pointer;
    font-size: 14px;
    transition: background-color 0.3s ease-in-out;
    margin-left: 0%;
}
</style>