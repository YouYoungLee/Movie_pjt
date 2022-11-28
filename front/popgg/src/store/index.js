import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import router from "@/router"
import createdPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"

export default new Vuex.Store({
  plugins: [createdPersistedState()],
  state: {
    token: null,
    movies: [],
    gmovies: [],
    articles: [],
    comments: [],
    nickname: null,
    gender: null,
    region: null,
    user_id: null,
    username: null,
  },
  // getters: {
  //     isLogin(state) {
  //       return state.token ? true : false
  //     },
  //   },
  mutations: {
    GET_MOVIES(state, movies) {
      console.log(movies)
      state.movies = movies
      console.log(this.state.movies)
    },
    GET_GMOVIES(state, gmovies) {
      console.log(gmovies, "------------")
      state.gmovies = gmovies
      console.log(this.state.gmovies, "gmovies;;;;;;;;;;")
    },
    // 회원가입 && 로그인
    SAVE_TOKEN(state, token) {
      console.log(token)
      state.token = token
      console.log(state.token)
      router.push({ name: "MovieView" })
    },
    GET_ARTICLE(state, article) {
      state.articles = article
      console.log(this.state.articles)
    },
    DELETE_TOKEN(state) {
      state.token = null
      state.nickname = null
      state.gender = null
      state.region = null
      state.user_id = null
    },
    GETUSERNICKNAME(state, user) {
      console.log(user)
      state.nickname = user.nickname
      state.gender = user.gender
      state.region = user.region
      state.user_id = user.id
    },
    SAVE_USERNAME(state, username) {
      state.username = username
    },
  },
  actions: {
    getMovies(context) {
      console.log(context)
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movielist/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log(res.data[0].title, context)
          // console.log(res.data)
          // context.commit("GET_ARTICLES", res.data)
          context.commit("GET_MOVIES", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getGMovies(context) {
      console.log(context, "겟지무비")
      axios({
        method: "get",
        url: `${API_URL}/api/v1/gmovielist/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log(res.data[0].title, context)
          // console.log(res.data)
          // context.commit("GET_ARTICLES", res.data)
          context.commit("GET_GMOVIES", res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
          nickname: payload.nickname,
          gender: payload.genders,
          region: payload.regions,
          name: payload.name,
        },
      }).then((res) => {
        console.log(res)
        context.commit("SAVE_TOKEN", res.data.key)
        context.commit("SAVE_USERNAME", payload.username)
      })
    },
    Get_Article(context) {
      console.log("아티클 내가 여기 왔다")
      axios({
        method: "get",
        url: `${API_URL}/api/v3/index/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log(res.data)
          // console.log(res.data)
          // context.commit("GET_ARTICLES", res.data)
          context.commit("GET_ARTICLE", res.data)
        })
        .catch((err) => {
          console.log(err, context)
        })
    },
    logIn(context, payload) {
      console.log(payload)
      const username = payload.username
      const password = payload.password
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log(res)
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .catch((err) => console.log(err))
    },
    logOut(context) {
      context.commit("DELETE_TOKEN")
    },

    Get_Comment(context) {
      console.log("커멘트 내가 여기 왔다")
      axios({
        method: "get",
        url: `${API_URL}/api/v3/article_comments/`,
        headers: {
          Authorization: `Token ${context.state.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log(res.data)
          // console.log(res.data)
          // context.commit("GET_ARTICLES", res.data)
          context.commit("GET_ARTICLE", res.data)
        })
        .catch((err) => {
          console.log(err, context)
        })
    },
    Usernametemp(context, username) {
      axios({
        method: "get",
        url: `${API_URL}/api/v2/${username}/`,
        // headers: {
        //   Authorization: `Token ${context.state.token}`,
        //   // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        // },
      })
        .then((res) => {
          console.log(res.data, "--------------유저네임템프--")
          // console.log(res.data)
          // context.commit("GET_ARTICLES", res.data)
          context.commit("GETUSERNICKNAME", res.data)
        })
        .catch((err) => {
          console.log(err, context)
          console.log("--------------유저네임템프실패--")
        })
    },
  },

  modules: {
    // socket,
  },
})
