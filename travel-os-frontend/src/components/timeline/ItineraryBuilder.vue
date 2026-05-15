<template>
  <div
    class="h-full flex flex-col glass-panel rounded-2xl overflow-hidden border border-os-border/50"
  >
    <div class="p-6 border-b border-os-border/50 bg-os-panel/30">
      <h2 class="text-xl font-bold text-white mb-1">Trip Itinerary</h2>
      <p class="text-sm text-os-muted flex items-center gap-2">
        <span>3 Days 2 Nights</span>
        <span class="w-1 h-1 bg-os-muted rounded-full"></span>
        <span>HCM -> Da Lat</span>
      </p>
    </div>

    <div class="flex-1 overflow-y-auto p-6 space-y-6">
      <div v-for="(day, dIndex) in itinerary" :key="day.day" class="relative">
        <h3 class="text-indigo-400 font-semibold mb-4 flex items-center gap-2">
          <Calendar class="w-4 h-4" /> Day {{ day.day }}
        </h3>

        <div
          class="space-y-4 relative before:absolute before:inset-0 before:ml-[15px] before:-translate-x-px md:before:mx-auto md:before:translate-x-0 before:h-full before:w-0.5 before:bg-gradient-to-b before:from-transparent before:via-os-border before:to-transparent"
        >
          <div
            v-for="(node, nIndex) in day.nodes"
            :key="node.id"
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
                  class="text-xs text-os-muted bg-white/5 px-2 py-1 rounded"
                  >{{ node.time }}</span
                >
              </div>
              <p class="text-xs text-os-muted">{{ node.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <button
        class="w-full py-3 rounded-xl border border-dashed border-os-border hover:border-os-accent/50 hover:bg-os-accent/5 text-os-muted hover:text-white transition flex items-center justify-center gap-2 text-sm font-medium"
      >
        <Plus class="w-4 h-4" /> Add Destination
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Calendar, MapPin, Coffee, Bed, Plus, Utensils } from "lucide-vue-next";

const getIcon = (type: string) => {
  switch (type) {
    case "attraction":
      return MapPin;
    case "coffee":
      return Coffee;
    case "hotel":
      return Bed;
    case "restaurant":
      return Utensils;
    default:
      return MapPin;
  }
};

// Data giả lập cho timeline
const itinerary = ref([
  {
    day: 1,
    nodes: [
      {
        id: "1",
        type: "attraction",
        title: "Tập trung tại Quận 1",
        time: "06:00 AM",
        description: "Điểm khởi hành chính",
      },
      {
        id: "2",
        type: "coffee",
        title: "Trạm dừng chân",
        time: "08:30 AM",
        description: "Ăn sáng & Nghỉ ngơi",
      },
      {
        id: "3",
        type: "attraction",
        title: "Thác Prenn",
        time: "14:00 PM",
        description: "Tham quan thác",
      },
      {
        id: "4",
        type: "hotel",
        title: "Colline Hotel",
        time: "16:00 PM",
        description: "Check-in khách sạn",
      },
    ],
  },
  {
    day: 2,
    nodes: [
      {
        id: "5",
        type: "attraction",
        title: "Lang Biang",
        time: "08:00 AM",
        description: "Leo núi, chụp ảnh",
      },
      {
        id: "6",
        type: "restaurant",
        title: "Nhà hàng Leguda",
        time: "12:00 PM",
        description: "Buffet rau Đà Lạt",
      },
    ],
  },
]);
</script>
