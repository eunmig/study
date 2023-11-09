import { createRouter, createWebHistory } from 'vue-router'
import Someview from '@/views/SomeView.vue'
import Otherview from '@/views/OtherView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'some',
      // views : SomeView
      component: Someview
    },
    {
      path : '/other',
      name : 'other',
      // views: OtherView
      component: Otherview
    }
  ]
})

export default router
