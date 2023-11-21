import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'
import { useAuthStore } from '@/stores/auth.js'


export const useFinanceStore = defineStore('finance', () => {
    const products = ref([])
    const API_URL = 'http://127.0.0.1:8000'
    const authStore = useAuthStore()
    const token = authStore.token

    const getProducts = function() {
        axios({
            method: 'get',
            url: `${API_URL}/finance/deposit-products/`,
            headers: {
                Authorization: `Token ${token}`
            }
        }).then(res => {
            products.value = res.data
        }).catch(err => console.log(err))

    }
    
    const saveDeposits = function() {
        axios({
            method: 'get',
            url: `${API_URL}/finance/save-deposit-products/`
        })
        .then(res => {
            getProducts()
        })
        .catch(err => console.log(err))
    }

    return {
        getProducts,
        saveDeposits,
        API_URL,
        products,
    }
}, { persist: true})