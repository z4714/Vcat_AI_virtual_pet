import { defineConfig } from '@umijs/max';

export default defineConfig({
  antd: {},
  access: {},
  model: {},
  initialState: {},
  request: {},
  layout: {
    title: 'Vcat',
  },
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      name: '首页',
      path: '/home',
      component: './Home',
    },
    {
      name: '宠物仓',
      path: '/access',
      component: './Access',
    },
    {
      name: '互动',
      path: '/table',
      component: './Table',
    },
    {
      name: '用户',
      path: '/user',
      component: './User',
    },
    {
      name: '登录',
      path: '/login',
      component: './Login',
    },
  ],
  npmClient: 'pnpm',


}





);
  // ...


