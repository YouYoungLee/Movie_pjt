<template>
  <div>
    <b-navbar
      type="dark"
      variant="dark"
      class="px-5"
      style="
        position: fixed;
        top: 0;
        width: 100%;
        font-weight: bold;
        display: flex;
        justify-content: space-between;
        align-items: center;
      "
    >
      <b-navbar-brand href="/index">
        <img src="@/assets/couple1.png" alt="" style="height: 70px" />
      </b-navbar-brand>
      <b-navbar-brand href="/index">
        <h1 style="font-weight: bold; color: white">POP.GG</h1>
      </b-navbar-brand>

      <!-- <b-navbar-toggle target="nav-collapse"></b-navbar-toggle> -->

      <b-collapse class="justify-content-end" id="nav-collapse" is-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-navbar-nav>
            <nav class="justify-content-end container">
              <router-link
                class="text-decoration-none mx-3 col-4"
                :to="{ name: 'ChatList' }"
              >
                Chatting
              </router-link>
              <router-link
                class="text-decoration-none mx-3 col-4"
                :to="{ name: 'MovieView' }"
              >
                Movie
              </router-link>
              <router-link
                class="text-decoration-none mx-3 col-4"
                :to="{ name: 'CommunityView' }"
              >
                Community
              </router-link>
              <router-link
                class="text-decoration-none mx-3 col-4"
                @click.native="logout"
                :to="{ name: 'HomeView' }"
              >
                LogOut
              </router-link>
            </nav>
            <br />
          </b-navbar-nav>
        </b-navbar-nav>
        {{ $store.state.nickname }}님 환영합니다.
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "aHeader",
  methods: {
    logout() {
      console.log(1)
      this.$store.dispatch("logOut")
    },
  },
}
</script>

<style>
.navbar.navbar-dark.bg-dark {
  background-color: rgb(240, 157, 170) !important;
  position: relative;
  z-index: 2;
}
</style>
