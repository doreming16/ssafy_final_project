<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model.trim="username" />
      <br />

      <label for="password">password : </label>
      <input type="password" id="password" v-model.trim="password" />
      <br />

      <label for="passwordcheck">password-Check : </label>
      <input
        type="passwordcheck"
        id="passwordcheck"
        v-model.trim="passwordcheck"
      />
      <br />
      <input type="submit" value="SignUp" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";

const username = ref(null);
const password = ref(null);
const passwordcheck = ref(null);

const store = useCounterStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password: password.value,
    passwordcheck: passwordcheck.value,
  };
  store.signUp(payload);
};
</script>

<style scoped></style>
