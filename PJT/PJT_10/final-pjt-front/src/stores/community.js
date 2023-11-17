import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router/index.js'
import { useAuthStore } from '@/stores/auth.js'

export const useCommunityStore = defineStore('community', () => {
  const posts = ref([])
  const categories = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const authStore = useAuthStore()
  const token = authStore.token
  console.log(token)
  // post 정보 가져오기
  const getPosts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/posts/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {
      posts.value = res.data
      // console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
      console.log(token)
    
    })
  }

  // 카테고리 정보 받아오기 -> post 할 때 select option 으로 사용
  const getCategories = function () {
    axios({
      method: 'get',
      url: `${API_URL}/community/category/`,
      headers: {
        Authorization: `Token ${token}`
      }
    })
    .then(res => {
      categories.value = res.data
      console.log(res.data)
    })
    .catch(err => console.log(err))
  }

  

  return { 
    posts, 
    categories,
    API_URL, 
    getPosts,
    getCategories,
  }

}, { persist: true})
