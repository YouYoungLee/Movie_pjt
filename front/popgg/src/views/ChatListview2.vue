<template>
  <div style="background-color: pink; margin-top: 110px">
    <div
      v-for="(message, idx) in messages"
      :key="`message-${idx}`"
      style="
        text-align: top;
        height: auto;
        overflow: auto;
        border-left: solid;
        border-right: solid;
        margin-right: 35%;
        margin-left: 35%;
      "
    >
      <!-- {{ $store.state.user_id }} -->
      <div v-if="message.user == $store.state.user_id" style="float: right">
        <div
          style="
            margin-right: 20px;
            background-color: #f9eb54;
            position: relative;
            display: inline-block;
            max-width: 300px;
            padding: 10px;
            margin-top: 7px;
            font-size: 13px;
            border-radius: 10px;
          "
        >
          {{ message.content }}
        </div>
      </div>
      <span
        v-else
        style="float: left; margin-left: 10px"
        class="fa-solid fa-user"
      >
        <span v-if="message.user_gender == '남'">
          <img src="@/assets/profileman.png" alt="" style="height: 40px" />
        </span>
        <span v-else-if="message.user_gender == '여'">
          <img src="@/assets/profilewoman.png" alt="" style="height: 40px" />
        </span>
        <span>
          {{ message.user_nickname }}
        </span>
        <span
          style="
            margin-right: 20px;
            background-color: rgb(157, 240, 240);
            position: relative;
            display: inline-block;
            max-width: 300px;
            padding: 10px;
            margin-top: 7px;
            font-size: 13px;
            border-radius: 10px;
          "
        >
          {{ message.content }}
        </span>
      </span>
      <br />
      <br />
    </div>
    <footer>
      <div
        style="
          position: fixed;
          bottom: 2%;
          left: 50%;
          transform: translateX(-50%);
        "
      >
        <input
          type="text"
          v-model="newmessage"
          placeholder="메시지를 입력하세요"
          @keyup.enter="createMessage"
          style="width: 500px; height: 40px; border-radius: 5px"
        />
        <span>
          <b-button @click="createMessage()">보내기</b-button>
        </span>
      </div>
    </footer>
    <br />
    <br />
    <br />
    <br />
  </div>
</template>

<script>
// import router from "@/router"
import axios from "axios"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"

export default {
  components: {},
  name: "ArticleDetail",
  data() {
    return {
      newmessage: null,
      messages: [],
      user1_id: null,
      room_id: null,
    }
  },
  created() {
    console.log(this.$route.params.id, "j아이디디디디디")
    this.room_id = this.$route.params.id
    console.log(this.room_id, "44444444444")
    this.getMessageDetail2()
    this.gotobot()
  },
  computed: {
    token() {
      return this.$store.state.token
    },
    user2_id() {
      return this.$store.state.user_id
    },
  },
  methods: {
    createMessage() {
      const content = this.newmessage
      axios({
        method: "post",
        url: `${API_URL}/api/v4/${this.room_id}/message/create/`,
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
          this.getMessageDetail2()
          this.newmessage = null
        })
        .catch((err) => console.log(err))
    },
    gotobot() {
      window.scrollTo(0, document.documentElement.scrollHeight)
      console.log(document.documentElement.scrollHeight)
    },
    getMessageDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v4/room_message/${this.room_id}/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.messages = res.data))
        })
        .catch((err) => console.log(err))
    },
    getMessageDetail2() {
      axios({
        method: "get",
        url: `${API_URL}/api/v4/room_message/${this.room_id}/`,
        headers: {
          //   Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.messages = res.data))
        })
        .then(() => {
          window.scrollTo(0, document.documentElement.scrollHeight)
        })
        .catch((err) => console.log(err))
    },
  },
  mounted() {
    console.log(this.user1_id, "333333333")
    setInterval(this.getMessageDetail, 2000)
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
</style>
