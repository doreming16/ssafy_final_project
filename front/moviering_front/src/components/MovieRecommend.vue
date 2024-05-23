<template>
    <div class="container">
      <h1>영화 추천</h1>
        
      <!-- {{ userinfo }} -->
      <!-- {{ props.userinfo }} -->
        <p>myGender : {{ myGender }}</p>

        <div class="container">
            <h2 class="main_subtitle">장르별 추천</h2>
            <p>myGenre: {{ myGenre }}</p>
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
            <p>myYear: {{ myYear }}</p>

            <div class="movie_list_all" >
                <div v-for="movie in final_list">
                    <RouterLink :to="{ name: 'movie_detail_page', params: { id : movie.pk }}">
                        <!-- <img class="poster_main" :src="`https://image.tmdb.org/t/p/w300/${movie.fields.poster_path}`" alt="Image"> -->
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

    // 연도별 filter
    const movielist_filtered = ref([]);

    // 새로 로그인해서 들어올 때 userinfo를 바로 못찾는건지 에러가 남 !
    // 한 번 주석처리했다가 다시 풀면 작동됨 --- async 문젠가 ?
    // props.userinfo[0].blahblah    이런 류를 주석처리하면 에러 안남
    // promise에서 저 blahblah를 찾을 수 없다
    // const myYear = props.userinfo[0].era

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
                movielist_filtered.value.push(movie)
            }
        }
    }

    filter_year(movieData)
    console.log(movielist_filtered) // movielist_filter 1차 완성


    // 장르별 filter
    // const movielist_genre = ref([]);
    // const myGenre = props.userinfo[0].favorite_genre
    const filter_genre = function (data) {
        
    }


    // 성별 filter
    // const myGender = props.userinfo[0].gender
    const filter_gender = function (data) {

    }

    const final_list = movielist_filtered.value
    console.log(final_list)

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
  