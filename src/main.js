import Vue from 'vue';

// Libraries
import Router from 'vue-router';
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(Router);
Vue.use(BootstrapVue);

// Views
import App from './App.vue';

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: App,
    },
  ]
});

new Vue({
  el: '#app',
  render: h => h(App),
  router
});
