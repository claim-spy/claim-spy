import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from "pinia";
import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from './components/MainLayout.vue';
import Placeholder from './pages/Placeholder.vue';
import Login from './pages/Login.vue';
import Register from './pages/Register.vue';
import { refreshAccessToken, refreshUser, removeAuthStorage } from './utils';

const app = createApp(App)
const pinia = createPinia()

const routes = [{ 
    path: '/', 
    component: MainLayout,
    children: [
        {
            path: 'home',
            name: 'Home',
            component: Placeholder,
            meta: {title: "Placeholder home"}
        },
    ]},
  {
    path: '/login',
    name: "Login", 
    component: Login
  },
    { 
    path: '/register',
    name: "Register", 
    component: Register
  },
]

export async function isAuthenticatedGuard(to) {
    const publicRoutes = ['Login', 'Register']

    if (publicRoutes.includes(to.name)) return true

    if(!localStorage.getItem('refresh_token')){
        removeAuthStorage()
        return {name: 'Login'}
    }
    
    if(!localStorage.getItem('access_token')){
        await refreshAccessToken(router)
    }
    
    if(!sessionStorage.getItem('user')){
        await refreshUser(router)
    }
}

const router = createRouter({
  history: createWebHistory(),
  routes,
})
router.beforeEach(isAuthenticatedGuard)
app.use(pinia)
app.use(router)
app.mount('#app')
