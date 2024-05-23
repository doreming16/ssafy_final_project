<script setup>
import { RouterLink, RouterView } from "vue-router";
import data from '@/fixtures/movies2.json'
import anniversary_recommend from '@/fixtures/anniversary_recommend.json'
import { useCounterStore } from '@/stores/counter'
import { onMounted } from "vue";

const authstore = useCounterStore()
const authUser = authstore.user
const authToken = localStorage.getItem('authToken')

const logOut = () => {
  authstore.logOut()
}

if (authstore.token) {
  onMounted(() => {
    authstore.get_user_profile()
  });
}

// 오늘 날짜를 가져오는 Date 객체 생성
const today = new Date();

// 연도, 월, 일을 추출
const year = today.getFullYear();
const month = String(today.getMonth() + 1).padStart(2, '0'); // 월은 0부터 시작하므로 +1
const day = String(today.getDate()).padStart(2, '0'); // 날짜를 두 자리로 유지

// 원하는 형식으로 조합
const formattedDate = `${year}-${month}-${day}`;

// console.log(formattedDate); // "2024-05-24" 형식으로 출력


</script>

<template>
  <div class="container">
    <div v-if="authUser">
      <p>
        안녕하세요, {{ authUser.username }} 님.
      </p>
      <p>
        {{ authUser.username }} 님의 user.id는 [ {{ authUser.id }} ] 입니다.
      </p>
    </div>

    <div style="display: flex;">  

      <!-- 로그인, 로그아웃 버튼 toggle -->
      <div v-if="authToken">
          <button @click="logOut" class="accounts_button">로그아웃</button>
      </div>
        
      <div v-else>
        <RouterLink :to="{ path: '/accounts/login' }">
          <button class="accounts_button">로그인</button>
        </RouterLink>
      </div>
        
      <div>
        <RouterLink :to="{ path: '/accounts/signup' }">
          <button class="accounts_button">회원가입</button>
        </RouterLink>
      </div>

    </div>
    
    <div class="form_divide" style="margin: 50px 0px;">
        ---
    </div>
      

    <div class="main_row1">
      <p class="main_subtitle">Today's Movie</p>
        <div v-for="anniversary in anniversary_recommend">
          <div class="aniversary_movies" v-if="anniversary.date === formattedDate">
            <div v-for="movie in anniversary.movies">
              <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
                <img id="todays_movie_img" :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" alt="home_movie_image" />
              </RouterLink>
            </div>
            <p>오늘은 {{ anniversary.name }}입니다.</p>
            <p>관련된 영화를 추천 드립니다.</p>
          </div>
        </div>
    </div>
    <span style="margin: 80px 0px;">---</span>
    <RouterLink v-if="authUser" :to="{ path: `/accounts/${authUser.id}` }">My Movie Data</RouterLink>
    <RouterLink v-else :to="{ path: '/accounts/login' }">Please Login First</RouterLink>
    <span style="margin: 80px 0px;">---</span>
    
    <RouterLink v-if="authUser" :to="{ path: `/movies/recommend/${authUser.id}` }">Recommendation for You</RouterLink>
    <RouterLink v-else :to="{ path: '/accounts/login' }">Please Login First</RouterLink>
    <RouterView />
    <span style="margin: 80px 0px;">---</span>

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
.anniversary_movies{
  display: inline-block;
}
#todays_movie_img{
  width: 300px;
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
