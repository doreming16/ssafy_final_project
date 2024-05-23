<template>
    <div id="go_back_link">
      <RouterLink :to="{ name: 'home' }">뒤로가기</RouterLink>
    </div>
    <div class="container">
      <div class="row1">
        <div class="box_left">
          <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="detail_movie_image" />
        </div>
        <div id="center_line"></div>
        <div class="box_right">
          <p id="movie_title">제목: {{ movie.title }}</p>
          <p>장르 : {{ movie.genre_ids }}</p>
          <p><b>줄거리</b> : {{ movie.overview }}</p>
          <p><span>{{ movie.release_date }}</span> 개봉</p>
          <p>평점 : {{ movie.vote_average }}</p>
        </div>
      </div>

      <ReviewView :id="moviePk"/>
    </div>
  </template>
  
  <script setup>
  import axios from "axios";
  import { ref, onMounted } from "vue";
  import { RouterLink, RouterView } from "vue-router";
  import { useRoute } from "vue-router";
  import data from '@/fixtures/movies2.json'
  import ReviewView from '@/views/ReviewView.vue'
  
  const route = useRoute()
  const movie = ref(null)
  for (const datum of data) {
    if (datum.pk == route.params.id) {
      movie.value = datum.fields
    }
  }

  const moviePk = ref(parseInt(route.params.id))
</script>
  
  <style scoped>
  #go_back_link{
    text-align: center;
    
  }
  a{
    color: white;
    font-family: SUITE;
    font-size: 15px;
    text-decoration: none;
    padding: 5px 8px;
    border: 1px solid pink;
    background-color: transparent;
    margin: 15px;
    cursor: pointer;
  }
  .container .row1 {
    font-family: SUITE;
    display: flex;
    justify-content: center;
    margin: 50px 0px;
  }
  img {
    height: 500px;
  }
  #center_line {
    margin: 0px 50px;
    width: 0.5px;
    height: 500px;
    background-color: white;
  }
  .box_right {
    font-family: SUITE;
    width: 500px;
  }
  .list_name {
    font-weight: bold;
  }
  #movie_title {
    font-size: 30px;
  }
  #question {
    font-size: 25px;
    color: rgb(255, 204, 204);
  }
  .row2 {
    font-family: SUITE;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 50px 0px;
  }
  .count_stars {
    display: flex;
  }
  .star {
    width: 20px;
    height: 20px;
    margin: 5px;
  }
  .comment {
    width: 800px;
    height: 200px;
    background-color: transparent;
    border: 1px solid skyblue;
  }
  .row3 {
    display: flex;
    justify-content: center;
  }
  .submit_button {
    margin: 20px;
    width: 40px;
    height: 25px;
  }
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .title_comment {
    display: flex;
  }
  .box_comment {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 20px 0px;
  }
  .star_comment {
    width: 10px;
    height: 10px;
  }
  .user_comment {
    margin: 0px 10px;
  }
  </style>
  