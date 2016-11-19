/**
 * Created by george on 11/19/16.
 */

import index from './components/Index';
import list from './components/List';
import notFound from './components/notFound'

const routes = [
  { path: '/', component: index },
  { path: '/list', component: list },
  { path: '*', component: notFound }
];

export  default routes ;
