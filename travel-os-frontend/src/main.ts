// travel-os-frontend/src/main.ts
import { createApp } from "vue";
import { createPinia } from "pinia";
import { MotionPlugin } from "@vueuse/motion";
import router from "./router"; // Bắt buộc phải có dòng này
import App from "./App.vue";
import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router); // Bắt buộc phải có dòng này
app.use(MotionPlugin);

app.mount("#root");
