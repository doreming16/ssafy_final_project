<template>
    <div class="container">
      <h1>영화 추천</h1>
  
        <div class="container">
            <h2 class="main_subtitle">장르별 추천</h2>
            <div class="movie_list_all" >
                <div v-for="movie in data">
                    <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
                        <img class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
                    </RouterLink>
                </div>
            </div>
        </div>

      <span style="margin: 30px 0px;">---</span>

        <div class="container">
            <h2 class="main_subtitle">연도별 추천</h2>
            <div class="movie_list_all" >
                <div v-for="movie in data">
                    <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
                        <img class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image">
                    </RouterLink>
                </div>
            </div>
        </div>

    </div>
  </template>
  
  <script setup>
    import data from '@/fixtures/movies2.json'

    defineProps({
        userinfo: Array
    })
  
  </script>
  
  <style scoped>
    *{
        text-align: center;
    }
    .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 100px;
    width: 100%;
  }
  .movie_list_all{
    display: flex;
    width: 100%;
  }
  </style>
  