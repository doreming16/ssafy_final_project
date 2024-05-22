<template>
  <div class="accounts_container">
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
      
      <button class="userinfo_button" @click="toUserInfo">데이터 입력하기</button>
      <div>
        <h2 style="color: pink;">나의 영화 취향</h2>
      </div>
    
      <div v-for="info in userInfo">
        <p v-if="info.isSpecial === true" class="info_item">
          <span class="span_bracket">[</span>
          기념일 관련 영화를 추천받고 싶어요
          <span class="span_bracket">]</span>
        </p>
        <p v-if="info.isSpecial === false" class="info_item">
          <span class="span_bracket">[</span>
          기념일 관련 영화를 추천받고 싶지 않아요
          <span class="span_bracket">]</span>
        </p>

        <p v-if="info.gender === 'male'" class="info_item">
          <span class="span_bracket">[</span>
          남성
          <span class="span_bracket">]</span>
        </p>
        <p v-else class="info_item">
          <span class="span_bracket">[</span>  
          여성
          <span class="span_bracket">]</span>
        </p>

        <p>
          <span v-for="era in era_list">
            <span v-if="era.eng === info.era" class="info_item">
          <span class="span_bracket">[</span>
              {{ era.kor }}
          <span class="span_bracket">]</span>
            </span>
          </span>
        </p>
        
        <p class="info_item">
          <span class="span_bracket">[</span>
          <span v-for="genre_pk in info.favorite_genre">
            <span v-for="genre in data">
              <span v-if="genre_pk === genre.pk" style="margin: 5px;">
                {{ genre.fields.name }}
              </span>
            </span>
          </span>
          <span class="span_bracket">]</span>
        </p>
        
        <p class="info_item">
          <span class="span_bracket">[</span>
          viewing_enviroment : {{ info.viewing_environment }}
          <span class="span_bracket">]</span>
        </p>

        <p class="info_item">
          <span class="span_bracket">[</span>
          생일 : {{ info.birthday }}
          <span class="span_bracket">]</span>
        </p>
        
        
      </div>

    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, RouterLink, RouterView } from "vue-router";
import UserInfo from "@/components/UserInfo.vue";
import axios from 'axios';
import { ref, onMounted } from 'vue';
import data from '@/fixtures/genres.json'

const router = useRouter();

const toUserInfo = function () {
  router.push({ name: "userinfo" });
};

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
.accounts_container {
  text-align: center;
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
.userinfo_button{
  font-family: SUITE;
  font-size: 18px;
  color: white;
  border: none;
  border-bottom: 2px solid pink;
  background-color: transparent;
  margin: 30px;
  cursor: pointer;
}
.info_item{
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 30px 0;
}
.span_bracket{
  color: pink;
  font-size: 30px;
  margin: 0 10px;
}
</style>
