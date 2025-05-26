import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from "pinia";
import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from './components/MainLayout.vue';
import Placeholder from './pages/Placeholder.vue';

const app = createApp(App)
const pinia = createPinia()

const routes = [{ 
    path: '/', 
    component: MainLayout,
    children: [
        {
            path: 'placeholder',
            name: 'Placeholder',
            component: Placeholder,
            meta: {title: "Placeholder"}
        },
    ]},
  { 
    path: '/login',
    name: "Login", 
    component: Placeholder
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
// router.beforeEach(isAuthenticated)

app.use(pinia)
app.use(router)
app.mount('#app')
