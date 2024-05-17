<template>
  <div class="accounts_container">
    <h1>Accounts</h1>
    <RouterLink :to="{ path: '/accounts/login' }">
      <button>로그인</button>
    </RouterLink>
    <RouterLink :to="{ path: '/accounts/signup' }">
      <button>회원가입</button>
    </RouterLink>
    <!-- <RouterLink :to="{ path: '/accounts/userinfo' }"> -->
    <button @click="toUserInfo">UserInfo</button>
    <!-- </RouterLink> -->
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
h1 {
  color: white;
}
</style>
