<template>
  <aside
    class="fixed left-0 top-0 h-screen glass-panel border-r border-os-border/40 flex flex-col transition-all duration-500 ease-out z-[100]"
    :class="appStore.isSidebarCollapsed ? 'w-[88px]' : 'w-[280px]'"
    style="background: rgba(15, 23, 42, 0.4); backdrop-filter: blur(20px)"
  >
    <div
      class="p-6 flex items-center h-24 shrink-0 transition-all duration-300"
      :class="appStore.isSidebarCollapsed ? 'justify-center' : 'space-x-4'"
    >
      <div
        class="relative w-10 h-10 rounded-xl flex items-center justify-center shrink-0 group cursor-pointer"
      >
        <div
          class="absolute inset-0 bg-indigo-500 blur-md opacity-50 group-hover:opacity-100 transition-opacity duration-500"
        ></div>
        <div
          class="relative w-full h-full bg-gradient-to-br from-indigo-500 to-purple-600 rounded-xl flex items-center justify-center border border-white/20 shadow-xl"
        >
          <span class="text-white font-black text-xl tracking-tighter">T</span>
        </div>
      </div>
      <div
        class="flex flex-col transition-all duration-300 overflow-hidden"
        :class="
          appStore.isSidebarCollapsed ? 'opacity-0 w-0' : 'opacity-100 w-auto'
        "
      >
        <span
          class="text-2xl font-black tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-indigo-200 to-slate-400 whitespace-nowrap"
        >
          TravelOS
        </span>
        <span
          class="text-[10px] text-indigo-400 font-bold uppercase tracking-[0.2em] -mt-1"
          >Enterprise</span
        >
      </div>
    </div>

    <nav
      class="flex-1 px-4 py-6 space-y-2 overflow-y-auto overflow-x-hidden custom-scrollbar"
    >
      <p
        v-if="!appStore.isSidebarCollapsed"
        class="px-4 text-[11px] font-bold text-os-muted uppercase tracking-wider mb-4"
      >
        Menu Chính
      </p>

      <router-link
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        class="flex items-center px-4 py-3.5 rounded-2xl transition-all duration-300 group relative overflow-hidden"
        :class="[
          $route.path === item.path
            ? 'bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 shadow-[inset_0_0_20px_rgba(99,102,241,0.05)]'
            : 'text-slate-400 hover:bg-white/5 hover:text-white border border-transparent',
          appStore.isSidebarCollapsed ? 'justify-center' : 'space-x-4',
        ]"
        :title="appStore.isSidebarCollapsed ? item.label : ''"
      >
        <div
          class="absolute inset-0 bg-gradient-to-r from-white/0 via-white/[0.02] to-white/0 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-1000"
        ></div>

        <component
          :is="item.icon"
          class="w-[22px] h-[22px] shrink-0 transition-transform duration-300 group-hover:scale-110"
          :class="{
            'text-indigo-400 drop-shadow-[0_0_8px_rgba(129,140,248,0.5)]':
              $route.path === item.path,
          }"
        />

        <span
          class="font-semibold whitespace-nowrap transition-all duration-300"
          :class="
            appStore.isSidebarCollapsed
              ? 'opacity-0 w-0 translate-x-4'
              : 'opacity-100 translate-x-0'
          "
        >
          {{ item.label }}
        </span>

        <div
          v-if="$route.path === item.path"
          class="absolute left-0 top-1/4 bottom-1/4 w-1.5 bg-gradient-to-b from-indigo-400 to-purple-500 rounded-r-full shadow-[0_0_10px_rgba(99,102,241,0.8)]"
        ></div>
      </router-link>
    </nav>

    <div class="p-4 border-t border-os-border/40 bg-black/10">
      <div
        class="flex items-center rounded-2xl transition-all duration-300 overflow-hidden relative group cursor-pointer"
        :class="
          appStore.isSidebarCollapsed
            ? 'justify-center p-2 hover:bg-white/5'
            : 'p-3 bg-white/5 hover:bg-white/10 border border-white/5 space-x-3'
        "
      >
        <div class="relative w-10 h-10 shrink-0">
          <div
            class="absolute inset-0 bg-emerald-500 rounded-full blur-[2px] opacity-40 group-hover:opacity-80 transition-opacity"
          ></div>
          <img
            src="https://i.pravatar.cc/150?u=a042581f4e29026704d"
            alt="LuNu"
            class="relative w-10 h-10 rounded-full border-2 border-slate-800 object-cover"
          />
          <div
            class="absolute bottom-0 right-0 w-3 h-3 bg-emerald-400 border-2 border-slate-900 rounded-full"
          ></div>
        </div>

        <div
          class="flex-1 overflow-hidden transition-all duration-300"
          :class="appStore.isSidebarCollapsed ? 'opacity-0 w-0' : 'opacity-100'"
        >
          <p class="font-bold text-white text-sm truncate">LuNu Manager</p>
          <p class="text-[11px] text-emerald-400 font-medium truncate">
            Giám đốc điều hành
          </p>
        </div>
      </div>

      <button
        @click="appStore.toggleSidebar()"
        class="mt-4 w-full flex items-center justify-center p-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 hover:border-white/10 border border-transparent transition-all duration-300 group"
      >
        <PanelLeftClose
          v-if="!appStore.isSidebarCollapsed"
          class="w-5 h-5 group-hover:-translate-x-1 transition-transform"
        />
        <PanelLeftOpen
          v-else
          class="w-5 h-5 group-hover:translate-x-1 transition-transform"
        />
      </button>
    </div>
  </aside>
</template>

<script setup lang="ts">
import {
  LayoutDashboard,
  Map,
  Users,
  Settings,
  Briefcase,
  CreditCard,
  PanelLeftClose,
  PanelLeftOpen,
} from "lucide-vue-next";
import { useAppStore } from "@/stores/app";

const appStore = useAppStore();

const menuItems = [
  { label: "Tổng Quan", path: "/", icon: LayoutDashboard },
  { label: "Thiết Kế Tour AI", path: "/tour-designer", icon: Map },
  { label: "Quản Lý Khách (CRM)", path: "/crm", icon: Users },
  { label: "Hợp Đồng & Đặt Chỗ", path: "/bookings", icon: Briefcase },
  { label: "Tài Chính & Kế Toán", path: "/finance", icon: CreditCard },
  { label: "Cài Đặt Hệ Thống", path: "/settings", icon: Settings },
];
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}
.custom-scrollbar:hover::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
}
</style>
