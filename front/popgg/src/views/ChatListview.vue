<template>
  <div style="background-color: pink; padding-top: 110px">
    <h1>POP TALK</h1>
    <table style="margin: auto">
      <tr v-for="(room1, idx) in rooms1" :key="idx">
        <span v-if="room1.user1 != room1.user2">
          <span v-if="room1.user1_gender == '남'">
            <img
              src="@/assets/profileman.png"
              alt="man"
              style="height: 70px; float: left"
            />
          </span>
          <span v-else-if="room1.user1_gender == '여'">
            <img
              src="@/assets/profilewoman.png"
              alt="woman"
              style="height: 70px; float: left"
            />
          </span>
          <span @click="move(room1.id)" style="font-size: 50px">
            {{ room1.user1_nickname }}
          </span>
        </span>
      </tr>
      <tr v-for="(room2, idx) in rooms2" :key="idx">
        <span v-if="room2.user1 != room2.user2">
          <span v-if="room2.user2_gender == '남'">
            <img
              src="@/assets/profileman.png"
              alt="man"
              style="height: 70px; float: left"
            />
          </span>
          <span v-else-if="room2.user2_gender == '여'">
            <img
              src="@/assets/profilewoman.png"
              alt="woman"
              style="height: 70px; float: left"
            />
          </span>
          <span @click="move(room2.id)" style="font-size: 50px">
            {{ room2.user2_nickname }}
          </span>
        </span>
      </tr>
    </table>
  </div>
</template>

<script>
import router from "@/router"
import axios from "axios"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000";

export default {
  components: {},
  name: "ArticleDetail",
  data() {
    return {
      article: null,
      temp: [],
      rooms1: [],
      rooms2: [],
      article_id: null,
      movie_id: null,
    }
  },
  created() {
    this.getroom()
  },
  computed: {
    user_id() {
      return this.$store.state.user_id
    },
    token() {
      return this.$store.state.token
    },
  },
  methods: {
    getroom() {
      axios({
        method: "get",
        url: `${API_URL}/api/v4/index/`,
        headers: {
          Authorization: `Token ${this.token}`,
          // Authorization: `Token 5bf38fd3b0616df0e87b182307ab0de78b7411f1`,
        },
      })
        .then((res) => {
          console.log((this.temp = res.data))
          this.temp.filter((e) => {
            console.log(e)
            if (e.user2 === this.user_id) {
              console.log("e확인용")
              this.rooms1.push(e)
            }
            if (e.user1 === this.user_id) {
              console.log("e2확인용")
              this.rooms2.push(e)
              console.log(this.rooms)
            }
          })
        })
        .catch((err) => console.log(err))
    },
    move(e) {
      console.log(e, "e확인이니")
      router.push({
        name: "ChatRoom2",
        params: { id: e },
      })
    },
  },
}
</script>

<style>
html {
  background-color: pink;
}
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
