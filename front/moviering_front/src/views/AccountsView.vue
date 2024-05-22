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
      
      <div>
        <p>나의 영화 취향</p>
        <div>
          받은 데이터 리스트 나열~~
        </div>
        <button class="userinfo_button" @click="toUserInfo">데이터 입력하기</button>
      </div>

      {{ userInfo }}

    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, RouterLink, RouterView } from "vue-router";
import UserInfo from "@/components/UserInfo.vue";
import axios from 'axios';
import { ref, onMounted } from 'vue';

const router = useRouter();

const toUserInfo = function () {
  router.push({ name: "userinfo" });
};

 
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
  margin: 20px;
  cursor: pointer;
}
</style>
