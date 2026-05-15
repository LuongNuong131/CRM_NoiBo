<template>
  <div
    class="h-full flex flex-col glass-panel rounded-2xl overflow-hidden border border-os-border/50"
  >
    <div class="p-6 border-b border-os-border/50 bg-os-panel/30">
      <h2 class="text-xl font-bold text-white mb-1">
        {{ tourStore.tourTitle }}
      </h2>
      <p class="text-sm text-os-muted flex items-center gap-2">
        <span v-if="tourStore.itinerary.length"
          >{{ tourStore.itinerary.length }} Days</span
        >
        <span v-else>0 Days</span>
        <span class="w-1 h-1 bg-os-muted rounded-full"></span>
        <span>Est. Cost: {{ tourStore.estimatedCost }}</span>
      </p>
    </div>

    <div class="flex-1 overflow-y-auto p-6 space-y-6 relative">
      <div
        v-if="tourStore.isGenerating"
        class="absolute inset-0 z-20 bg-os-bg/80 backdrop-blur-sm flex flex-col items-center justify-center"
      >
        <div
          class="w-10 h-10 border-4 border-indigo-500 border-t-transparent rounded-full animate-spin mb-4"
        ></div>
        <p class="text-indigo-400 font-medium animate-pulse">
          AI is crafting your perfect trip...
        </p>
      </div>

      <div
        v-for="(day, dIndex) in tourStore.itinerary"
        :key="day.day"
        class="relative"
      >
        <h3 class="text-indigo-400 font-semibold mb-4 flex items-center gap-2">
          <Calendar class="w-4 h-4" /> Day {{ day.day }}
        </h3>

        <div
          class="space-y-4 relative before:absolute before:inset-0 before:ml-[15px] before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-os-border before:to-transparent"
        >
          <div
            v-for="(node, nIndex) in day.nodes"
            :key="nIndex"
            class="relative flex items-center justify-between md:justify-normal md:odd:flex-row-reverse group is-active"
          >
            <div
              class="flex items-center justify-center w-8 h-8 rounded-full border-4 border-os-bg bg-os-accent text-white shadow shrink-0 md:order-1 md:group-odd:-translate-x-1/2 md:group-even:translate-x-1/2 z-10 transition-transform group-hover:scale-110"
            >
              <component :is="getIcon(node.type)" class="w-3 h-3" />
            </div>

            <div
              class="w-[calc(100%-4rem)] md:w-[calc(50%-2.5rem)] glass-panel p-4 rounded-xl cursor-grab hover:border-os-accent/50 transition-colors"
            >
              <div class="flex justify-between items-start mb-1">
                <h4 class="font-bold text-white text-sm">{{ node.title }}</h4>
                <span
                  class="text-xs text-os-muted bg-white/5 px-2 py-1 rounded whitespace-nowrap ml-2"
                  >{{ node.time }}</span
                >
              </div>
              <p class="text-xs text-os-muted">{{ node.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div
        v-if="!tourStore.itinerary.length && !tourStore.isGenerating"
        class="text-center py-10 opacity-50"
      >
        <p>Ask AI to generate a tour itinerary</p>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Calendar, MapPin, Coffee, Bed, Utensils } from "lucide-vue-next";
import { useTourStore } from "@/stores/tour";

const tourStore = useTourStore();

const getIcon = (type: string) => {
  const t = type.toLowerCase();
  if (t.includes("coffee")) return Coffee;
  if (t.includes("hotel") || t.includes("stay")) return Bed;
  if (t.includes("restaurant") || t.includes("food") || t.includes("meal"))
    return Utensils;
  return MapPin; // default cho attraction
};
</script>
