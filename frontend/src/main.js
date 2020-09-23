// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import axios from 'axios'
import store from './store/index'
Vue.config.productionTip = true
/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: store,
  router,
  components: { App },
  template: '<App/>'
})

