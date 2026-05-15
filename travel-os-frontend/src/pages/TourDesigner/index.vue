<template>
  <div class="h-full flex gap-6">
    <div class="w-1/3 h-full min-w-[350px]">
      <ItineraryBuilder />
    </div>

    <div class="flex-1 h-full relative">
      <MapboxEngine />

      <div
        class="absolute bottom-6 left-1/2 -translate-x-1/2 w-3/4 max-w-2xl glass-panel p-2 rounded-full flex items-center gap-3 shadow-[0_0_30px_rgba(99,102,241,0.15)]"
      >
        <div
          class="w-10 h-10 rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 flex items-center justify-center shrink-0 ml-1 shadow-lg"
        >
          <Sparkles class="w-5 h-5 text-white" />
        </div>

        <input
          v-model="aiPrompt"
          @keyup.enter="handleGenerate"
          :disabled="tourStore.isGenerating"
          type="text"
          placeholder="Ask AI: Create a 3D2N trip to Da Lat under 4M..."
          class="flex-1 bg-transparent border-none text-white focus:outline-none text-sm px-2 disabled:opacity-50"
        />

        <button
          @click="handleGenerate"
          :disabled="tourStore.isGenerating || !aiPrompt.trim()"
          class="bg-indigo-500 hover:bg-indigo-600 disabled:bg-white/10 disabled:text-os-muted text-white px-6 py-2 rounded-full text-sm font-medium transition mr-1 flex items-center gap-2"
        >
          <span
            v-if="tourStore.isGenerating"
            class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"
          ></span>
          {{ tourStore.isGenerating ? "Thinking..." : "Generate" }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Sparkles } from "lucide-vue-next";
import MapboxEngine from "@/components/map/MapEngine.vue";
import ItineraryBuilder from "@/components/timeline/ItineraryBuilder.vue";
import { useTourStore } from "@/stores/tour";

const tourStore = useTourStore();
const aiPrompt = ref("");

const handleGenerate = () => {
  if (aiPrompt.value.trim() && !tourStore.isGenerating) {
    tourStore.generateAITour(aiPrompt.value);
  }
};
</script>
