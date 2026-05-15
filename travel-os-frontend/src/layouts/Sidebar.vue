<template>
  <aside
    class="fixed left-0 top-0 h-screen glass-panel border-r border-os-border/50 flex flex-col transition-all duration-300 ease-in-out"
    :class="appStore.isSidebarCollapsed ? 'w-[88px]' : 'w-[260px]'"
  >
    <div
      class="p-6 flex items-center h-20 shrink-0"
      :class="appStore.isSidebarCollapsed ? 'justify-center' : 'space-x-3'"
    >
      <div
        class="w-8 h-8 bg-os-accent rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(99,102,241,0.5)] shrink-0"
      >
        <span class="text-white font-bold">T</span>
      </div>
      <span
        class="text-xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400 whitespace-nowrap transition-opacity duration-300"
        :class="
          appStore.isSidebarCollapsed ? 'opacity-0 w-0 hidden' : 'opacity-100'
        "
      >
        TravelOS
      </span>
    </div>

    <nav class="flex-1 px-4 py-4 space-y-2 overflow-hidden">
      <router-link
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        class="flex items-center px-4 py-3 rounded-xl transition-all duration-200 group relative"
        :class="[
          $route.path === item.path
            ? 'bg-os-accent/10 text-os-accent'
            : 'text-os-muted hover:bg-white/5 hover:text-white',
          appStore.isSidebarCollapsed ? 'justify-center' : 'space-x-3',
        ]"
        :title="appStore.isSidebarCollapsed ? item.label : ''"
      >
        <component :is="item.icon" class="w-5 h-5 shrink-0" />
        <span
          class="font-medium whitespace-nowrap transition-opacity duration-300"
          :class="
            appStore.isSidebarCollapsed ? 'opacity-0 w-0 hidden' : 'opacity-100'
          "
        >
          {{ item.label }}
        </span>
        <div
          v-if="$route.path === item.path"
          class="absolute left-0 w-1 h-6 bg-os-accent rounded-r-full"
        ></div>
      </router-link>
    </nav>

    <div class="p-4 border-t border-os-border/50 flex flex-col gap-4">
      <div
        class="flex items-center rounded-xl transition-all overflow-hidden"
        :class="
          appStore.isSidebarCollapsed
            ? 'justify-center p-0'
            : 'p-3 bg-white/5 space-x-3'
        "
      >
        <div
          class="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-500 to-purple-500 border border-white/20 shrink-0"
        ></div>
        <div
          class="overflow-hidden text-sm transition-opacity duration-300"
          :class="
            appStore.isSidebarCollapsed ? 'opacity-0 w-0 hidden' : 'opacity-100'
          "
        >
          <p class="font-semibold text-white truncate">LuNu Dev</p>
          <p class="text-xs text-os-muted truncate">Enterprise Admin</p>
        </div>
      </div>

      <button
        @click="appStore.toggleSidebar()"
        class="flex items-center justify-center p-2 rounded-xl text-os-muted hover:text-white hover:bg-white/5 transition-colors border border-transparent hover:border-os-border"
      >
        <PanelLeftClose v-if="!appStore.isSidebarCollapsed" class="w-5 h-5" />
        <PanelLeftOpen v-else class="w-5 h-5" />
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
  { label: "Dashboard", path: "/", icon: LayoutDashboard },
  { label: "Tour Designer", path: "/tour-designer", icon: Map },
  { label: "Customers CRM", path: "/crm", icon: Users },
  { label: "Bookings", path: "/bookings", icon: Briefcase },
  { label: "Finance", path: "/finance", icon: CreditCard },
  { label: "Settings", path: "/settings", icon: Settings },
];
</script>
