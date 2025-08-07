import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/DashboardSimple.vue'

const routes = [
  {
    path: '/',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/commands',
    name: 'Commands',
    component: () => import('../views/Commands.vue')
  },
  {
    path: '/metrics',
    name: 'Metrics',
    component: () => import('../views/Metrics.vue')
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../views/Settings.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router