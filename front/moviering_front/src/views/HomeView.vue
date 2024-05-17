<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <div class="container">
    <div>
      <img src="../img/movie4.jpeg" alt="home_movie_image" />
    </div>
    <RouterLink :to="{ name: 'accounts' }">Accounts</RouterLink>
    <br />
    <RouterLink :to="{ path: '/movies' }">Movies</RouterLink>
    <RouterView />
  </div>
</template>

<style scoped>
.container {
  text-align: center;
}
h1 {
  color: rgb(83, 123, 255);
}
img {
  width: 250px;
}
a {
  color: white;
  text-decoration: none;
}
</style>
