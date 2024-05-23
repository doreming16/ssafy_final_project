<template>
    <div>
      <h2 v-if="store.user" style="color: pink;">{{ store.user.username }}님의 영화 취향</h2>

      <div class="form_box" style="display: flex; justify-content: center; align-items: center;">
        <span class="bracket_large">[</span>
        <div v-for="info in userInfo">
          <p v-if="info.isSpecial === true" class="info_item">
            기념일 관련 영화를 추천받고 싶어요
          </p>
          <p v-if="info.isSpecial === false" class="info_item">
            기념일 관련 영화를 추천받고 싶지 않아요
          </p>
  
          <p v-if="info.gender === 'male'" class="info_item">
            남성
          </p>
          <p v-else class="info_item">
            여성
          </p>
  
          <p>
            <span v-for="era in era_list">
              <span v-if="era.eng === info.era" class="info_item">
                {{ era.kor }}
              </span>
            </span>
          </p>
          
          <p class="info_item">
            <span v-for="genre_pk in info.favorite_genre">
              <span v-for="genre in data">
                <span v-if="genre_pk === genre.pk" style="margin: 5px;">
                  {{ genre.fields.name }}
                </span>
              </span>
            </span>
          </p>
          
          <p class="info_item">
            {{ info.viewing_environment }}
          </p>
  
          <p class="info_item">
            {{ info.birthday }}
          </p>
          
        </div>
        <span class="bracket_large">]</span>
      </div>

      <p style="margin-bottom: 70px;">
        <RouterLink
          :to="{ path: '/movies/recommend/:id' }"
          class="back_tag">
        영화 추천받기
        </RouterLink>
      </p>
      <!-- 개인 데이터 추천 페이지로 이동해야함 -->
    </div>
  </template>
  
  <script setup>
  import { useRouter, RouterLink, RouterView } from "vue-router";
  import axios from 'axios';
  import { ref, onMounted } from 'vue';
  import data from '@/fixtures/genres.json'
  import { useCounterStore } from "@/stores/counter";
  const store = useCounterStore()

  const era_list = [
    {
      'eng': 'bf1970',
      'kor': '1970년대 이전',
    },
    {
      'eng': '1970s',
      'kor': '1970년대',
    },
    {
      'eng': '1980s',
      'kor': '1980년대',
    },
    {
      'eng': '1990s',
      'kor': '1990년대',
    },
    {
      'eng': '2000s',
      'kor': '2000년대',
    },
    {
      'eng': '2010s',
      'kor': '2010년대',
    },
    {
      'eng': 'af2020',
      'kor': '2020년 이후'
    }]
  
  
  const userInfo = ref([]);
  
  const getUserInfo = function () {
    axios({
      method: 'get',
      url: 'http://localhost:8000/accounts/api/userinfo/',
    }).then(res => {
      userInfo.value = res.data
      console.log(res.data)
    }).catch(err =>{
      console.log(err)
    })
  }
  
  onMounted(() => {
    getUserInfo()
  });
  
  </script>
  
  <style scoped>
  .form_box{
    margin: 0;
    height: 400px;
  }
  .info_item{
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 30px 0;
  }
  .bracket_large{
    font-size: 400px;
    font-weight: lighter;
    color: pink;
    margin: 0 25px;
  }
  .back_tag{
  color: white;
  text-decoration: none;
}
.back_tag:hover{
  color: pink;
}
  </style>
  