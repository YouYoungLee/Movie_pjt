<template>
    <div>
        <swiper class="swiper" :options="swiperOption">
            <movie-card-2
            v-for="movie in movieList"
            :key="movie.id"
            :movie="movie"
            >
            {{movie.title}}
        </movie-card-2>
        <div class="swiper-button-prev" slot="button-prev">후후</div>
      <div class="swiper-button-next" slot="button-next">후후</div>
    </swiper>
</div>
</template>
    
    <script>
    import { Swiper } from "vue-awesome-swiper";
import MovieCard2 from './MovieCard2.vue';
    
    export default {
      name: "MovieCard2",
      components: {
          MovieCard2,
          Swiper,
      },
      props: {
        movieList: Array,
      },
      data() {
        return {
          swiperOption: {
            slidesPerView: 6,
            spaceBetween: 5,
            slidesPerGroup: 5,
            loopFillGroupWithBlank: true,
            pagination: {
              el: ".swiper-pagination",
              clickable: true,
            },
            navigation: {
              nextEl: ".swiper-button-next",
              prevEl: ".swiper-button-prev",
            },
          },
        };
      },
      created(){
        console.log(this.movieList,'잉????')
      }
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
    
    .swiper {
  margin-bottom: 2vw;
}
    
    </style>
    