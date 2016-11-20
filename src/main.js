/**
 * Created by george on 11/19/16.
 */
import Vue from 'vue'
import VueRouter from 'vue-router'
import routes from './routes'
import ElementUI from 'element-ui'
import VueResource from 'vue-resource'

import App from './App'
import '../node_modules/element-ui/lib/theme-default/index.css'

Vue.use(VueRouter);
Vue.use(ElementUI);
Vue.use(VueResource)

Vue.config.devtools = true;

const router = new VueRouter({
    routes // short for routes: routes
});

const app = new Vue({
	router,
    el:"#app",
    render:h=>h(App)
    //router
});
//.$mount('#app');