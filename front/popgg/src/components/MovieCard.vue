<template>
  <router-link
    :to="{
      name: 'MovieDetail',
      params: { id: movie.id },
    }"
    style="
      text-decoration-line: none;
      color: black;
      border: 10px solid;
      width: 48%;
      height: 470px;
      border-radius: 10px;
      margin: 1%;
    "
  >
    <b-card
      :img-src="`https://image.tmdb.org/t/p/w342${movie.poster_path}`"
      img-height="450px"
      alt="영화 이미지"
      style="background-color: white; color: black; border-radius: 5px"
      img-left
      class="mb-3"
    >
      <b-card-text>
        <h4
          class="mb-0"
          style="
            text-align: center;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: break-word;
            height: auto;
            display: -webkit-box;
            -webkit-line-clamp: 1;
            -webkit-box-orient: vertical;
            overflow: hidden;
            content: '...';
          "
        >
          {{ movie.title }}
        </h4>
        <br />
        <span class="mb-0" style="float: left"
          >상영시간 : {{ movie.runnig_time }}분</span
        >
        <span class="mb-0" style="float: right"
          >개봉일 :{{ movie.release_data }}</span
        >
        <br />
        <span class="mb-0" style="float: left">장르 : {{ movie.genre }}</span>
        <span class="mb-0" style="float: right"
          >평점 : {{ movie.vote_average }}</span
        >
        <br />
        <br />
        <br />
        <p
          class="mb-0"
          style="
            text-align: left;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: break-word;
            display: -webkit-box;
            -webkit-line-clamp: 11;
            -webkit-box-orient: vertical;
            overflow: hidden;
            content: '...';
          "
        >
          줄거리 : {{ movie.overview }}
        </p>
        <!-- <template #footer> -->
        <!-- </template> -->
      </b-card-text>
    </b-card>
  </router-link>
</template>

<script>
export default {
  name: "MovieCard",
  props: {
    movie: Object,
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
p {
  text-align: left;
}
</style>
