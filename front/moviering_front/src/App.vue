<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div>
      <nav>
        <div>Logo</div>
        <RouterLink :to="{ path: '/'}">Home</RouterLink>
        <p>Navbar here</p>
      </nav>
    </div>
  </header>


  <RouterView />
</template>

<style scoped>
  nav{
    background-color: gray;
    display: flex
  }
</style>
