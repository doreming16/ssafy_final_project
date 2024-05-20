import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useCounterStore = defineStore(
  "counter",
  () => {
    const API_URL = "http://127.0.0.1:8000";

    // token 저장
    const token = ref(null);

    const signUp = function (payload) {
      const username = payload.username;
      const password1 = payload.password1;
      const password2 = payload.password2;

      // const { username, password, passwordcheck } = payload


      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2
        },
      })
        .then((res) => {
          console.log("회원가입 완료");
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const logIn = function (payload) {
      const username = payload.username;
      const password = payload.password;

      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log("로그인 완료");
          console.log(res.data);
          token.value = res.data.key;
        })
        .catch((err) => {
          console.log(err);
        });
    };
    return { API_URL, signUp, logIn, token };
  },
  { persist: true }
);
