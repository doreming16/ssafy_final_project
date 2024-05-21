<template>
  <div class="signup_container">
    <p>back to <RouterLink :to="{ path: '/accounts' }">accounts</RouterLink></p>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" class="signup_button" id="username" v-model.trim="username" />
      <br />

      <label for="password1">password : </label>
      <input type="password" class="signup_button" id="password1" v-model.trim="password1" />
      <br />

      <label for="password2">password-Check : </label>
      <input
        type="password"
        class="signup_button"
        id="password2"
        v-model.trim="password2"
      />
      <br />
      <input class="signup_submit_button" type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const store = useCounterStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
a{
  color: white;
}
.signup_container{
  text-align: center;
}
.signup_button{
  font-family: SUITE;
  font-size: 15px;
  color: white;
  padding: 5px 8px;
  border: 1px solid pink;
  background-color: transparent;
  margin: 15px;
  cursor: pointer;
}
.signup_submit_button{
  font-family: SUITE;
  font-size: 20px;
  padding: 6px 10px;
  color: white;
  border: 3px solid pink;
  background-color: transparent;
  margin: 50px;
  cursor: pointer;
}
</style>
