<template>
  <div style="background-color: pink; margin-top: 100px">
    <div class="Articledetail" style="padding-bottom: 75px">
      <br />
      <br />
      <h1 style="float: left; margin-left: 20%">
        <strong> 글 제목: {{ article.title }}</strong>
      </h1>
      <br />
      <br />
      <div style="float: right; margin-right: 10%">
        작성자: [{{ article.user_region }} {{ article.user_gender }}]
        {{ article.user_nickname }}
      </div>
      <br />
      <div style="color: lightslategray; float: right; margin-right: 10%">
        최근 수정일: {{ article.updated_at.substring(0, 10) }}
        {{ article.updated_at.substring(11, 19) }}
      </div>
      <img
        :src="`https://image.tmdb.org/t/p/w342${movies.poster_path}`"
        alt=""
        style="max-width: 200px; float: left; margin-left: 25%"
      />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <br />
      <h3 style="float: right; margin-right: 10%">
        영화관: {{ article.cinema }}
      </h3>
      <br />
      <br />
      <div style="float: right; margin-right: 10%">
        <div v-if="cinemas_name === 'CGV'">
          <a
            href="http://www.cgv.co.kr/ticket/"
            style="text-decoration-line: none"
          >
            예매 바로가기
          </a>
        </div>
        <div v-else-if="cinemas_name === '메가박스'">
          <a
            href="https://www.megabox.co.kr/booking"
            style="text-decoration-line: none"
          >
            예매 바로가기
          </a>
        </div>
        <div v-else-if="cinemas_name === '롯데시네마'">
          <a
            href="https://www.lottecinema.co.kr/NLCHS/Ticketing"
            style="text-decoration-line: none"
          >
            예매 바로가기
          </a>
        </div>
      </div>
      <br />
      <br />
      <br />
      <br />
      <!-- <h2 style="float: left; margin-left: 25%">{{ movies.title }}</h2> -->
      <br />
      <br />
      <div
        style="
          width: 70%;
          height: auto;
          background-color: aliceblue;
          margin-left: 20%;
          padding-left: 30px;
          padding-top: 10px;
          padding-bottom: 20px;
          text-align: left;
          font-size: 20px;
        "
      >
        {{ article.content }}
      </div>
      <br />
      <span
        style="float: right; margin-right: 10%"
        v-if="article.user == $store.state.user_id"
        ><button @click="deletearticle(article.id)">삭제</button></span
      >
      <router-link
        v-if="article.user == $store.state.user_id"
        :to="{
          name: 'UpdateArticle',
          params: { Article: article_id },
        }"
        style="float: right; margin-right: 1%; text-decoration-line: none"
        >수정</router-link
      >

      <br />
      <br />
      <br />

      <article-comments
        :article_id="article_id"
        style="margin-left: 18%; margin-right: 10%"
      >
      </article-comments>
    </div>
    <footer>
      <button
        class="btn btn-secondary"
        @click="$router.push({ name: 'CommunityView' })"
        style="margin-left: 18%"
      >
        커뮤니티로 가기
      </button>
      <nav style="margin-right: 8%">
        <button
          v-if="article.user != $store.state.user_id"
          class="btn btn-secondary"
        >
          <router-link
            :to="{
              name: 'ChatRoom',
              params: { User_id: article.user },
            }"
            style="text-decoration: none; color: white"
            >작성자와 채팅하러 가기</router-link
          >
        </button>
      </nav>
    </footer>
  </div>
</template>

<script>
import router from "@/router"
import axios from "axios"
import ArticleComments from "../components/ArticleComments.vue"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"

export default {
  components: {
    ArticleComments,
  },
  name: "ArticleDetail",
  data() {
    return {
      article: null,
      comments: [],
      article_id: null,
      movie_id: null,
      cinemas_name: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    movies() {
      return this.$store.state.movies[this.movie_id - 1]
    },
    token() {
      return this.$store.state.token
    },
  },
  methods: {
    getArticleDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v3/${this.$route.params.id}/`,
        headers: {
          Authorization: `Token ${this.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log((this.article = res.data))
          this.article_id = this.$route.params.id
          this.movie_id = res.data.movie_title
          this.cinemas_name = res.data.cinema
        })
        .catch((err) => console.log(err))
    },
    deletearticle() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v3/${this.$route.params.id}/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          router.push({ name: "CommunityView" })
        })
        .catch((err) => console.log(err))
    },
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
.articleContainer {
  width: 900px;
}
footer {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;

  height: 75px;
  padding: 1rem;
  color: white;
  background: pink;
  font-weight: bold;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
