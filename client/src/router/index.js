import { createRouter, createWebHistory } from "vue-router";
import DashBoard from "@/components/Dashboard.Vue";
import LoginPage from "@/components/Login.Vue";
import store from '@/store/store.js'

// const allowOnlyTouristRoute = (to, from, next) => {
//   console.log(store.state);
//   console.log(store.state.type);
//   console.log(`Allow: ${store.state.type === "tourist"}`);
//   store.state.type === "tourist" ? next() : next("/noaccess");
// }

// const allowOnlyTourGuideRoute = (to, from, next) => {
//   console.log(store.state);
//   console.log(store.state.type);
//   console.log(`Allow: ${store.state.type === "tour-guide"}`);
//   store.state.type === "tour-guide" ? next() : next("/noaccess");
// }

// const allowOnlyAuthRoute = (to, from, next) => {
//   console.log(store.state);
//   console.log(store.state.type);
//   console.log(`Allow: ${store.state.type !== null}`);
//   store.state.type !== null ? next() : next("/noaccess");
// }


const routes = [
    {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage
    },
    {
      path: '/dashboard',
      name: 'DashBoard',
      component: DashBoard
    },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
