import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import CreatePostView from '@/views/CreatePostView.vue'
import PostListView from '@/views/PostListView.vue'
import DetailView from '@/views/DetailView.vue'
import FinanceListView from '@/views/FinanceListView.vue'
import FinanceDetailView from '@/views/FinanceDetailView.vue'
import BankView from '@/views/BankView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import EditPostView from '@/views/EditPostView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/signup',
      name: 'SignUp',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogIn',
      component: LogInView,
    },
    {
      path: '/posts',
      name: 'Post',
      component: PostListView
    },
    {
      path: '/post/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/createPost',
      name: 'CreatePost',
      component: CreatePostView
    },
    {
      path: '/financeList',
      name: 'FinanceItems',
      component: FinanceListView
    },
    {
      path: '/financeItem/:id',
      name: 'FinanceItemDetail',
      component: FinanceDetailView
    },
    {
      path: '/bank',
      name: 'Bank',
      component: BankView
    },
    {
      path: '/exchange',
      name: 'Exchange',
      component: ExchangeView
    },
    {
      path: '/profile',
      name: 'Profile',
      component: ProfileView
    },
    {
      path: '/edit_post/:post_pk',
      name: 'EditPost',
      component: EditPostView
    },
  ]
})
router.beforeEach((to, from, next) => {
  // Check authentication status dynamically (replace this with your actual authentication logic)
  const isAuthenticated = checkAuthentication()

  // Routes that do not require authentication
  const publicRoutes = ['LogIn', 'SignUp']

  if (!isAuthenticated && !publicRoutes.includes(to.name)) {
    console.log('로그인이 필요합니다.')
    window.alert('로그인이 필요합니다')
    next({ name: 'LogIn' })
  } else if (isAuthenticated && to.name === 'LogIn') {
    console.log('이미 로그인되어 있습니다.')
    next({ name: 'Home' })
  } else {
    next()
  }
})


function checkAuthentication() {
  // Check if the 'auth' key exists in localStorage
  const authData = localStorage.getItem('auth');

  // Parse the JSON data, and check if 'token' property exists
  const isAuthenticated = authData ? JSON.parse(authData).token : null;

  // Return true if the 'token' property exists, indicating the user is authenticated
  return !!isAuthenticated
}

export default router
