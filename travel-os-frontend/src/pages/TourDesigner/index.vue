<template>
  <div class="h-full flex gap-6">
    <div class="w-1/3 h-full min-w-[350px]">
      <ItineraryBuilder />
    </div>

    <div class="flex-1 h-full relative">
      <MapboxEngine />

      <div
        class="absolute bottom-6 left-1/2 -translate-x-1/2 w-3/4 max-w-2xl glass-panel p-2 rounded-full flex items-center gap-3"
      >
        <div
          class="w-10 h-10 rounded-full bg-gradient-to-r from-indigo-500 to-purple-500 flex items-center justify-center shrink-0 ml-1"
        >
          <Sparkles class="w-5 h-5 text-white" />
        </div>
        <input
          type="text"
          placeholder="Ask AI: Generate a 3D2N trip to Da Lat under 4M..."
          class="flex-1 bg-transparent border-none text-white focus:outline-none text-sm px-2"
        />
        <button
          class="bg-white/10 hover:bg-white/20 text-white px-6 py-2 rounded-full text-sm font-medium transition mr-1"
        >
          Generate
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Sparkles } from "lucide-vue-next";
import MapboxEngine from "@/components/map/MapboxEngine.vue";
import ItineraryBuilder from "@/components/timeline/ItineraryBuilder.vue";
</script>
