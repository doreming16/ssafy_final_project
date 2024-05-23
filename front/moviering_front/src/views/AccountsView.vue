<template>
  <div class="accounts_container">
    <p style="margin-bottom: 70px;"><RouterLink :to="{ path: '/' }" class="back_tag">back</RouterLink></p>
    <button class="userinfo_button" @click="toUserInfo">Input My Data</button>
    
    <UserInfoDetail />

    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, RouterLink, RouterView } from "vue-router";
import UserInfoDetail from "@/components/UserInfoDetail.vue";
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
.back_tag{
  color: white;
  text-decoration: none;
}
.back_tag:hover{
  color: pink;
}
.userinfo_button{
  font-family: SUITE;
  font-size: 15px;
  color: white;
  /* border: none; */
  border: 2px solid pink;
  padding: 10px 15px;
  background-color: transparent;
  margin: 30px 0 50px 0;
  cursor: pointer;
}
.userinfo_button:hover{
  background-color: pink;
  color: black;
}
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
.span_bracket{
  color: pink;
  font-size: 30px;
  margin: 0 10px;
}
.bracket_large{
  font-size: 400px;
  font-weight: lighter;
  color: pink;
  margin: 0 25px;
}
</style>
