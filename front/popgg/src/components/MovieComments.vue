<template>
  <div class="row" style="margin: 0">
    <div style="width: 50%; text-align: center; padding-right: 0%">
      <h1>리뷰 작성</h1>
      <textarea
        v-model="newcomment"
        cols="50"
        rows="2"
        placeholder="지금 당장 리뷰 나눔"
        @keyup.enter="createComment"
      ></textarea>
      <span><button @click="createComment">작성</button></span>
    </div>
    <div style="width: 50%; text-align: center">
      <hr />
      <div
        v-for="comment in comments"
        :key="comment.id"
        style="display: flex; justify-content: space-between"
      >
        <!-- {{ comment.user_region }} -->
        <!-- {{ comment.user_gender }} -->
        {{ comment.user_nickname }}[{{ comment.user_gender }}]:
        {{ comment.content }}
        <a
          style="margin-left: 0%; width: 60px"
          @click="deletereview(comment.id)"
          v-if="comment.user == $store.state.user_id"
        >
          삭제
        </a>
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"
export default {
  name: "ArticleComments",
  props: {
    movie_id: Object,
  },
  data() {
    return {
      comments: [],
      newcomment: null,
      comments_id: null,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    },
  },
  methods: {
    getArticleComment() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/reviews/${this.movie_id}/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.comments = res.data))
          console.log(this.comments, "------------------")
        })
        .catch((err) => console.log(err))
      // axios({
      //     method: 'get',
      //     url: `${API_URL}/api/v2/accounts/${this.comments.user}/`,
      //     headers: {
      // //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
      // Authorization: `Token ${this.token}`,
      // },
      // })
      // .then((res) => {
      //     console.log(this.comments=res.data)
      // })
      // .catch(err => console.log(err))
    },
    deletereview(e) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/${this.movie_id}/reviews/${e}/update_delete/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.users = res.data))
          this.getArticleComment()
        })
        .catch((err) => console.log(err))
    },
    createComment() {
      const content = this.newcomment
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movie_detail/${this.movie_id}/reviews/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: content,
        },
      })
        .then((res) => {
          console.log(res.data, "44444444444")
          this.getArticleComment()
          this.newcomment = null
        })
        .catch((err) => console.log(err))
    },
  },
  created() {
    this.getArticleComment()
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
