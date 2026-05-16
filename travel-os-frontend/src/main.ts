// travel-os-frontend/src/main.ts
import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";

// Import CSS (Tailwind)
import "./assets/main.css";

const app = createApp(App);

// Khởi tạo trái dứa (Pinia) - Nơi chứa dữ liệu Global của toàn app
const pinia = createPinia();

// BẮT BUỘC: Phải use(pinia) và use(router) trước khi mount app
app.use(pinia);
app.use(router);

app.mount("#app");
