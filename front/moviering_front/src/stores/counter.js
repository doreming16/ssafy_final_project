import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore(
  "counter",
  () => {
    const images = ref([])
    const API_URL = "http://127.0.0.1:8000";

    const getImages = function () {
      axios({
        method: 'get',
        url: `${API_URL}/movies/home`
      })
    }

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
          const password = password1
          logIn({ username, password })
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const router = useRouter()  
  
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
          router.push({ name : 'home' })
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const isLogin = computed(() => {
      if (token.value === null){
        return false
      } else {
        return true
      }
    })
    return { API_URL, signUp, logIn, token, isLogin };
  },
  { persist: true }
);
