import Vue from "vue"
import VueRouter from "vue-router"
import MovieView from "../views/MovieView.vue"
import SignUpView from "../views/SignUpView.vue"
import CreateArticle from "@/views/CreateArticle"
import HomeView from "@/views/HomeView.vue"
import MovieDetail from "@/views/MovieDetail.vue"
import CommunityView from "@/views/CommunityView.vue"
import ArticleDetail from "@/views/CommunityDetail.vue"
import LoginView from "@/views/Login.vue"
import UpdateArticle from "@/views/UpdateArticle.vue"
import Store from "@/store/index"
import ChatRoom from "@/views/ChatRoomview.vue"
import ChatRoom2 from "@/views/ChatListview2.vue"
import ChatList from "@/views/ChatListview.vue"
// import Chat from "@/views/ChatView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "HomeView",
    component: HomeView,
  },
  {
    path: "/login",
    name: "LoginView",
    component: LoginView,
  },
  {
    path: "/index",
    name: "MovieView",
    component: MovieView,
  },
  {
    path: "/signup",
    name: "SignUpView",
    component: SignUpView,
  },
  {
    path: "/article/create",
    name: "CreateArticle",
    component: CreateArticle,
  },
  {
    path: "/article/update",
    name: "UpdateArticle",
    component: UpdateArticle,
    props: true,
  },
  {
    path: "/community",
    name: "CommunityView",
    component: CommunityView,
  },
  {
    path: "/chatlist",
    name: "ChatList",
    component: ChatList,
  },
  {
    path: "/chatroom/:id",
    name: "ChatRoom",
    component: ChatRoom,
  },
  {
    path: "/movie/:id",
    name: "MovieDetail",
    component: MovieDetail,
  },
  {
    path: "/community/:id",
    name: "ArticleDetail",
    component: ArticleDetail,
  },
  {
    path: "/chatroom2/:id",
    name: "ChatRoom2",
    component: ChatRoom2,
  },
  // {
  //   path: "/chat",
  //   name: "Chat",
  //   component: Chat,
  // },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  // 로그인 여부

  let isLoggedIn = false

  // // 로그인이 필요한 페이지
  // const authPages = ["hello"]

  // const isAuthRequired = authPages.includes(to.name)

  // const isLoggedIn = ture

  if (Store.state.token != null) {
    isLoggedIn = true
  } else {
    isLoggedIn = false
  }

  // 로그인이 필요한 페이지 전부다 막음
  // const authPages = ["hello", "home", "about"]
  const allowAllPages = ["HomeView", "LoginView", "SignUpView"]

  // const isAuthRequired = authPages.includes(to.name)
  const isAuthRequired = !allowAllPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    console.log("Login으로 이동!")
    next({ name: "HomeView" })
  } else {
    console.log("to로 이동!")
    next()
  }
  // if (!isAuthRequired && isLoggedIn) {
  //   next({ name: "index" })
  // } else {
  //   next()
  // }
})

export default router
