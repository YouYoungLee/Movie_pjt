<template>
  <div style="background-color: pink">
    <b-navbar type="dark" variant="dark" class="px-5">
      <b-navbar-brand href="/index">
        <img src="@/assets/couple1.png" alt="" style="height: 70px" />
      </b-navbar-brand>
      <b-navbar-brand href="/index">
        <h1>POP.GG</h1>
      </b-navbar-brand>

      <!-- <b-navbar-toggle target="nav-collapse"></b-navbar-toggle> -->

      <b-collapse class="justify-content-end" id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <nav class="justify-content-end container">
              <router-link
                class="text-decoration-none mx-3 col-4"
                :to="{ name: 'LoginView' }"
              >
                Login
              </router-link>
              <router-link
                class="text-decoration-none mx-3 col-4"
                :to="{ name: 'SignUpView' }"
              >
                SignUp
              </router-link>
            </nav>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <div
      style="
        min-height: 80vh;
        display: flex;
        align-items: center;
        /* margin-top: 200px; */
      "
    >
      <div
        style="
          background-color: rgb(240, 157, 170);
          color: black;
          width: auto;
          padding: 50px;
          border: 10px solid black;
          border-radius: 10%;
          margin: auto;
        "
      >
        <img
          src="@/assets/couple1.png"
          alt=""
          width="150px"
          style="margin-bottom: 30px"
        />
        <!-- <h1>회원가입</h1> -->
        <form @submit.prevent="signUp" style="text-align: left">
          <label for="username">아이디 : </label>
          <input
            type="text"
            id="username"
            v-model="username"
            style="float: right"
          /><br />

          <label for="password1"> 비밀번호 : </label>
          <input
            type="password"
            id="password1"
            v-model="password1"
            style="float: right"
          /><br />

          <label for="password2"> 비밀번호 확인 : </label>
          <input
            type="password"
            id="password2"
            v-model="password2"
            style="float: right"
          /><br />

          <label for="name"> 이름 : </label>
          <input
            type="text"
            id="name"
            v-model="name"
            style="float: right"
          /><br />

          <label for="region"> region : </label>
          <select
            name="region"
            id="region"
            v-model="selecregion"
            style="width: 202px; height: 30px; float: right"
          >
            <option v-for="region in regions" :key="region">
              {{ region }}
            </option></select
          ><br />

          <label for="gender"> gender : </label>
          <select
            name="gender"
            id="gender"
            v-model="selecgender"
            style="width: 202px; height: 30px; float: right"
          >
            <option v-for="gender in genders" :key="gender">
              {{ gender }}
            </option></select
          ><br />

          <label for="nickname"> 닉네임 : </label>
          <input
            type="text"
            id="nickname"
            v-model="nickname"
            style="float: right"
          /><br />

          <input
            type="submit"
            value="회원가입"
            @click="signUp"
            class="btn btn-dark"
            style="width: 350px; margin-bottom: 30px"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignUpView",
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      name: null,
      nickname: null,
      selecgender: null,
      selecregion: null,
      genders: ["남", "여"],
      regions: [
        "서울",
        "경기",
        "강원",
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
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname
      const genders = this.selecgender
      const regions = this.selecregion
      const name = this.name
      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
        nickname: nickname,
        genders: genders,
        regions: regions,
        name: name,
      }
      this.$store.dispatch("signUp", payload)
      console.log(payload)
    },
  },
}
</script>

<style>
.navbar.navbar-dark.bg-dark {
  background-color: rgb(240, 157, 170) !important;
}
label {
  margin-bottom: 10px;
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
