<!-- BarChartComponent.vue -->
<script setup>
import { ref, defineProps, onMounted, watch } from 'vue'
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps(['likedProducts'])

const chartData = ref({
  labels: props.likedProducts,
  datasets: [{ data: [40, 20, 12] }]
})

const chartOptions = ref({
  responsive: true
})


// Watch for changes in the likedProducts prop
watch(() => props.likedProducts, (newVal) => {
  console.log('Liked Products Updated:', newVal)
})

</script>

<template>
  <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
</template>
