<template>
    <h1>{{ item.fin_prdt_nm }}</h1>
    <p>{{ item.kor_co_nm }}</p>
    <p v-html="formattedEtcNote"></p>
    <OptionList :options="itemOption" />
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { useFinanceStore } from '../stores/finance'
import { useAuthStore } from '../stores/auth'
import router from '../router'
import OptionList from '../components/OptionList.vue'


const authStore = useAuthStore()
const token = authStore.token
const financeStore = useFinanceStore()
const route = useRoute()
const itemOption = ref([])
const item = ref(null)


const formattedEtcNote = computed(() => {
  // Replace newline characters with <br> tags
  return item.value?.etc_note ? item.value.etc_note.replace(/\n/g, '<br>') : ''
})

onMounted(() => {
  axios({
    method: 'get',
    url: `${financeStore.API_URL}/finance/deposit-product-options/${route.params.id}/`,
    headers: {
      Authorization: `Token ${token}`
    }
  })
  .then((res) => {
    itemOption.value = res.data
    console.log('상품 옵션 res', res.data)
  })
  .catch(err => {
    console.log(err)
  })

  axios({
    method: 'get',
    url: `${financeStore.API_URL}/finance/deposit-product/${route.params.id}/`,
    headers: {
      Authorization: `Token ${token}`
    }
  })
  .then((res) => {
    item.value = res.data
    console.log('금융상품 res', res.data)
  })
  .catch(err => {
    console.log(err)
  })
})

</script>

<style scoped>

</style>