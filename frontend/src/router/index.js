import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
// import HelloWorld from '@/components/HelloWorld'

const routerOptions = [
  { name: 'Home', path: '/', component: 'Home' },
  { name: 'About', path: '/about', component: 'About' },
  { name: 'NotFound', path: '*', component: 'NotFound' },
  { name: 'HelloWorld', path: '/helloworld', component: 'HelloWorld' },
  { name: 'Login', path: '/login', component: 'Login' },
  { name: 'Secure', path: '/secure', component: 'Secure' },
  { name: 'NavBar', path: '/nav', component: 'NavBar' },
  { name: 'Account', path: '/account', component: 'Account' },
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
/*
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAUTH)) {
    if (!store.getters.is_logged_in) { }
  }
})
*/
