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
    <!-- <div style="height: 200px"></div> -->
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
          width: 400px;
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
        <!-- <h1>Login</h1> -->
        <form @submit.prevent="login">
          <label for="username"></label>
          <input
            type="text"
            id="username"
            v-model="username"
            placeholder="아이디"
            style="margin-bottom: 3px"
          />
          <br />
          <label for="password1"></label>
          <input
            type="password"
            id="password1"
            v-model="password"
            placeholder="비밀번호"
            style="margin-bottom: 3px"
          /><br />
          <input
            type="submit"
            value="로그인"
            @click="login"
            class="btn btn-dark"
            style="width: 210px; margin-bottom: 30px"
          />
          <br />

          <input
            type="submit"
            value="회원가입"
            @click="signup"
            class="btn btn-danger"
            style="margin-left: 42%"
          />
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import router from "@/router"

export default {
  name: "LoginView",
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password,
      }
      this.$store.dispatch("Usernametemp", username)
      this.$store.dispatch("logIn", payload)
    },
    signup() {
      router.push({ name: "SignUpView" })
    },
  },
}
</script>

<style>
.navbar.navbar-dark.bg-dark {
  background-color: rgb(240, 157, 170) !important;
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
