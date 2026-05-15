// travel-os-frontend/src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "dashboard",
      component: () => import("@/pages/Dashboard/index.vue"),
    },
    {
      path: "/tour-designer",
      name: "tour-designer",
      component: () => import("@/pages/TourDesigner/index.vue"),
    },
    {
      path: "/crm",
      name: "crm",
      component: () => import("@/pages/CRM/index.vue"),
    },
    // Chặn mọi đường dẫn lỗi và đẩy về trang chủ
    {
      path: "/:pathMatch(.*)*",
      redirect: "/",
    },
  ],
});

export default router;
