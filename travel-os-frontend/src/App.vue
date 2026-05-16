<template>
  <div class="min-h-screen bg-os-bg relative overflow-hidden flex">
    <div
      class="fixed inset-0 pointer-events-none z-0 bg-[radial-gradient(ellipse_80%_50%_at_20%_0%,rgba(99,102,241,0.08)_0%,transparent_60%),radial-gradient(ellipse_60%_40%_at_80%_100%,rgba(139,92,246,0.08)_0%,transparent_60%)]"
    ></div>

    <Sidebar class="z-50" />

    <div
      class="flex-1 flex flex-col relative z-10 transition-all duration-500 ease-in-out"
      :class="appStore.isSidebarCollapsed ? 'ml-[88px]' : 'ml-[280px]'"
    >
      <Topbar />

      <main
        class="flex-1 p-8 overflow-y-auto h-[calc(100vh-64px)] custom-scrollbar"
      >
        <router-view v-slot="{ Component }">
          <transition
            enter-active-class="transition duration-400 ease-out"
            enter-from-class="transform translate-y-4 opacity-0 scale-[0.98]"
            enter-to-class="transform translate-y-0 opacity-100 scale-100"
            mode="out-in"
          >
            <Suspense v-if="Component">
              <component :is="Component" />
              <template #fallback>
                <div class="flex items-center justify-center h-full w-full">
                  <div
                    class="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin shadow-[0_0_15px_rgba(99,102,241,0.5)]"
                  ></div>
                </div>
              </template>
            </Suspense>
          </transition>
        </router-view>
      </main>
    </div>

    <AICopilot />
  </div>
</template>

<script setup lang="ts">
import Sidebar from "@/layouts/Sidebar.vue";
import Topbar from "@/layouts/Topbar.vue";
import AICopilot from "@/components/common/AICopilot.vue";
import { useAppStore } from "@/stores/app";

const appStore = useAppStore();
</script>

<style>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
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
