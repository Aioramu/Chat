import Vue from 'vue'
import Router from 'vue-router'
import Chat from '@/components/Chat'
import UserAuth from '@/components/UserAuth'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/chatting',
      name: 'Chat',
      component: Chat
    },

    {
      path: '/users',
      name: 'UserAuth',
      component: UserAuth
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  }
  } else {
    next('/auth')
  }
})

export default router