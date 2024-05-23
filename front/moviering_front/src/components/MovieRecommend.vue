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
    import { ref } from 'vue'

    const movieData = data

    const movielist_year = ref([]);

    const era_list = [
        {'title': 'bf1970','kor': '1970년대 이전'},
        {'title': '1970s','kor': '1970년대',},
        {'title': '1980s','kor': '1980년대',},
        {'title': '1990s','kor': '1990년대',},
        {'title': '2000s','kor': '2000년대',},
        {'title': '2010s','kor': '2010년대',},
        {'title': 'af2020','kor': '2020년 이후'}
    ]

    const filter_year = function (data) {
        for (const movie of data){
            const release_year = movie.fields.release_date.slice(0, 4)
            // console.log(release_year)
            // console.log(typeof(release_year))

            // const new_year = Number(release_year)
            const new_year = parseInt(release_year, 10)
            // console.log(typeof new_year)

            if (new_year >= 1970 && new_year < 1980){
                console.log(`filtered: ${new_year}`)
                movielist_year.value.push(toString(new_year))
            }
        }
    }

    filter_year(movieData)
    console.log(movielist_year.value)

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
  