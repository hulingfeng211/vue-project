/**
 * Created by george on 11/19/16.
 */

import index from './components/Index';
import list from './components/List';
import notFound from './components/notFound'
import Markdown from './components/Markdown'

const routes = [
  { path: '/', component: index },
  { path: '/list', component: list },
  { path: '/markdown', component: Markdown },
  { path: '*', component: notFound }
];

export  default routes ;
