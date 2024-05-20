// import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
// import '@/src/assets/fonts.css';

const app = createApp(App);
const pinia = createPinia();

// pinia.user(piniaPluginPersistedstate);
// app.use(createPinia())
app.use(pinia);
app.use(router);

app.mount("#app");
