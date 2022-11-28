<template>
  <div style="background-color: pink; margin-top: 130px">
    <h1>영화 순위</h1>
    <br />
    <movie-card
      v-for="(movie, idx) in gmovies"
      :key="`movie-${idx}`"
      :movie="movie"
      style="float: left"
    >
    </movie-card>
    <!-- </div> -->
    <!-- <swiper class="swiper" :options="swiperOption"> -->
    <!-- <movie-card-2
        v-for="movie in gmovies"
        :key="movie.id"
        :movie="movie"
      ></movie-card-2> -->
    <!-- <div class="swiper-button-prev" slot="button-prev">이</div> -->
    <!-- <div class="swiper-button-next" slot="button-next">아</div> -->
    <!-- <div class="swiper-pagination" slot="pagination"></div> -->
    <!-- </swiper> -->
  </div>
</template>

<script>
// import Swiper from "vue-awesome-swiper"
// import MovieCard2 from "../components/MovieCard2.vue"
import MovieCard from "../components/MovieCard.vue"

export default {
  name: "MovieView",
  components: {
    // Swiper,
    // MovieCard2,
    MovieCard,
  },
  computed: {
    gmovies() {
      return this.$store.state.gmovies
    },
  },
  // data() {
  //   return {
  //     swiperOption: {
  //       slidesPerView: 6,
  //       spaceBetween: 5,
  //       slidesPerGroup: 5,
  //       loopFillGroupWithBlank: true,
  //       pagination: {
  //         el: ".swiper-pagination",
  //         clickable: true,
  //       },
  //       navigation: {
  //         nextEl: ".swiper-button-next",
  //         prevEl: ".swiper-button-prev",
  //       },
  //     },
  //   }
  // },
  created() {
    console.log(this.gmovies, "호호")
    this.$store.dispatch("getGMovies")
    if (this.$store.state.user_id == null) {
      console.log("아이디널값!")
      this.$store.dispatch("Usernametemp", this.$store.state.username)
    }
    console.log(this.$store.state.user_id, "@@@@@@@@@@@@@@@@@@@@@@@@@")
  },
  methods: {},
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
