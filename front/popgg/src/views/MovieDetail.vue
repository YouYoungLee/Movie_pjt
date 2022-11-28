<template>
  <div style="background-color: pink; margin-top: 120px">
    <h1 style="margin-bottom: 30px">영화 정보</h1>
    <div class="row" style="margin: 0">
      <div style="width: 50%">
        <img
          :src="`https://image.tmdb.org/t/p/w342${movie.poster_path}`"
          alt="영화 이미지"
          style="border: 18px inset; border-radius: 1%; width: 90%"
        />
      </div>
      <div style="width: 50%">
        <iframe
          width="100%"
          height="500"
          :src="movie_url"
          frameborder="0"
          allowfullscreen
        >
        </iframe>
        <b-card
          title="줄거리"
          header-tag="header"
          footer-tag="footer"
          style="width: 100% padding: 0px"
        >
          <template #header>
            <br />
            <h2 class="mb-0">{{ movie.title }}</h2>
            <h5 class="mb-0">감독: {{ movie.director }}</h5>
            <br />
          </template>
          <h5 class="container" style="text-align: left">
            {{ movie.overview }}
          </h5>
          <template>
            <h5 class="mb-0" style="text-align: left">
              평점 : {{ movie.vote_average }}
            </h5>
            <h5 class="mb-0" style="text-align: left">
              개봉 일 :{{ movie.release_data }}
            </h5>
            <h5 class="mb-0" style="text-align: left">
              장르 :{{ movie.genre }}
            </h5>
            <h5 class="mb-0" style="text-align: left">
              배우 :{{ movie.actor }}
            </h5>
            <h5 class="mb-0" style="text-align: left">
              상영 시간 : {{ movie.runnig_time }}분
            </h5>
          </template>
        </b-card>
      </div>
    </div>

    <movie-comments :movie_id="movie_id"> </movie-comments>
  </div>
</template>

<script>
import axios from "axios"
import MovieComments from "../components/MovieComments.vue"

const API_URL = "http://43.201.136.140:8000"
// const API_URL = "http://127.0.0.1:8000"

export default {
  components: { MovieComments },
  name: "MovieDetail",
  data() {
    return {
      movie: null,
      movie_id: null,
      movie_url: null,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    },
  },
  created() {
    this.getMovieDetail()
    console.log(this.token, "-------------")
  },
  methods: {
    getMovieDetail() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/gmovie_detail/${this.$route.params.id}/`,
        headers: {
          // Authorization: `Token 953478ef404ae03d3fbc263ae258d254d310b1fc`,
          Authorization: `Token ${this.token}`,
        },
      })
        .then((res) => {
          console.log((this.movie = res.data))
          this.movie_id = this.$route.params.id
          this.movie_url = res.data.video
          console.log(this.movie_url)
        })
        .catch((err) => console.log(err))
    },
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
</style>
