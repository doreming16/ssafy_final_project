<template>
  <div class="user_info_container">
    <p style="margin-bottom: 70px;"><RouterLink :to="{ path: `/accounts/${user.id}` }" class="back_tag">back</RouterLink></p>

    <h1>UserInfoForm</h1>
    <UserInfoForm />

    <p style="margin-bottom: 70px;">
        <RouterLink
          :to="{ path: '/movies/recommend/:id' }"
          class="back_tag">
        영화 추천받기
        </RouterLink>
    </p>
  </div>
</template>

<script setup>
import UserInfoForm from "@/components/UserInfoForm.vue";
import { RouterLink } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const user = store.user

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
