import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'
import { useAuthStore } from '@/stores/auth.js'


export const useFinanceStore = defineStore('finance', () => {
    const products = ref([])
    const savings = ref([])
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

    const getSavingsProducts = function() {
        axios({
            method: 'get',
            url: `${API_URL}/finance/saving-products/`,
            headers: {
                Authorization: `Token ${token}`
            }
        }).then(res => {
            savings.value = res.data
            console.log('savings', savings)
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
        getSavingsProducts,
        saveDeposits,
        API_URL,
        products,
        savings,
    }
}, { persist: true})