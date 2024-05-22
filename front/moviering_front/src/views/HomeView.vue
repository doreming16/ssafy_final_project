<script setup>
import { RouterLink, RouterView } from "vue-router";
import data from '@/fixtures/movies2.json'
</script>

<template>
  <div class="container">
    <div>
      <RouterLink :to="{ path: '/accounts/login' }">
        <button class="accounts_button">로그인</button>
      </RouterLink>
      <RouterLink :to="{ path: '/accounts/signup' }">
        <button class="accounts_button">회원가입</button>
      </RouterLink>
    </div>
    
    <div class="form_divide" style="margin: 30px 0px;">
        ---
    </div>
      

    <div class="main_row1">
      <p class="main_subtitle">Today's Movie</p>
      <RouterLink :to="{ name: 'movie_detail_page', params: { id : 271714 }}">
        <img src="https://image.tmdb.org/t/p/w300/slLFGhzADsFdFzrrISsDo4X1Gwf.jpg" alt="home_movie_image" />
      </RouterLink>
    </div>
    <span style="margin: 30px 0px;">---</span>
    <RouterLink :to="{ path: '/accounts' }">My Movie Data</RouterLink>
    <span style="margin: 30px 0px;">---</span>
    <br />
    <RouterLink :to="{ path: '/movies' }">Movie Recommendation</RouterLink>
    <RouterView />
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">Movie List - ALL</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
          <img class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
        </RouterLink>
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">평점 8 이상</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
          <img v-if="movie.fields.vote_average > 8" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
        </RouterLink>
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">2000년 이후 개봉</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
          <img v-if="movie.fields.release_date > '2000-01-01'" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
        </RouterLink>
      </div>
    </div>
    <span style="margin: 30px 0px;">---</span>

    <p class="main_subtitle">음악 장르</p>
    <div class="movie_list_all" >
      <div v-for="movie in data">
        <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
          <img v-if="movie.fields.genre_ids.includes(10402)" class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
        </RouterLink>
      </div>
    </div>
    
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-bottom: 100px;
}
.accounts_button{
  font-family: SUITE;
  font-size: 13px;
  color: white;
  /* border: none; */
  /* border-radius: 5px; */
  padding: 5px 8px;
  border: 1px solid pink;
  background-color: transparent;
  margin: 15px;
  cursor: pointer;
}
.accounts_button:hover{
  background-color: pink;
  color: black;
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
.movie_list_all{
  display: flex;
  width: 100%;
}
.poster_main{
  width: 150px;
  height: 80%;
  margin: 10px;
  border: 1px solid white;
}
a {
  color: white;
  text-decoration: none;
}
</style>
