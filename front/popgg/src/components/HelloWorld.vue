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
                style="font-size: 20px"
              >
                Login
              </router-link>
            </nav>
          </b-navbar-nav>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <div style="margin-top: 200px">
      <img
        src="@/assets/man1.png"
        alt=""
        style="width: 200px; display: inline; float: left; margin-left: 5%"
      />
      <span style="margin-top: 150px; font-size: 100px"
        >아직도 혼자 영화 보니?</span
      >
      <img
        src="@/assets/woman1.png"
        alt=""
        style="width: 200px; float: right; margin-right: 5%"
      />
    </div>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <button class="btn btn-dark" style="width: 700px; height: 160px">
      <router-link
        class="text-decoration-none mx-3 col-4"
        :to="{ name: 'SignUpView' }"
        style="text-decoration: none; color: white; font-size: 80px"
      >
        회원가입 바로가기
      </router-link>
    </button>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: white;
}
</style>
