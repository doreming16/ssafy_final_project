<template>
  <div class="user_info_container">
    <p style="margin-bottom: 70px;"><RouterLink :to="{ path: '/accounts' }" class="back_tag">back</RouterLink></p>

    <h1>UserInfoForm</h1>
    <UserInfoForm />
  </div>
</template>

<script setup>
import UserInfoForm from "@/components/UserInfoForm.vue";
</script>

<style scoped>
a{
  color: white;
}
.user_info_container {
  text-align: center;
}
h1 {
  color: gray;
}
.back_tag:hover{
  color: pink;
}
</style>
