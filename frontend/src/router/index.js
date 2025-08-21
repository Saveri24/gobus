import Vue from "vue";
import Router from "vue-router";

import Dashboard from "@/pages/admin/Dashboard.vue";
import BusList from "@/pages/admin/BusList.vue";
import ScheduleList from "@/pages/admin/ScheduleList.vue";
import BookingList from "@/pages/admin/BookingList.vue";

import Home from "@/pages/user/Home.vue";
import SearchResults from "@/pages/user/SearchResults.vue";
import BookingPage from "@/pages/user/BookingPage.vue";
import MyBookings from "@/pages/user/MyBookings.vue";

import Login from "@/pages/auth/Login.vue";
import Register from "@/pages/auth/Register.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: Home,
    },
    {
      path: "/search",
      name: "SearchResults",
      component: SearchResults,
    },
    {
      path: "/booking/:id",
      name: "BookingPage",
      component: BookingPage,
    },
    {
      path: "/my-bookings",
      name: "MyBookings",
      component: MyBookings,
    },
    {
      path: "/admin/dashboard",
      name: "Dashboard",
      component: Dashboard,
    },
    {
      path: "/admin/buses",
      name: "BusList",
      component: BusList,
    },
    {
      path: "/admin/schedules",
      name: "ScheduleList",
      component: ScheduleList,
    },
    {
      path: "/admin/bookings",
      name: "BookingList",
      component: BookingList,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
    },
  ],
});
