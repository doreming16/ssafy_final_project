<template>
    <div>
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
  
      <div class="row2">
        <p id="question">이 영화, 어떠셨나요?</p>
        <div>
          <input type="radio">
          <img v-for="star in 1" value='1' class="star" src="../icons/star1.png" alt="icon_star" />
        </div> 
        <div>
          <input type="radio">
          <img v-for="star in 2" value='2' class="star" src="../icons/star1.png" alt="icon_star" />
        </div> 
        <div>
          <input type="radio">
          <img v-for="star in 3" value='3' class="star" src="../icons/star1.png" alt="icon_star" />
        </div> 
        <div>
          <input type="radio">
          <img v-for="star in 4" value='4' class="star" src="../icons/star1.png" alt="icon_star" />
        </div> 
        <div>
          <input type="radio">
          <img v-for="star in 5" value='5'  class="star" src="../icons/star1.png" alt="icon_star" />
        </div>
        <!-- <div class="count_stars">
          <div v-for="count in count_stars">
            <img class="star" src="../icons/star1.png" alt="icon_star" />
          </div>
        </div> -->
      </div>
  
      <div class="row3">
        <form>
          <input class="comment" type="text" />
          <input class="submit_button" type="submit" value="입력" />
        </form>
      </div>
  
      <div class="row4">
        <div v-for="count in count_stars" class="box_comment">
          <div class="title_comment">
            <div class="user_comment">user1</div>
            <div class="count_stars">
              <div v-for="count in count_stars">
                <img
                  class="star_comment"
                  src="../icons/star1.png"
                  alt="icon_star"
                />
              </div>
            </div>
          </div>
          <div>show Comment here</div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from "axios";
  import { ref, onMounted } from "vue";
  import { RouterLink, RouterView } from "vue-router";
  import { useRoute } from "vue-router";
  import data from '@/fixtures/movies2.json'
  
  const route = useRoute()
  const movie = ref('')
  for (const datum of data) {
    if (datum.pk == route.params.id) {
      movie.value = datum.fields
    }
  }
  
  const count_stars = ref(4);
  </script>
  
  <style scoped>
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
  