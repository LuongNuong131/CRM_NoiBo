<template>
  <aside
    class="fixed left-0 top-0 h-screen w-[260px] glass-panel border-r border-os-border/50 flex flex-col z-50"
  >
    <div class="p-8 flex items-center space-x-3">
      <div
        class="w-8 h-8 bg-os-accent rounded-lg flex items-center justify-center shadow-[0_0_20px_rgba(99,102,241,0.5)]"
      >
        <span class="text-white font-bold">T</span>
      </div>
      <span
        class="text-xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white to-slate-400"
      >
        TravelOS
      </span>
    </div>

    <nav class="flex-1 px-4 space-y-2">
      <router-link
        v-for="item in menuItems"
        :key="item.path"
        :to="item.path"
        class="flex items-center space-x-3 px-4 py-3 rounded-xl transition-all duration-200 group relative"
        :class="[
          $route.path === item.path
            ? 'bg-os-accent/10 text-os-accent'
            : 'text-os-muted hover:bg-white/5 hover:text-white',
        ]"
      >
        <component :is="item.icon" class="w-5 h-5" />
        <span class="font-medium">{{ item.label }}</span>
        <div
          v-if="$route.path === item.path"
          class="absolute left-0 w-1 h-6 bg-os-accent rounded-r-full"
        ></div>
      </router-link>
    </nav>

    <div class="p-6 border-t border-os-border/50">
      <div class="flex items-center space-x-3 p-3 rounded-xl bg-white/5">
        <div
          class="w-10 h-10 rounded-full bg-gradient-to-br from-indigo-500 to-purple-500 border border-white/20"
        ></div>
        <div class="overflow-hidden text-sm">
          <p class="font-semibold truncate">LuNu Dev</p>
          <p class="text-xs text-os-muted truncate">Enterprise Admin</p>
        </div>
      </div>
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
} from "lucide-vue-next";

const menuItems = [
  { label: "Dashboard", path: "/", icon: LayoutDashboard },
  { label: "Tour Designer", path: "/tour-designer", icon: Map },
  { label: "Customers CRM", path: "/crm", icon: Users },
  { label: "Bookings", path: "/bookings", icon: Briefcase },
  { label: "Finance", path: "/finance", icon: CreditCard },
  { label: "Settings", path: "/settings", icon: Settings },
];
</script>
