<template>
  <div class="h-full flex flex-col space-y-6 overflow-hidden">
    <div class="flex items-center justify-between shrink-0">
      <div class="relative">
        <div
          class="absolute -inset-1 bg-amber-500/20 blur-xl rounded-full"
        ></div>
        <h1
          class="relative text-3xl font-black text-white tracking-tight mb-2 flex items-center gap-3"
        >
          Phễu Khách Hàng AI
          <Sparkles
            class="w-6 h-6 text-amber-400 drop-shadow-[0_0_10px_rgba(251,191,36,0.8)]"
          />
        </h1>
        <p class="relative text-sm text-slate-400 font-medium">
          Quản lý khách hàng tiềm năng và báo giá với hệ thống chấm điểm AI tự
          động.
        </p>
      </div>
      <div class="flex items-center gap-4">
        <div
          class="bg-black/20 border border-white/10 rounded-xl flex items-center px-4 py-2.5 backdrop-blur-md shadow-inner focus-within:border-indigo-500/50 transition-colors"
        >
          <Search class="w-4 h-4 text-slate-400 mr-2" />
          <input
            type="text"
            placeholder="Tìm kiếm khách hàng..."
            class="bg-transparent border-none text-sm text-white focus:outline-none w-56 placeholder-slate-500"
          />
        </div>
        <button
          class="bg-gradient-to-r from-indigo-500 to-purple-600 hover:from-indigo-400 hover:to-purple-500 text-white px-6 py-2.5 rounded-xl text-sm font-bold transition-all flex items-center gap-2 shadow-[0_0_20px_rgba(99,102,241,0.4)] hover:shadow-[0_0_30px_rgba(99,102,241,0.6)] hover:-translate-y-0.5"
        >
          <Plus class="w-4 h-4" /> Thêm Khách
        </button>
      </div>
    </div>

    <div class="flex-1 flex gap-6 overflow-x-auto pb-4 custom-scrollbar">
      <div
        v-for="column in pipeline"
        :key="column.id"
        class="w-80 shrink-0 flex flex-col glass-panel border border-white/5 bg-slate-900/40 rounded-3xl overflow-hidden shadow-2xl relative group"
        @dragover.prevent
        @drop="onDrop($event, column.id)"
      >
        <div
          class="absolute top-0 inset-x-0 h-1"
          :class="column.glowClass"
        ></div>

        <div
          class="p-5 border-b border-white/5 flex items-center justify-between bg-white/[0.02] backdrop-blur-md"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-3 h-3 rounded-full shadow-[0_0_10px_currentColor]"
              :class="column.colorClass"
            ></div>
            <h3 class="font-bold text-white tracking-wide">
              {{ column.title }}
            </h3>
            <span
              class="bg-white/10 text-xs font-bold text-slate-300 px-2.5 py-1 rounded-lg border border-white/5"
              >{{ column.cards.length }}</span
            >
          </div>
          <button class="text-slate-500 hover:text-white transition-colors">
            <MoreHorizontal class="w-5 h-5" />
          </button>
        </div>

        <div class="flex-1 p-4 overflow-y-auto space-y-4 custom-scrollbar">
          <transition-group name="list">
            <div
              v-for="card in column.cards"
              :key="card.id"
              draggable="true"
              @dragstart="onDragStart($event, card, column.id)"
              class="relative bg-slate-800/50 p-5 rounded-2xl cursor-grab active:cursor-grabbing border border-white/5 hover:border-indigo-500/50 hover:bg-slate-800/80 transition-all duration-300 group/card overflow-hidden shadow-lg"
            >
              <div
                v-if="card.aiScore >= 90"
                class="absolute -right-8 -top-8 w-32 h-32 bg-amber-500/20 blur-2xl rounded-full pointer-events-none transition-opacity duration-500 opacity-50 group-hover/card:opacity-100"
              ></div>

              <div class="flex justify-between items-start mb-4 relative z-10">
                <div class="flex items-center gap-3">
                  <div
                    class="w-10 h-10 rounded-full bg-gradient-to-br border border-white/20 flex items-center justify-center text-sm font-black text-white shadow-lg"
                    :class="card.avatarGradient"
                  >
                    {{ card.initials }}
                  </div>
                  <div>
                    <h4
                      class="text-sm font-bold text-white group-hover/card:text-indigo-400 transition-colors"
                    >
                      {{ card.company }}
                    </h4>
                    <p class="text-[11px] text-slate-400 font-medium">
                      {{ card.contact }}
                    </p>
                  </div>
                </div>
              </div>

              <div class="mb-4 relative z-10">
                <p
                  class="text-xs text-slate-300/90 line-clamp-2 leading-relaxed"
                >
                  {{ card.request }}
                </p>
              </div>

              <div
                class="flex items-center justify-between pt-4 border-t border-white/5 relative z-10"
              >
                <div class="flex items-center gap-2">
                  <span
                    class="px-2.5 py-1 rounded-lg text-[10px] font-black uppercase tracking-wider flex items-center gap-1.5 shadow-inner"
                    :class="
                      card.aiScore >= 90
                        ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                        : 'bg-indigo-500/20 text-indigo-400 border border-indigo-500/30'
                    "
                  >
                    <BrainCircuit class="w-3.5 h-3.5" />
                    Tỉ Lệ {{ card.aiScore }}%
                  </span>
                </div>
                <span
                  class="text-sm font-black text-emerald-400 tracking-tight"
                  >{{ card.value }}</span
                >
              </div>
            </div>
          </transition-group>

          <div
            v-if="column.cards.length === 0"
            class="h-28 border-2 border-dashed border-white/10 rounded-2xl flex items-center justify-center text-slate-500 text-xs font-medium bg-black/10"
          >
            Kéo thả thẻ vào đây
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import {
  Plus,
  Search,
  MoreHorizontal,
  Sparkles,
  BrainCircuit,
} from "lucide-vue-next";

