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
      component: LogInView
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
    }

  ]
})

export default router
