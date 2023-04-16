// import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView
//     },
//     {
//       path: '/about',
//       name: 'about',
//       // route level code-splitting
//       // this generates a separate chunk (About.[hash].js) for this route
//       // which is lazy-loaded when the route is visited.
//       component: () => import('../views/AboutView.vue')
//     }
//   ]
// })

// export default router

// index.js 文件内容

import { createRouter, createWebHashHistory } from 'vue-router'

// 1. 定义路由组件.
// 也可以从其他文件导入
import task from '../views/task.vue'
import testcase from '../views/testcase.vue'
import index from '../views/index.vue'

// 2. 定义一些路由
// 每个路由都需要映射到一个组件。
const routes = [
    {
        path: '/',
        redirect:'/index/testcase',
    },
    {
        path: '/index',
        component: index,
        children: [
            { path: 'task', name: 'task', component: task },
            { path: 'testcase', name: 'testcase', component: testcase },
        ]
    },

]

const router = createRouter({
    // 3. 内部提供了 history 模式的实现
    history: createWebHashHistory(),
    routes, // `routes: routes` 的缩写
})
export default router;




