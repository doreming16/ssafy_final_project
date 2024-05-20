<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="navbar">
      <nav>
        <RouterLink
          :to="{ path: '/' }"
          style="color: white; text-decoration: none; font-size: 30px">
          <span>MovieRing</span>
        </RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
@font-face {
	font-family: 'SUITE';
	font-weight: 500;
	src: url('@/assets/fonts/SUITE-Medium.woff2') format('woff2');
}
@font-face {
	font-family: 'SUITE';
	font-weight: 300;
	src: url('@/assets/fonts/SUITE-Light.woff2') format('woff2');
}
@font-face {
	font-family: 'SUITE';
	font-weight: 800;
	src: url('@/assets/fonts/SUITE-ExtraBold.woff2') format('woff2');
}
* {
  font-family: 'SUITE';
}
.navbar {
  display: flex;
  justify-content: center;
}
nav {
  padding: 20px;
  margin-bottom: 50px;
  width: 50%;
  height: 50px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border-bottom: 1px solid rgb(255, 220, 220);
}
</style>
