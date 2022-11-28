<template>
  <div style="background-color: pink; padding-top: 150px">
    <movie-card-2></movie-card-2>
    <hr style="border: solid white" />
    <h1 class="text-center">동네에서 같이 영화 보자!</h1>
    <select
      name="region"
      id="region"
      v-model="selecregion"
      style="width: 202px; height: 30px; float: right; margin-right: 17%"
      @change="onChange()"
      class="custom-select"
    >
      <!-- <option value="" disabled selected>Select your option</option>
      -->
      <option :value="null">지역을 선택하세요</option>
      <option v-for="region in regions" :key="region" :value="region">
        {{ region }}
      </option>
    </select>
    <label for="region" style="float: right; margin-right: 3px"> 지역 : </label>
    <br />
    <hr style="border: solid white" />
    <table style="margin: auto">
      <tr>
        <th class="text-center">지역</th>
        <th class="text-center">영화</th>
        <th class="text-center">영화관</th>
        <th class="text-center">글제목</th>
        <th class="text-center">작성자</th>
        <th class="text-center">작성시간</th>
      </tr>
      <article-card
        v-for="(article, idx) in sarticles"
        :key="`article-${idx}`"
        :article="article"
      >
      </article-card>
    </table>
    <p></p>
    <button class="btn btn-secondary" style="float: right; margin-right: 10%">
      <router-link
        :to="{ name: 'CreateArticle' }"
        style="text-decoration: none; color: white"
        >글쓰기</router-link
      >
    </button>
    <br />
    <br />
    <hr />
    <br />
  </div>
</template>

<script>
import ArticleCard from "../components/ArticleCard.vue"
import MovieCard2 from "../components/MovieCard2.vue"

export default {
  name: "ArticleView",
  components: {
    ArticleCard,
    MovieCard2,
  },
  data() {
    return {
      articles: [],
      sarticles: [],
      selecregion: null,
      regions: [
        "전체",
        "서울",
        "강원",
        "경기",
        "충북",
        "충남",
        "경북",
        "경남",
        "전북",
        "전남",
        "제주",
        "인천",
        "부산",
        "광주",
        "대전",
        "대구",
        "울산",
        "세종",
      ],
    }
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  methods: {
    onChange() {
      console.log(this.selecregion)
      this.sarticles = []
      this.articles.filter((article) => {
        if (article.user_region === this.selecregion) {
          console.log(this.selecregion)
          this.sarticles.push(article)
        }
      })
      if (this.selecregion === "전체") {
        this.sarticles = this.$store.state.articles
      }
    },
  },
  created() {
    console.log("아티클")
    this.$store.dispatch("Get_Article")
    this.articles = this.$store.state.articles
    this.sarticles = this.$store.state.articles
    this.$store.dispatch("getMovies")
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
