import { createRouter, createWebHistory } from 'vue-router'
import Someview from '@/views/SomeView.vue'
import Otherview from '@/views/OtherView.vue'
import StudentView from '@/views/StudentView.vue'
import StudentDetailView from '@/views/StudentDetailView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'some',
      component: Someview
    },
    {
      path : '/other',
      name : 'other',
      component: Otherview
    },
    {
      path : '/students',
      component: StudentView
    },
    {
      path: '/students/:name',
      name : 'studentDetail',
      component: StudentDetailView
    }
  ]
})

export default router
