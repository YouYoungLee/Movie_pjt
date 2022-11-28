<template>
  <div class="container" style="width: 75%">
    <div class="backsheet p-4" style="text-align: left">
      <p class="text-content">댓글 작성</p>
      <textarea
        v-model="newcomment"
        cols="50"
        rows="2"
        placeholder="지금 당장 같이 고고"
        @keyup.enter="createComment"
      ></textarea>
      <span><button @click="createComment">작성</button></span>
      <hr />
      <h3>댓글 목록</h3>
      <hr />
      <p v-for="comment in comments" :key="comment.id">
        <!-- {{ comment.user_region }} -->
        <!-- {{ comment.user_gender }} -->
        {{ comment.user_nickname }}:
        {{ comment.content }}
        <button
          @click="deletereview(comment.id)"
          v-if="comment.user == $store.state.user_id"
        >
          삭제
        </button>
      </p>
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
    article_id: Object,
  },
  data() {
    return {
      comments: [],
      newcomment: null,
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
        url: `${API_URL}/api/v3/article_comments/${this.article_id}/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.comments = res.data))
          console.log(this.comments)
        })
        .catch((err) => console.log(err))
    },
    createComment() {
      const content = this.newcomment
      console.log(content, "호호호호")
      axios({
        method: "post",
        url: `${API_URL}/api/v3/${this.article_id}/comments/create/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
        data: {
          content: content,
        },
      })
        .then((res) => {
          console.log(res)
          this.getArticleComment()
          this.newcomment = null
        })
        .catch((err) => console.log(err))
    },
    deletereview(e) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v3/${this.article_id}/comments/${e}/update_delete/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.comments = res.data))
          this.getArticleComment()
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
