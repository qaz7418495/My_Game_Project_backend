import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: ()=> import('../views/Main.vue')
    },
    {
      path: '/lol',
      name: 'Lol',
      component: ()=> import('../views/lol/lol.vue')
    },
    {
      path: '/valorant',
      name: 'Valorant',
      component: ()=> import('../views/valorant/valorant.vue')
    },
    {
      path: '/csgo',
      name: 'Csgo',
      component: ()=> import('../views/csgo/csgo.vue')
    },
    {
      path: '/welcome',
      name: 'Welcome',
      component: ()=> import('../views/Welcome.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: ()=> import('../views/login/login.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: ()=> import('../views/register/register.vue')
    },
  ]
})

export default router
