<template>
  <tr
    @click="move()"
    style="
      border-bottom: 1px solid white;
      border-top: 1px solid white;
      padding: 10px;
    "
  >
    <td style="width: 10%; text-align: center">{{ article.user_region }}</td>
    <td style="width: 20%">
      <img
        :src="`https://image.tmdb.org/t/p/w342${movie.poster_path}`"
        alt="영화 이미지"
        style="border: 5px; height: 7rem; float: left; margin-right: 1rem"
      />
      <span
        style="
          display: table-cell;
          height: 7rem;
          text-align: left;
          vertical-align: middle;
        "
      >
        {{ movie.title }}
      </span>
    </td>
    <td style="width: 10%; text-align: center">{{ article.cinema }}</td>
    <td style="width: 25%; text-align: center">{{ article.title }}</td>
    <td style="width: 15%; text-align: center">{{ article.user_nickname }}</td>
    <td style="width: 20%; text-align: center">
      {{ article.updated_at.substring(0, 10) }}
      <br />
      {{ article.updated_at.substring(11, 16) }}
    </td>
  </tr>
</template>

<script>
import router from "@/router"

export default {
  name: "ArticleCard",
  props: {
    article: Object,
  },
  data() {
    return {
      movie_id: null,
    }
  },
  computed: {
    movie() {
      return this.$store.state.movies[this.article.movie_title - 1]
    },
  },
  methods: {
    move() {
      router.push({ name: "ArticleDetail", params: { id: this.article.id } })
    },
  },
}
</script>

<style>
tr {
  background-color: pink;
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
