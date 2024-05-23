<template>
    <div class="container">
      <h1>영화 추천</h1>
        
      {{ userinfo }}

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
            <p>{{ props.userinfo[0].era }}</p>
            <!-- 이거 함수 처리 -->

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
    import { ref } from 'vue'

    const props = defineProps({
        userinfo: Array
    })
    
    const movieData = data

    const movielist_year = ref([]);

    const era_list = [
        {'title': 'bf1970','smaller': 1970, 'larger': 1970},
        {'title': '1970s', 'smaller': 1970, 'larger': 1980},
        {'title': '1980s', 'smaller': 1970, 'larger': 1980},
        {'title': '1990s', 'smaller': 1970, 'larger': 1980},
        {'title': '2000s', 'smaller': 1970, 'larger': 1980},
        {'title': '2010s', 'smaller': 1970, 'larger': 1980},
        {'title': 'af2020', 'smaller': 1970, 'larger': 1980}
    ]

    const filter_year = function (data) {
        for (const movie of data){
            const release_year = movie.fields.release_date.slice(0, 4)

            const new_year = parseInt(release_year, 10)

            if (new_year >= 1970 && new_year < 1980){
                movielist_year.value.push(toString(new_year))
            }
        }
    }

    filter_year(movieData)


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
  