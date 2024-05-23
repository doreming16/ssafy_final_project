import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from 'vue-router'


export const useCounterStore = defineStore(
  "counter",
  () => {
    const images = ref([])
    const reviews = ref([])
    const API_URL = "http://127.0.0.1:8000";

    const getImages = function () {
      axios({
        method: 'get',
        url: `${API_URL}/movies/home`
      })
    }

    const getReviews = function (Id) {
      if (token.value) {

        axios({
          method: 'get',
          url: `${API_URL}/movies/detail/${Id}/reviews/`
        })
        .then(res => {
          // console.log(res)
          // console.log(res.data)
          reviews.value = res.data
        })
        .catch(err => console.log(err))
      }
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
          // console.log(token.value)
          localStorage.setItem('authToken', token.value); // Storage에 Token 저장
          router.push({ name : 'home' })
        })
        .catch((err) => {
          console.log(err);
        });
    };
    
    const user = ref(null);

    const logOut = function () {
      localStorage.removeItem('authToken');
      token.value = null;
      user.value = null;
      console.log('로그아웃 완료');
      router.push({ name : 'home'});
    };

    const isLogin = computed(() => {
      if (token.value === null){
        return false
      } else {
        return true
      }
    });


    const get_user_profile = function () {
      const authToken = localStorage.getItem('authToken');
      // console.log(authToken)

      if (authToken) {

        axios({
          method: 'get',
          url: `${API_URL}/accounts/profile/`,
          headers: {
            Authorization: `Token ${authToken}`
          },
        }).then(res => {
          user.value = res.data;
          console.log('user_profile 가져오기 완료')
          console.log(user.value.username);
        }).catch(err => {
          console.log(err);
        });

      }
    }

    if (token.value) {
      get_user_profile();
    }
    
    return { API_URL, signUp, logIn, token, isLogin, logOut, get_user_profile, user, getReviews};
  },
  { persist: true }
);
