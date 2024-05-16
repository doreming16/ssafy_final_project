<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
    <div>
        <h1>Home</h1>
        <p style="color:white;">Move to :</p>
        <RouterLink :to="{ name: 'accounts' }">Accounts</RouterLink>
        <br>
        <RouterLink :to="{ path: '/movies' }">Movies</RouterLink>
        <RouterView />
    </div>
</template>

<style scoped>
h1{
    color: rgb(83, 123, 255);
}
a{
    color: white;
    text-decoration: none;
}
</style>