<template>
  <div style="background-color: pink">
    <h1>같이 봐요!(수정)</h1>
    <form @submit.prevent="CreateArticle">
      <label for="movie_title"> 영화제목 : </label>
      <select name="movie_title" id="movie_title" v-model="movie_title">
        <option v-for="movie in movies" :key="movie.title">
          {{ movie.id }} {{ movie.title }}
        </option></select
      ><br />

      <label for="cinema"> 영화관 : </label>
      <select name="cinema" id="cinema" v-model="article.cinema">
        <option v-for="cinema in cinemas" :key="cinema">
          {{ cinema }}
        </option></select
      ><br />

      <label for="title">제목 : </label>
      <input type="text" id="username" v-model="article.title" /><br />

      <label for="content"> 내용 : </label>
      <textarea
        id="content"
        cols="30"
        rows="10"
        v-model="article.content"
      ></textarea>

      <input type="submit" value="영화 보러 가자!" @click="create" />
    </form>
  </div>
</template>

<script>
import axios from "axios"
import router from "@/router"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"

export default {
  name: "CreateArticle",
  data() {
    return {
      title: null,
      content: null,
      cinema: null,
      movie_title: null,
      cinemas: ["CGV", "메가박스", "롯데시네마", "기타"],
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
    article() {
      return this.$store.state.articles
    },
    token() {
      return this.$store.state.token
    },
  },
  methods: {
    create() {
      const title = this.article.title
      const content = this.article.content
      const cinema = this.article.cinema
      const movie_title = this.movie_title.substr(0, 2)
      // const token = this.token

      const payload = {
        title: title,
        content: content,
        cinema: cinema,
        movie_title: movie_title,
      }
      console.log(payload)
      axios({
        method: "put",
        url: `${API_URL}/api/v3/${this.$route.params.Article}/`,
        headers: {
          Authorization: `Token ${this.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
        data: {
          title,
          content,
          cinema,
          movie_title,
        },
      })
        .then((res) => {
          console.log(res)
          // console.log(res.data)
          // context.commit("CREATE_ARTICLES", res.data)
          // context.commit("GET_MOVIES", res.data)
          router.push({
            name: "ArticleDetail",
            params: { id: this.$route.params.Article },
          })
        })
        .catch((err) => console.log(err))
    },
  },
  created() {
    console.log(this.$route.params.Article)
    console.log(this.$store.state.articles)
    this.$store.state.articles.filter((article) => {
      console.log(article.id)
      if (article.id === this.$route.params.Article) {
        this.article.title = article.title
        this.article.content = article.content
        this.article.cinema = article.cinema
        console.log(article)
      }
    })
  },
}
</script>
<style>
@font-face {
  font-family: "NanumSquareNeo-Variable";
  src: url("https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_11-01@1.0/NanumSquareNeo-Variable.woff2")
    format("woff2");
  font-weight: normal;
  font-style: normal;
}
template {
  font-size: 15px;
  font-family: NanumSquareNeo-Variable;
}
</style>
