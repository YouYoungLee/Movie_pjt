<template>
  <div>
    <h1>박스오피스 순위 <i class="far fa-thumbs-up"></i></h1>
    <VueSlickCarousel
      :arrows="true"
      :dots="true"
      v-bind="settings"
      style="margin-left: 3%; margin-right: 3%"
      
    >
      <span v-for="movie in movies" :key="movie.id" :movie="movie">
        <h3>{{ movie.id }}위</h3>
        <span>
          <img :src="`https://image.tmdb.org/t/p/w342${movie.poster_path}`" />
        </span>
      </span>
    </VueSlickCarousel>
    <br />
  </div>
</template>

<script>
import VueSlickCarousel from "vue-slick-carousel"
import "vue-slick-carousel/dist/vue-slick-carousel.css"
// optional style for arrows & dots
import "vue-slick-carousel/dist/vue-slick-carousel-theme.css"

export default {
  name: "MovieCard2",
  components: {
    VueSlickCarousel,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    },
  },
  data() {
    return {
      settings: {
        dots: true,
        focusOnSelect: true,
        infinite: true,
        speed: 500,
        slidesToShow: 5,
        slidesToScroll: 5,
        touchThreshold: 5,
      },
    }
  },
  created() {
    console.log(this.movie, "호호호무비")
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
div {
  font-size: 15px;
  font-family: NanumSquareNeo-Variable;
}
</style>
