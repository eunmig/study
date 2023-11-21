<template>
    <div>
      <h1>Currency Converter</h1>
      <div v-if="currencies.length"> 
        <div>
          <label for="targetCurrency">Target Currency:</label>
          <select v-model="targetCurrency" id="targetCurrency">
            <option v-for="currency in currencies" :key="currency.id" :value="currency.id">
              {{ currency.korean_name }} ({{ currency.country }})
            </option>
          </select>
        </div>
  
        <div>
          <label for="otherAmount">{{ targetCurrencyLabel }}:</label>
          <input v-model="otherAmount" type="number" :id="otherAmountId" @input="convertCurrency(currencies.find(c => c.id === targetCurrency).currency_name)" />
        </div>

        <div>
          <label for="krwAmount">KRW:</label>
          <input v-model="krwAmount" type="number" id="krwAmount" @input="convertCurrency('KRW')" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue'
  import axios from 'axios'
  import { useCommunityStore } from '@/stores/community'
  import { useAuthStore } from '@/stores/auth'
  
  const authStore = useAuthStore()
  const store = useCommunityStore()
  const token = authStore.token
  const currencies = ref([])
  const krwAmount = ref(1)
  const targetCurrency = ref(null)
  const otherAmount = ref(null)
  const otherAmountId = ref('otherAmount')
  const targetCurrencyLabel = ref(null)
  
  const updateOtherAmountLabel = () => {
    const selectedCurrency = currencies.value.find((c) => c.id === targetCurrency.value)
    if (selectedCurrency) {
      otherAmountId.value = `otherAmount${selectedCurrency.country}`
      targetCurrencyLabel.value = selectedCurrency.country
    }
  }
  
  const resetValues = () => {
    krwAmount.value = 1
    otherAmount.value = null
  };
  
  const convertCurrency = (baseCurrency) => {
    if (targetCurrency.value) {
      const toCurrency = currencies.value.find((c) => c.id === targetCurrency.value)
      if (toCurrency) {
        const toRate = toCurrency.rate
  
        if (baseCurrency === 'KRW') {
          otherAmount.value = (parseFloat(krwAmount.value) * toRate).toFixed(2)
        } else {
          krwAmount.value = (parseFloat(otherAmount.value) / toRate).toFixed(2)
        }
      } else {
        console.error(`Currency not found for targetCurrency: ${targetCurrency.value}`)
      }
    }
  }
  
  onMounted(() => {
    axios({
      method: 'get',
      url: `${store.API_URL}/exchange/get/`,
      headers: {
        Authorization: `Token ${token}`,
      },
    })
      .then((res) => {
        currencies.value = res.data;
        targetCurrency.value = res.data.find((currency) => currency.country === 'KRW').id
        convertCurrency()
        updateOtherAmountLabel()
      })
      .catch((error) => {
        console.error('Error fetching currencies:', error)
      })
  })
  
  watch(() => targetCurrency.value, () => {
    resetValues()
    updateOtherAmountLabel()
    convertCurrency()
  })
  </script>
  
  
  <style scoped>

  </style>
  