<script setup>
import { RouterLink, RouterView } from "vue-router";
import data from '@/fixtures/movies2.json'
</script>

<template>
  <div class="container">
    <div class="main_row1">
      <p class="main_subtitle">Today's Movie</p>
      <img src="../img/movie4.jpeg" alt="home_movie_image" />
    </div>
    <span style="margin: 30px 0px;">---</span>
    <RouterLink :to="{ path: '/accounts' }">Accounts</RouterLink>
    <span style="margin: 30px 0px;">---</span>
    <br />
    <RouterLink :to="{ path: '/movies' }">Movies</RouterLink>
    <RouterView />
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">Movie List(all)</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <img class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">Movie List(average > 7.5)</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <img v-if="movie.fields.vote_average > 7.5" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">Movie List(release date > 2000-00-00 )</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <img v-if="movie.fields.release_date > '2000-00-00'" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">Movie List(music)</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <img v-if="movie.fields.genre_ids.includes(10402)" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
      </div>
    </div>

  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 100px;
}
.main_row1{
  display: flex;
  flex-direction: column;
  align-items: center;
}
.main_subtitle{
  font-size: 20px;
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
