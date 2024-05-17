import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/HomeView.vue";
import Accounts from "@/views/AccountsView.vue";
import Movies from "@/views/MoviesView.vue";
import UserInfo from "@/components/UserInfo.vue";
import MovieDetail from "@/components/MovieDetail.vue";
import SignUpView from "@/views/SignUpView.vue";
import LoginView from "@/views/LoginView.vue";

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
      path: "/movies",
      name: "movies",
      component: Movies,
    },
    {
      path: "/movies/detail",
      name: "movie_detail",
      component: MovieDetail,
    },
  ],
});

export default router;
