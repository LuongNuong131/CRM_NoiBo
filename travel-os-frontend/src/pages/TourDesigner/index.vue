<template>
  <div class="h-full flex gap-6">
    <div class="w-[400px] h-full shrink-0 flex flex-col gap-4">
      <div
        class="glass-panel p-1.5 rounded-2xl flex bg-slate-900/60 border border-white/5 relative z-20 shadow-lg"
      >
        <button
          @click="designMode = 'ai'"
          class="flex-1 py-2 rounded-xl text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2"
          :class="
            designMode === 'ai'
              ? 'bg-indigo-500 text-white shadow-lg'
              : 'text-slate-400 hover:text-white'
          "
        >
          <Sparkles class="w-4 h-4" /> Trí Tuệ Nhân Tạo
        </button>
        <button
          @click="designMode = 'manual'"
          class="flex-1 py-2 rounded-xl text-sm font-bold transition-all duration-300 flex items-center justify-center gap-2"
          :class="
            designMode === 'manual'
              ? 'bg-emerald-500 text-white shadow-lg'
              : 'text-slate-400 hover:text-white'
          "
        >
          <MapPin class="w-4 h-4" /> Thủ Công
        </button>
      </div>

      <ItineraryBuilder />
    </div>

    <div
      class="flex-1 h-full relative flex flex-col rounded-3xl overflow-hidden shadow-2xl border border-white/5 bg-slate-900/40"
    >
      <div class="flex-1 relative z-0">
        <MapEngine />
      </div>

      <transition name="fade-up">
        <div
          v-if="designMode === 'ai'"
          class="absolute bottom-8 left-1/2 -translate-x-1/2 w-[80%] max-w-3xl z-10"
        >
          <div
            class="absolute -inset-2 bg-gradient-to-r from-indigo-500 to-purple-600 blur-xl opacity-20 rounded-full"
          ></div>
          <div
            class="relative glass-panel bg-slate-900/80 backdrop-blur-xl p-2.5 rounded-full flex items-center gap-3 shadow-2xl border border-white/10"
          >
            <div
              class="w-12 h-12 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shrink-0 ml-1"
            >
              <Sparkles class="w-6 h-6 text-white" />
            </div>
            <input
              v-model="aiPrompt"
              @keyup.enter="handleGenerate"
              :disabled="tourStore.isGenerating"
              type="text"
              placeholder="Hỏi AI: Lên lịch trình đi Phú Quốc 3N2Đ..."
              class="flex-1 bg-transparent border-none text-white text-sm font-medium focus:outline-none px-3 disabled:opacity-50"
            />
            <button
              @click="handleGenerate"
              :disabled="tourStore.isGenerating || !aiPrompt.trim()"
              class="bg-white text-slate-900 hover:bg-slate-200 px-8 py-3.5 rounded-full text-sm font-black transition-all mr-1 flex items-center gap-2"
            >
              {{
                tourStore.isGenerating ? "ĐANG TÍNH TOÁN..." : "TẠO LỊCH TRÌNH"
              }}
            </button>
          </div>
        </div>
      </transition>

      <transition name="fade-down">
        <div
          v-if="designMode === 'manual'"
          class="absolute top-8 left-8 w-[380px] z-10 flex flex-col gap-3"
        >
          <div
            class="glass-panel bg-slate-900/80 backdrop-blur-xl p-3 rounded-2xl shadow-2xl border border-white/10 flex items-center gap-3"
          >
            <Search class="w-5 h-5 text-emerald-400" />
            <input
              v-model="manualQuery"
              @input="handleManualSearch"
              type="text"
              placeholder="Tìm kiếm địa điểm trên toàn thế giới..."
              class="flex-1 bg-transparent border-none text-white text-sm focus:outline-none"
            />
            <div
              v-if="tourStore.isSearching"
              class="w-4 h-4 border-2 border-emerald-500 border-t-transparent rounded-full animate-spin"
            ></div>
          </div>

          <div
            v-if="tourStore.searchResults.length > 0"
            class="glass-panel bg-slate-900/90 backdrop-blur-xl rounded-2xl shadow-2xl border border-white/10 overflow-hidden"
          >
            <div
              v-for="place in tourStore.searchResults"
              :key="place.place_id"
              class="p-4 border-b border-white/5 hover:bg-white/5 cursor-pointer transition-colors group"
            >
              <h4
                class="text-sm font-bold text-white group-hover:text-emerald-400 truncate"
              >
                {{ place.display_name.split(",")[0] }}
              </h4>
              <p class="text-[10px] text-slate-400 truncate mt-1">
                {{ place.display_name }}
              </p>

              <div
                class="mt-3 flex gap-2 overflow-x-auto custom-scrollbar pb-1"
              >
                <button
                  v-for="(day, idx) in tourStore.itinerary"
                  :key="day.day"
                  @click="tourStore.addManualNode(idx, place)"
                  class="shrink-0 text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2 py-1 rounded hover:bg-emerald-500 hover:text-white transition-colors"
                >
                  + Ngày {{ day.day }}
                </button>
                <button
                  @click="tourStore.addNewDay()"
                  class="shrink-0 text-[10px] font-bold bg-white/10 text-slate-300 px-2 py-1 rounded hover:bg-white/20"
                >
                  + Ngày Mới
                </button>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Sparkles, MapPin, Search } from "lucide-vue-next";
import MapEngine from "@/components/map/MapEngine.vue";
import ItineraryBuilder from "@/components/timeline/ItineraryBuilder.vue";
import { useTourStore } from "@/stores/tour";

const tourStore = useTourStore();
const designMode = ref("ai"); // 'ai' hoặc 'manual'
const aiPrompt = ref("");
const manualQuery = ref("");

let searchTimeout: any = null;
const handleManualSearch = () => {
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => {
    tourStore.searchLocationManual(manualQuery.value);
  }, 500); // Debounce 500ms chống spam API
};

const handleGenerate = () => {
  if (aiPrompt.value.trim() && !tourStore.isGenerating) {
    tourStore.generateAITour(aiPrompt.value);
  }
};
</script>

<style scoped>
.fade-up-enter-active,
.fade-up-leave-active,
.fade-down-enter-active,
.fade-down-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.fade-up-enter-from,
.fade-up-leave-to {
  opacity: 0;
  transform: translate(-50%, 20px);
}
.fade-down-enter-from,
.fade-down-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}
</style>
