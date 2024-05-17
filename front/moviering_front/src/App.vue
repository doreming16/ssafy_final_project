<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <div>
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
div {
  color: white;
}
nav {
  padding: 20px;
  margin-bottom: 50px;
  height: 50px;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  border-bottom: 1px solid rgb(255, 220, 220);
}
</style>
