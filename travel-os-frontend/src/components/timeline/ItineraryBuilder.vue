<template>
  <div
    class="h-full flex flex-col glass-panel rounded-3xl overflow-hidden border border-white/5 bg-slate-900/40 shadow-2xl relative"
  >
    <div
      class="p-6 border-b border-white/5 bg-gradient-to-b from-white/[0.05] to-transparent relative z-10"
    >
      <div
        class="absolute top-0 inset-x-0 h-1 bg-gradient-to-r from-indigo-500 to-purple-500 opacity-50"
      ></div>
      <h2
        class="text-xl font-black text-white mb-2 truncate"
        :title="tourStore.tourTitle"
      >
        {{ tourStore.tourTitle }}
      </h2>
      <div class="flex items-center gap-3">
        <span
          class="text-xs font-bold bg-indigo-500/20 text-indigo-300 px-2.5 py-1 rounded-md border border-indigo-500/20"
        >
          {{ tourStore.itinerary.length ? tourStore.itinerary.length : 0 }} Ngày
        </span>
        <span class="w-1.5 h-1.5 bg-slate-600 rounded-full"></span>
        <span
          class="text-xs font-bold text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-md border border-emerald-500/20"
        >
          Dự kiến: {{ tourStore.estimatedCost }}
        </span>
      </div>
    </div>

    <div class="flex-1 overflow-y-auto p-6 space-y-8 relative custom-scrollbar">
      <div
        v-if="tourStore.isGenerating"
        class="absolute inset-0 z-20 bg-slate-900/80 backdrop-blur-md flex flex-col items-center justify-center rounded-b-3xl"
      >
        <div class="relative w-20 h-20 mb-6 flex items-center justify-center">
          <div
            class="absolute inset-0 border-4 border-indigo-500/30 rounded-full"
          ></div>
          <div
            class="absolute inset-0 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin"
          ></div>
          <Sparkles class="w-8 h-8 text-indigo-400 animate-pulse" />
        </div>
        <h3 class="text-lg font-bold text-white mb-2">
          Trí tuệ nhân tạo đang làm việc...
        </h3>
        <p class="text-sm text-indigo-300 animate-pulse font-medium">
          Đang tính toán tọa độ, tối ưu hóa cung đường và ngân sách.
        </p>
      </div>

      <div v-for="day in tourStore.itinerary" :key="day.day" class="relative">
        <div
          class="sticky top-0 bg-slate-900/80 backdrop-blur px-2 py-3 z-10 rounded-lg mb-4 flex items-center gap-3 shadow-md border border-white/5"
        >
          <div
            class="w-8 h-8 rounded-lg bg-indigo-500 flex items-center justify-center shadow-[0_0_15px_rgba(99,102,241,0.5)]"
          >
            <Calendar class="w-4 h-4 text-white" />
          </div>
          <h3 class="text-white font-black uppercase tracking-widest text-sm">
            Ngày {{ day.day }}
          </h3>
        </div>

        <div
          class="space-y-6 relative before:absolute before:inset-0 before:ml-[19px] before:-translate-x-px before:h-full before:w-[2px] before:bg-gradient-to-b before:from-indigo-500/50 before:via-white/10 before:to-transparent"
        >
          <div
            v-for="(node, nIndex) in day.nodes"
            :key="nIndex"
            class="relative flex items-start gap-4 group"
          >
            <div
              class="relative mt-1 shrink-0 z-10 transition-transform duration-300 group-hover:scale-110"
            >
              <div
                class="absolute inset-0 bg-indigo-500 blur-sm opacity-50 rounded-full group-hover:opacity-100"
              ></div>
              <div
                class="w-10 h-10 rounded-full border-[3px] border-slate-900 bg-indigo-600 flex items-center justify-center text-white relative shadow-xl"
              >
                <component :is="getIcon(node.type)" class="w-4 h-4" />
              </div>
            </div>

            <div
              class="flex-1 bg-white/5 border border-white/5 p-4 rounded-2xl hover:bg-white/10 hover:border-indigo-500/30 transition-all duration-300 cursor-pointer shadow-lg"
            >
              <div class="flex justify-between items-start mb-2">
                <h4
                  class="font-bold text-white text-sm group-hover:text-indigo-300 transition-colors"
                >
                  {{ node.title }}
                </h4>
                <span
                  class="text-[10px] font-black text-indigo-200 bg-indigo-500/20 px-2 py-1 rounded-lg shrink-0 ml-3"
                  >{{ node.time }}</span
                >
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">
                {{ node.description }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <div
        v-if="!tourStore.itinerary.length && !tourStore.isGenerating"
        class="h-full flex flex-col items-center justify-center text-center opacity-50 px-6"
      >
        <Map class="w-16 h-16 text-slate-400 mb-4" />
        <h3 class="text-white font-bold text-lg">Chưa có lịch trình</h3>
        <p class="text-sm text-slate-400 mt-2">
          Sử dụng thanh công cụ AI bên dưới Bản đồ để khởi tạo một hành trình
          mới.
        </p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  Calendar,
  MapPin,
  Coffee,
  Bed,
  Utensils,
  Sparkles,
  Map,
} from "lucide-vue-next";
import { useTourStore } from "@/stores/tour";

const tourStore = useTourStore();

const getIcon = (type: string) => {
  const t = type.toLowerCase();
  if (t.includes("coffee")) return Coffee;
  if (t.includes("hotel") || t.includes("stay") || t.includes("khách sạn"))
    return Bed;
  if (
    t.includes("restaurant") ||
    t.includes("food") ||
    t.includes("meal") ||
    t.includes("nhà hàng") ||
    t.includes("bữa")
  )
    return Utensils;
  return MapPin;
};
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
