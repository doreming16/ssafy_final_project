<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div class="navbar">
      <nav>
        <RouterLink
          :to="{ path: '/' }"
          style="color: white; text-decoration: none; font-size: 30px"
        >
          MovieRing
        </RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.container {
  color: white;
}
.navbar {
  color: white;
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
