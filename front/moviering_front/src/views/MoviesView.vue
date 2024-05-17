<template>
  <div>
    <p>오늘은 <span id="anniv_name">내 생일</span> 이네요!</p>
    <RouterLink :to="{ path: '/movies/detail' }">
      <img src="../img/movie4.jpeg" alt="home_movie_image" />
    </RouterLink>
    <p>
      이런 날, <span id="movie_name">조제, 호랑이 그리고 물고기들</span>은
      어떠세요?
    </p>
    <RouterView />
  </div>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";
const isLogin = ref(false);
</script>

<style scoped>
* {
  text-align: center;
}
#anniv_name {
  color: rgb(254, 168, 182);
  font-size: 40px;
  margin: 10px;
}
#movie_name {
  color: rgb(254, 168, 182);
  font-size: 40px;
  margin: 10px;
}
p {
  font-size: 20px;
}
img {
  width: 500px;
}
</style>
