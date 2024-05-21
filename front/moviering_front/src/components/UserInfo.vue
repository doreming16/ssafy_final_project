<template>
  <div class="user_info_container">
    <p style="margin-bottom: 70px;">back to <RouterLink :to="{ path: '/accounts' }">accounts</RouterLink></p>

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
</style>
