<script setup>
import { RouterLink, RouterView } from "vue-router";
import data from '@/fixtures/movies.json'
</script>

<template>
  <div class="container">
    <div class="main_row1">
      Today's Movie
      <img src="../img/movie4.jpeg" alt="home_movie_image" />
    </div>
    <span style="margin: 30px 0px;">---</span>
    <RouterLink :to="{ path: '/accounts' }">Accounts</RouterLink>
    <span style="margin: 30px 0px;">---</span>
    <br />
    <RouterLink :to="{ path: '/movies' }">Movies</RouterLink>
    <RouterView />
    <span style="margin: 30px 0px;">---</span>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <!-- {{ movie.fields.poster_path }} -->
        <img v-if="movie.fields.vote_average > 7.5" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.main_row1{
  display: flex;
  flex-direction: column;
  align-items: center;
}
h1 {
  color: rgb(83, 123, 255);
}
img {
  width: 250px;
  margin: 15px;
}
.poster_main{
  width: 250px;
  margin: 0;
}
a {
  color: white;
  text-decoration: none;
}
.movie_list_all{
  display: flex;
}
</style>
