<template>
  <div class="accounts_container">
    <!-- <h1>Accounts</h1> -->
    <!-- <RouterLink :to="{ path: '/accounts/userinfo' }"> -->
    <button class="userinfo_button" @click="toUserInfo">나의 영화 취향 입력하기</button>
    <!-- </RouterLink> -->
    <div>
      <RouterLink :to="{ path: '/accounts/login' }">
        <button class="accounts_button">로그인</button>
      </RouterLink>
      <RouterLink :to="{ path: '/accounts/signup' }">
        <button class="accounts_button">회원가입</button>
      </RouterLink>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { useRouter, RouterLink, RouterView } from "vue-router";
import UserInfo from "@/components/UserInfo.vue";

const router = useRouter();

const toUserInfo = function () {
  router.push({ name: "userinfo" });
};
</script>

<style scoped>
.accounts_container {
  text-align: center;
}
.accounts_button{
  font-family: SUITE;
  font-size: 15px;
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
  font-size: 20px;
  color: white;
  border: none;
  border-bottom: 2px solid pink;
  background-color: transparent;
  margin: 50px;
  cursor: pointer;
}
</style>
