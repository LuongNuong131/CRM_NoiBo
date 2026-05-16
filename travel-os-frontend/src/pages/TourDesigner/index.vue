<template>
  <div class="h-full flex flex-col gap-6">
    <div class="flex items-center justify-between">
      <div>
        <h1
          class="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400"
        >
          AI Tour Designer
        </h1>
        <p class="text-slate-400 mt-1">
          Sử dụng sức mạnh của Gemini để thiết kế lộ trình siêu tốc
        </p>
      </div>

      <button
        v-if="tourStore.currentTour"
        @click="tourStore.saveTourToDatabase"
        :disabled="tourStore.isSaving"
        class="flex items-center gap-2 px-6 py-2.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 text-white font-medium shadow-[0_0_20px_rgba(16,185,129,0.3)] hover:shadow-[0_0_30px_rgba(16,185,129,0.5)] transition-all disabled:opacity-50"
      >
        <div
          v-if="tourStore.isSaving"
          class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"
        ></div>
        <Save v-else class="w-4 h-4" />
        {{ tourStore.isSaving ? "Đang lưu vào MySQL..." : "Lưu Hành Trình" }}
      </button>
    </div>

    <div
      class="glass-panel bg-slate-900/60 border border-white/10 rounded-2xl p-6 relative overflow-hidden"
    >
      <div
        class="absolute -top-20 -right-20 w-40 h-40 bg-purple-500/20 blur-3xl rounded-full pointer-events-none"
      ></div>

      <div class="relative z-10 flex gap-4">
        <div class="flex-1 relative">
          <Sparkles
            class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-indigo-400"
          />
          <input
            v-model="promptInput"
            @keyup.enter="handleGenerate"
            type="text"
            placeholder="Ví dụ: Lên cho anh tour team building Vũng Tàu 2 ngày 1 đêm cho 40 người, budget 3 triệu/người..."
            class="w-full bg-black/40 border border-white/10 text-white rounded-xl py-4 pl-12 pr-4 focus:outline-none focus:border-indigo-500/50 focus:ring-1 focus:ring-indigo-500/50 transition-all placeholder:text-slate-500"
          />
        </div>
        <button
          @click="handleGenerate"
          :disabled="tourStore.isGenerating || !promptInput.trim()"
          class="px-8 rounded-xl bg-gradient-to-r from-indigo-500 to-purple-600 text-white font-medium hover:shadow-[0_0_20px_rgba(99,102,241,0.4)] transition-all disabled:opacity-50 flex items-center gap-2"
        >
          <div
            v-if="tourStore.isGenerating"
            class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"
          ></div>
          <Sparkles v-else class="w-5 h-5" />
          {{
            tourStore.isGenerating ? "AI đang tính toán..." : "Thiết Kế Ngay"
          }}
        </button>
      </div>
    </div>

    <div
      v-if="tourStore.isGenerating"
      class="flex-1 flex flex-col items-center justify-center min-h-[400px]"
    >
      <div class="relative w-24 h-24 flex items-center justify-center">
        <div
          class="absolute inset-0 border-4 border-indigo-500/20 rounded-full"
        ></div>
        <div
          class="absolute inset-0 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin"
        ></div>
        <Bot class="w-8 h-8 text-indigo-400 animate-pulse" />
      </div>
      <h3 class="text-xl font-bold text-white mt-6 animate-pulse">
        Gemini đang phân tích lộ trình...
      </h3>
      <p class="text-slate-400 mt-2">
        Đang tìm kiếm nhà hàng, khách sạn và điểm đến tối ưu nhất
      </p>
    </div>

    <div
      v-else-if="tourStore.currentTour"
      class="flex-1 grid grid-cols-3 gap-6 animate-[fadeIn_0.5s_ease-out]"
    >
      <div
        class="col-span-1 glass-panel bg-slate-900/60 border border-white/10 rounded-2xl p-6 h-fit sticky top-6"
      >
        <div
          class="w-12 h-12 rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center mb-6 shadow-lg"
        >
          <Map class="w-6 h-6 text-white" />
        </div>
        <h2 class="text-2xl font-bold text-white mb-2">
          {{ tourStore.currentTour.title }}
        </h2>

        <div class="mt-6 space-y-4">
          <div
            class="flex items-center justify-between p-4 bg-black/40 rounded-xl border border-white/5"
          >
            <span class="text-slate-400">Ước tính chi phí</span>
            <span class="text-emerald-400 font-bold">{{
              tourStore.currentTour.estimated_cost_per_person
            }}</span>
          </div>
          <div
            class="flex items-center justify-between p-4 bg-black/40 rounded-xl border border-white/5"
          >
            <span class="text-slate-400">Tổng thời gian</span>
            <span class="text-white font-medium"
              >{{ tourStore.currentTour.itinerary.length }} Ngày</span
            >
          </div>
        </div>
      </div>

      <div class="col-span-2 space-y-6 pb-10">
        <div
          v-for="day in tourStore.currentTour.itinerary"
          :key="day.day"
          class="glass-panel bg-slate-900/40 border border-white/5 rounded-2xl p-6"
        >
          <h3
            class="text-lg font-bold text-indigo-400 mb-6 flex items-center gap-2"
          >
            <div class="w-2 h-8 bg-indigo-500 rounded-full"></div>
            Ngày {{ day.day }}
          </h3>

          <div class="space-y-4 pl-4 border-l-2 border-white/10 ml-2">
            <div
              v-for="(node, idx) in day.nodes"
              :key="idx"
              class="relative pl-6"
            >
              <div
                class="absolute -left-[29px] top-1 w-4 h-4 rounded-full bg-slate-800 border-2 border-indigo-500 z-10"
              ></div>

              <div
                class="bg-black/40 hover:bg-white/5 transition-colors border border-white/5 rounded-xl p-4 flex gap-4"
              >
                <div
                  class="w-10 h-10 shrink-0 rounded-lg bg-indigo-500/20 flex items-center justify-center border border-indigo-500/30"
                >
                  <Hotel
                    v-if="node.type === 'HOTEL'"
                    class="w-5 h-5 text-indigo-400"
                  />
                  <MapPin
                    v-else-if="node.type === 'ATTRACTION'"
                    class="w-5 h-5 text-rose-400"
                  />
                  <Coffee v-else class="w-5 h-5 text-amber-400" />
                </div>
                <div>
                  <div class="flex items-center gap-3 mb-1">
                    <span class="text-sm font-bold text-slate-300">{{
                      node.time
                    }}</span>
                    <span
                      class="text-xs px-2 py-0.5 rounded-full bg-white/10 text-slate-300 border border-white/10"
                      >{{ node.type }}</span
                    >
                  </div>
                  <h4 class="text-base font-bold text-white">
                    {{ node.title }}
                  </h4>
                  <p class="text-sm text-slate-400 mt-1 leading-relaxed">
                    {{ node.description }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useTourStore } from "@/stores/tour";
import {
  Sparkles,
  Save,
  Bot,
  Map,
  MapPin,
  Hotel,
  Coffee,
} from "lucide-vue-next";

const tourStore = useTourStore();
const promptInput = ref("");

const handleGenerate = () => {
  if (!promptInput.value.trim()) return;
  tourStore.generateAITour(promptInput.value);
};
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
