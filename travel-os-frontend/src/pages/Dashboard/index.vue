<template>
  <div class="h-full flex flex-col space-y-8 pb-8">
    <div class="flex items-end justify-between shrink-0">
      <div class="relative">
        <div
          class="absolute -inset-1 bg-indigo-500/20 blur-xl rounded-full"
        ></div>
        <h1 class="relative text-3xl font-black text-white tracking-tight mb-2">
          Tổng Quan Doanh Nghiệp
        </h1>
        <p class="relative text-sm text-slate-400 font-medium">
          Chào mừng trở lại! Hệ thống AI đang hoạt động tối ưu.
        </p>
      </div>
      <button
        class="group relative px-6 py-3 bg-gradient-to-r from-indigo-500 to-purple-600 rounded-xl font-bold text-white shadow-[0_0_30px_rgba(99,102,241,0.4)] hover:shadow-[0_0_40px_rgba(99,102,241,0.6)] transition-all duration-300 hover:-translate-y-0.5 overflow-hidden"
      >
        <div
          class="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out"
        ></div>
        <span class="relative flex items-center gap-2"
          ><Plus class="w-5 h-5" /> Tạo Tour Mới</span
        >
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
      <div
        v-for="(stat, index) in stats"
        :key="index"
        class="glass-panel p-6 rounded-3xl relative overflow-hidden group hover:border-white/10 transition-colors duration-300 border border-white/5 bg-slate-900/40 shadow-xl"
      >
        <div
          class="absolute -right-12 -top-12 w-40 h-40 rounded-full blur-[40px] opacity-20 group-hover:opacity-40 transition-opacity duration-700"
          :class="stat.glowColor"
        ></div>

        <div class="flex justify-between items-start mb-6 relative z-10">
          <div
            class="w-12 h-12 rounded-2xl flex items-center justify-center border border-white/10 backdrop-blur-md shadow-inner"
            :class="stat.bgIconColor"
          >
            <component
              :is="stat.icon"
              class="w-6 h-6"
              :class="stat.iconColor"
            />
          </div>
          <div class="flex flex-col items-end">
            <span
              class="text-xs font-bold px-2.5 py-1 rounded-lg border flex items-center gap-1"
              :class="
                stat.trendUp
                  ? 'text-emerald-400 bg-emerald-400/10 border-emerald-400/20'
                  : 'text-rose-400 bg-rose-400/10 border-rose-400/20'
              "
            >
              <TrendingUp v-if="stat.trendUp" class="w-3 h-3" />
              <TrendingDown v-else class="w-3 h-3" />
              {{ stat.trend }}
            </span>
            <span class="text-[10px] text-slate-500 mt-1"
              >So với tháng trước</span
            >
          </div>
        </div>

        <div class="relative z-10">
          <h3
            class="text-slate-400 text-sm font-semibold mb-1 uppercase tracking-wider"
          >
            {{ stat.title }}
          </h3>
          <p
            class="text-3xl font-black text-white tracking-tight"
            style="font-family: &quot;SF Pro Display&quot;, sans-serif"
          >
            {{ stat.value }}
          </p>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 flex-1 min-h-[420px]">
      <div
        class="lg:col-span-2 glass-panel p-8 rounded-3xl flex flex-col border border-white/5 bg-slate-900/40 relative overflow-hidden shadow-2xl"
      >
        <div
          class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-1 bg-gradient-to-r from-transparent via-indigo-500/50 to-transparent"
        ></div>

        <div class="flex justify-between items-center mb-8 relative z-10">
          <div>
            <h3 class="text-xl font-bold text-white mb-1">
              Phân Tích Doanh Thu
            </h3>
            <p class="text-xs text-slate-400 font-medium">
              Dữ liệu tổng hợp theo thời gian thực
            </p>
          </div>
          <select
            class="bg-black/20 border border-white/10 text-sm font-medium text-white rounded-xl px-4 py-2 focus:outline-none focus:border-indigo-500 transition-colors appearance-none cursor-pointer hover:bg-white/5"
          >
            <option>Tháng này</option>
            <option>Quý này</option>
            <option>Năm nay</option>
          </select>
        </div>

        <div
          class="flex-1 flex items-end justify-between gap-3 px-2 pb-4 relative z-10"
        >
          <div
            class="absolute inset-0 flex flex-col justify-between pointer-events-none opacity-10"
          >
            <div
              v-for="n in 5"
              :key="n"
              class="w-full border-b border-white/50 h-0"
            ></div>
          </div>

          <div
            v-for="(col, i) in chartData"
            :key="i"
            class="w-full flex flex-col justify-end group cursor-pointer relative h-full"
          >
            <div
              class="w-full rounded-t-lg relative transition-all duration-500"
              :class="
                col.highlight
                  ? 'bg-gradient-to-t from-indigo-600 to-purple-400 shadow-[0_0_20px_rgba(129,140,248,0.4)]'
                  : 'bg-slate-700/50 group-hover:bg-indigo-500/50'
              "
              :style="{ height: `${col.height}%` }"
            >
              <div
                class="absolute inset-x-0 bottom-0 top-0 bg-white/20 rounded-t-lg opacity-0 group-hover:opacity-100 transition-opacity"
              ></div>
            </div>
            <div
              class="absolute -top-12 left-1/2 -translate-x-1/2 bg-slate-800 text-white text-xs font-bold px-3 py-1.5 rounded-lg opacity-0 group-hover:opacity-100 transition-all duration-300 border border-white/10 shadow-xl whitespace-nowrap z-20 pointer-events-none transform group-hover:-translate-y-1"
            >
              {{ col.value }} Tr
            </div>
          </div>
        </div>
        <div
          class="flex justify-between text-[11px] font-bold text-slate-500 uppercase mt-4 px-2 pt-4 border-t border-white/5 relative z-10"
        >
          <span
            v-for="month in [
              'T1',
              'T2',
              'T3',
              'T4',
              'T5',
              'T6',
              'T7',
              'T8',
              'T9',
              'T10',
              'T11',
              'T12',
            ]"
            :key="month"
            >{{ month }}</span
          >
        </div>
      </div>

      <div
        class="glass-panel p-8 rounded-3xl flex flex-col border border-white/5 bg-slate-900/40 relative shadow-2xl"
      >
        <div
          class="absolute top-0 right-1/2 translate-x-1/2 w-1/2 h-1 bg-gradient-to-r from-transparent via-emerald-500/30 to-transparent"
        ></div>

        <h3 class="text-xl font-bold text-white mb-6 relative z-10">
          Hoạt Động Gần Đây
        </h3>

        <div
          class="flex-1 overflow-y-auto pr-2 space-y-6 custom-scrollbar relative z-10"
        >
          <div
            v-for="(activity, index) in activities"
            :key="activity.id"
            class="relative flex gap-5 group cursor-pointer"
          >
            <div
              v-if="index !== activities.length - 1"
              class="absolute left-[11px] top-6 bottom-[-24px] w-[2px] bg-white/5 group-hover:bg-white/10 transition-colors"
            ></div>

            <div class="relative mt-1 shrink-0">
              <div
                class="w-6 h-6 rounded-full flex items-center justify-center bg-slate-800 border-2 border-slate-900 z-10 relative shadow-lg"
              >
                <div
                  class="w-2.5 h-2.5 rounded-full"
                  :class="activity.dotColor"
                ></div>
              </div>
              <div
                class="absolute inset-0 blur-sm opacity-50 rounded-full"
                :class="activity.dotColor"
              ></div>
            </div>

            <div
              class="flex-1 bg-white/0 group-hover:bg-white/[0.02] p-2 -my-2 rounded-xl transition-colors border border-transparent group-hover:border-white/5"
            >
              <p class="text-[13px] text-white font-bold leading-tight">
                {{ activity.title }}
              </p>
              <p
                class="text-xs text-slate-400 mt-1 line-clamp-2 leading-relaxed"
              >
                {{ activity.desc }}
              </p>
              <p
                class="text-[10px] font-bold text-slate-500 mt-2 uppercase tracking-wide"
              >
                {{ activity.time }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import {
  Plus,
  DollarSign,
  BrainCircuit,
  Users,
  CheckCircle,
  TrendingUp,
  TrendingDown,
} from "lucide-vue-next";

const stats = [
  {
    title: "Tổng Doanh Thu",
    value: "3.2 Tỷ ₫",
    trend: "14.5%",
    trendUp: true,
    icon: DollarSign,
    iconColor: "text-emerald-400",
    bgIconColor: "bg-emerald-500/10",
    glowColor: "bg-emerald-500",
  },
  {
    title: "Tour AI Đã Tạo",
    value: "1,248",
    trend: "32.1%",
    trendUp: true,
    icon: BrainCircuit,
    iconColor: "text-indigo-400",
    bgIconColor: "bg-indigo-500/10",
    glowColor: "bg-indigo-500",
  },
  {
    title: "Khách Hàng Mới",
    value: "342",
    trend: "2.4%",
    trendUp: false,
    icon: Users,
    iconColor: "text-rose-400",
    bgIconColor: "bg-rose-500/10",
    glowColor: "bg-rose-500",
  },
  {
    title: "Chốt Thành Công",
    value: "84%",
    trend: "12.0%",
    trendUp: true,
    icon: CheckCircle,
    iconColor: "text-amber-400",
    bgIconColor: "bg-amber-500/10",
    glowColor: "bg-amber-500",
  },
];

const chartData = [
  { height: 30, value: 120, highlight: false },
  { height: 45, value: 180, highlight: false },
  { height: 35, value: 140, highlight: false },
  { height: 60, value: 240, highlight: false },
  { height: 50, value: 200, highlight: false },
  { height: 80, value: 320, highlight: false },
  { height: 75, value: 300, highlight: false },
  { height: 95, value: 380, highlight: true }, // Tháng hiện tại
  { height: 40, value: 160, highlight: false },
  { height: 55, value: 220, highlight: false },
  { height: 65, value: 260, highlight: false },
  { height: 85, value: 340, highlight: false },
];

const activities = [
  {
    id: 1,
    title: "AI vừa tạo lịch trình mới",
    desc: "Tour Đà Lạt 3N2Đ cho tập đoàn FPT Software. Ngân sách 4 triệu/người.",
    time: "2 phút trước",
    dotColor: "bg-indigo-500",
  },
  {
    id: 2,
    title: "Thanh toán thành công",
    desc: "Hợp đồng INV-2026-849 đã được thanh toán qua chuyển khoản (120,000,000đ)",
    time: "15 phút trước",
    dotColor: "bg-emerald-500",
  },
  {
    id: 3,
    title: "Cảnh báo từ Map Engine",
    desc: "Tuyến đường đèo Prenn đang kẹt xe, AI đã tự động điều chỉnh lộ trình cho Tour #882",
    time: "1 giờ trước",
    dotColor: "bg-amber-500",
  },
  {
    id: 4,
    title: "Khách hàng VIP mới",
    desc: "Team nhân sự Vinamilk vừa đăng ký tư vấn qua landing page.",
    time: "3 giờ trước",
    dotColor: "bg-indigo-500",
  },
  {
    id: 5,
    title: "Điều phối Hướng Dẫn Viên",
    desc: "Nguyễn Văn A đã xác nhận dẫn đoàn Tour Đà Nẵng mã #901",
    time: "5 giờ trước",
    dotColor: "bg-slate-400",
  },
];
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
