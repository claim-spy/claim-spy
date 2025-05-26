import TestIndex from "@/pages/test/testIndex.vue";
import {createMemoryHistory, createRouter, createWebHistory} from "vue-router";
import Home from "@/pages/Home.vue";
import IndexVal from "@/pages/test/[value]/indexVal.vue";


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/test',
        name: 'test',
        component: TestIndex
    },
    {
        path: '/test/:value',
        name: 'testVal',
        component: IndexVal
    }
]

export default createRouter({
    history: createWebHistory(),
    routes
})

