import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/HomeView.vue";
import Accounts from "@/views/AccountsView.vue";
import Movies from "@/views/MoviesView.vue";
import UserInfo from "@/components/UserInfo.vue";
import MovieDetail from "@/components/MovieDetail.vue";
import MovieDetailPage from "@/components/MovieDetailPage.vue"
import SignUpView from "@/views/SignUpView.vue";
import LoginView from "@/views/LoginView.vue";
import ReviewView from "@/views/ReviewView.vue"
import MovieRecommendView from '@/views/MovieRecommendView.vue'
import { useCounterStore } from '@/stores/counter'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
    },
    {
      path: "/accounts",
      name: "accounts",
      component: Accounts,
    },
    {
      path: "/accounts/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/accounts/login",
      name: "LoginView",
      component: LoginView,
    },
    {
      path: "/accounts/userinfo",
      name: "userinfo",
      component: UserInfo,
    },
    {
      path: "/movies/recommend/:id",
      name: "movies_recommend",
      component: MovieRecommendView,
    },
    {
      path: "/movies",
      name: "movies",
      component: Movies,
    },
    { 
      path: "/movies/detail",
      name: "movie_detail",
      component: MovieDetail,
    },
    {
      path: "/movies/detail/:id",
      name: "movie_detail_page",
      component: MovieDetailPage,
    },
    { 
      path: "/movies/detail/:id/review",
      name: "ReviewView",
      component: ReviewView,
    }
  ],
});

router.beforeEach((to, from) => {
  const store = useCounterStore()
  // if (to.name === 'userinfo' && !store.isLogin) {
  //   window.alert('로그인이 필요합니다.')
  //   return { name : 'LoginView' }
  // }
  if ((to.name === 'SignUpView' || to.name==="LoginView") && (store.isLogin)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'home'}
  }
 {}})

export default router;