const pipeline = ref([
  {
    id: "lead",
    title: "Khách Hàng Mới",
    colorClass: "bg-blue-500 text-blue-500",
    glowClass:
      "bg-gradient-to-r from-blue-500 to-cyan-400 shadow-[0_0_15px_rgba(59,130,246,0.5)]",
    cards: [
      {
        id: 1,
        company: "FPT Software",
        contact: "Nguyễn Văn A",
        initials: "FS",
        avatarGradient: "from-blue-500 to-cyan-500",
        request:
          "Tour Company Trip 3N2Đ đi Đà Lạt cho 150 kỹ sư. Cần khách sạn 4 sao.",
        value: "125 Tr ₫",
        aiScore: 92,
      },
      {
        id: 2,
        company: "Vinamilk HR",
        contact: "Trần Thị B",
        initials: "VM",
        avatarGradient: "from-green-500 to-emerald-500",
        request: "Team building tại Phú Quốc. Ngân sách mở.",
        value: "250 Tr ₫",
        aiScore: 65,
      },
    ],
  },
  {
    id: "contacted",
    title: "Đã Liên Hệ",
    colorClass: "bg-amber-500 text-amber-500",
    glowClass:
      "bg-gradient-to-r from-amber-500 to-yellow-400 shadow-[0_0_15px_rgba(245,158,11,0.5)]",
    cards: [
      {
        id: 3,
        company: "Techcombank",
        contact: "Lê Văn C",
        initials: "TC",
        avatarGradient: "from-red-500 to-orange-500",
        request: "Tour VIP đi Nhật Bản ngắm hoa anh đào cho Ban Giám Đốc.",
        value: "450 Tr ₫",
        aiScore: 98,
      },
    ],
  },
  {
    id: "quotation",
    title: "Đã Gửi Báo Giá",
    colorClass: "bg-purple-500 text-purple-500",
    glowClass:
      "bg-gradient-to-r from-purple-500 to-pink-500 shadow-[0_0_15px_rgba(168,85,247,0.5)]",
    cards: [
      {
        id: 4,
        company: "Shopee VN",
        contact: "Phạm D",
        initials: "SP",
        avatarGradient: "from-orange-500 to-rose-500",
        request: "Year End Party + Cắm trại tại Vũng Tàu cho 80 người.",
        value: "82 Tr ₫",
        aiScore: 85,
      },
    ],
  },
  {
    id: "won",
    title: "Chốt Thành Công",
    colorClass: "bg-emerald-500 text-emerald-500",
    glowClass:
      "bg-gradient-to-r from-emerald-500 to-teal-400 shadow-[0_0_15px_rgba(16,185,129,0.5)]",
    cards: [],
  },
]);

const draggedCard = ref<any>(null);
const draggedFromColumn = ref<string | null>(null);

const onDragStart = (event: DragEvent, card: any, columnId: string) => {
  draggedCard.value = card;
  draggedFromColumn.value = columnId;
  if (event.dataTransfer) {
    event.dataTransfer.effectAllowed = "move";
    setTimeout(() => {
      (event.target as HTMLElement).style.opacity = "0.4";
    }, 0);
  }
};

const onDrop = (event: DragEvent, toColumnId: string) => {
  if (!draggedCard.value || !draggedFromColumn.value) return;
  if (draggedFromColumn.value !== toColumnId) {
    const fromCol = pipeline.value.find(
      (c) => c.id === draggedFromColumn.value,
    );
    if (fromCol)
      fromCol.cards = fromCol.cards.filter(
        (c) => c.id !== draggedCard.value.id,
      );
    const toCol = pipeline.value.find((c) => c.id === toColumnId);
    if (toCol) toCol.cards.push(draggedCard.value);
  }
  draggedCard.value = null;
  draggedFromColumn.value = null;
  const elements = document.querySelectorAll(".opacity-40");
  elements.forEach((el) => ((el as HTMLElement).style.opacity = "1"));
};
</script>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: scale(0.9) translateY(20px);
}
.custom-scrollbar::-webkit-scrollbar {
  height: 6px;
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
