import Vue from 'vue'
import Router from 'vue-router'

// Import components (relative paths instead of @ alias)
import AdminLayout from '../components/layouts/AdminLayout.vue'
import AdminDashboard from '../components/layouts/pages/admin/AdminDashboard.vue'
import BusList from '../components/layouts/pages/admin/BusList.vue'
import ScheduleList from '../components/layouts/pages/admin/ScheduleList.vue'
import BookingList from '../components/layouts/pages/admin/BookingList.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/admin',
      component: AdminLayout,
      children: [
        { path: 'dashboard', component: AdminDashboard },
        { path: 'buses', component: BusList },
        { path: 'schedules', component: ScheduleList },
        { path: 'bookings', component: BookingList }
      ]
    },
    { path: '*', redirect: '/admin/dashboard' }
  ]
})
