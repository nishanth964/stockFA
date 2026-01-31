import { createRouter, createWebHistory } from 'vue-router';
import Home from '../assets/pages/home.vue';
import Results from '../assets/pages/results.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/results',
    name: 'Results',
    component: Results,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;