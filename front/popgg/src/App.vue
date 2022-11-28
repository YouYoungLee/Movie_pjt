<template>
  <div id="app">
    <aHeader v-if="token" />
    <!-- <nav>
      <router-link :to="{ name: 'MovieView' }">Movie List</router-link> |
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> |
      <router-link :to="{ name: 'CommunityView' }">Community</router-link> |
      <router-link :to="{ name: 'Login' }">Login</router-link> |
      <router-link :to="{ name: 'Chat' }">Chat</router-link> |
    </nav> -->
    <router-view />
  </div>
</template>

<script>
import aHeader from "./components/layout/aHeader"

export default {
  name: "app",
  components: {
    aHeader,
  },
  computed: {
    token() {
      return this.$store.state.token
    },
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}



nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: white;
  font-size: large;
}

</style>
