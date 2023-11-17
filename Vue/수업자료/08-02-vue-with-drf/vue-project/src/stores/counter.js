import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  // 반응형 변수 선언
  const token = ref(null) 


  // DRF에 article 조회 요청을 보내는 action
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      // token 추가
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) =>{
        // console.log(res)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }


  // 실제 로그인 요청을 보내는 store의 logIn 함수 작성
  const logIn = function (payload) {
    const username = payload.username
    const password = payload.password

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then(res => {
      console.log('로그인이 완료되었습니다.')
      console.log(res.data)
      // 토큰저장
      token.value = res.data.key
      // 로그인 성공 후 자동으로 메인페이지로 이동
      router.push({ name: 'ArticleView' })
    })
    .catch(err => console.log(err))
  }

  // token 여부에 따라 로그인 상태를 boolean 값으로 나타낼 변수
  // computed를 활용해 token 값이 변할 때만 계산
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
