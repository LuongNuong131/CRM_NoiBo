// travel-os-frontend/src/router/index.ts
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
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
    {
      path: "/bookings",
      name: "bookings",
      component: () => import("@/pages/Bookings/index.vue"),
    },
    {
      path: "/finance",
      name: "finance",
      component: () => import("@/pages/Finance/index.vue"),
    },
    {
      path: "/settings",
      name: "settings",
      // Tạm thời trỏ về Dashboard, sau này mình làm trang Settings riêng nhé
      component: () => import("@/pages/Dashboard/index.vue"),
    },
  ],
});

export default router;
