<template>
  <div class="login_container">
    <RouterLink :to="{ path: '/' }">back</RouterLink>
    <h1>Login Page</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" class="login_button" id="username" v-model.trim="username" />
      <br />

      <label for="password">password : </label>
      <input type="password" class="login_button" id="password" v-model.trim="password" />
      <br />

      <input type="submit" class="login_submit_button" value="LogIn" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink, RouterView } from 'vue-router';

const username = ref(null);
const password = ref(null);

const store = useCounterStore();

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped>
a{
  color: white;
  text-decoration: none;
}
a:hover{
  color: pink;
}
.login_container{
  text-align: center;
}
.login_button{
  font-family: SUITE;
  font-size: 15px;
  color: white;
  padding: 5px 8px;
  border: 1px solid pink;
  background-color: transparent;
  margin: 15px;
  cursor: pointer;
}
.login_submit_button{
  font-family: SUITE;
  font-size: 20px;
  color: white;
  padding: 6px 10px;
  border: 3px solid pink;
  background-color: transparent;
  margin: 50px;
  cursor: pointer;
}
.login_submit_button:hover{
  background-color: pink;
  color: black;
}
</style>
