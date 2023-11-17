import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DetailView from '../views/DetailView.vue'
import LaterViewView from '../views/LaterView.vue'
import SearchViewView from '../views/SearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/detail/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/later',
      name: 'later',
      component: LaterViewView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchViewView
    },
  ]
})

export default router
