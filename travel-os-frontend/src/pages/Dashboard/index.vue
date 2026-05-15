<template>
  <div class="h-full flex flex-col space-y-6">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-2xl font-bold text-white mb-1">Enterprise Overview</h1>
        <p class="text-sm text-os-muted">
          Welcome back, LuNu! System is operating at peak performance.
        </p>
      </div>
      <button
        class="bg-indigo-500 hover:bg-indigo-600 text-white px-5 py-2.5 rounded-xl text-sm font-medium transition flex items-center gap-2 shadow-[0_0_20px_rgba(99,102,241,0.3)]"
      >
        <Plus class="w-4 h-4" /> New AI Tour
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
      <div
        v-for="stat in stats"
        :key="stat.title"
        class="glass-panel p-6 rounded-2xl relative overflow-hidden group"
      >
        <div
          class="absolute -right-10 -top-10 w-32 h-32 rounded-full blur-3xl transition-all duration-500 group-hover:bg-opacity-20"
          :class="stat.glowColor"
        ></div>

        <div class="flex justify-between items-start mb-4 relative z-10">
          <div
            class="w-10 h-10 rounded-xl bg-white/5 flex items-center justify-center border border-white/10"
          >
            <component
              :is="stat.icon"
              class="w-5 h-5"
              :class="stat.iconColor"
            />
          </div>
          <span
            class="text-xs font-medium px-2 py-1 rounded-md"
            :class="
              stat.trendUp
                ? 'text-green-400 bg-green-400/10'
                : 'text-red-400 bg-red-400/10'
            "
          >
            {{ stat.trend }}
          </span>
        </div>

        <div class="relative z-10">
          <h3 class="text-os-muted text-sm font-medium mb-1">
            {{ stat.title }}
          </h3>
          <p class="text-3xl font-bold text-white tracking-tight">
            {{ stat.value }}
          </p>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 flex-1 min-h-[400px]">
      <div class="lg:col-span-2 glass-panel p-6 rounded-2xl flex flex-col">
        <div class="flex justify-between items-center mb-6">
          <h3 class="text-lg font-semibold text-white">Revenue Analytics</h3>
          <select
            class="bg-white/5 border border-os-border text-xs text-white rounded-lg px-3 py-1.5 focus:outline-none"
          >
            <option>Last 30 Days</option>
            <option>This Year</option>
          </select>
        </div>

        <div class="flex-1 flex items-end justify-between gap-2 px-2 pb-2">
          <div
            v-for="i in 12"
            :key="i"
            class="w-full bg-white/5 rounded-t-sm relative group cursor-pointer"
            :style="{ height: `${Math.floor(Math.random() * 70 + 20)}%` }"
          >
            <div
              class="absolute inset-x-0 bottom-0 top-0 bg-indigo-500/80 rounded-t-sm opacity-0 group-hover:opacity-100 transition-opacity"
            ></div>
            <div
              class="absolute -top-8 left-1/2 -translate-x-1/2 bg-os-panel text-white text-xs px-2 py-1 rounded opacity-0 group-hover:opacity-100 transition border border-os-border"
            >
              ${{ Math.floor(Math.random() * 50 + 10) }}k
            </div>
          </div>
        </div>
        <div
          class="flex justify-between text-[10px] text-os-muted uppercase mt-2 px-2 border-t border-os-border/50 pt-2"
        >
          <span>Jan</span><span>Feb</span><span>Mar</span><span>Apr</span
          ><span>May</span><span>Jun</span> <span>Jul</span><span>Aug</span
          ><span>Sep</span><span>Oct</span><span>Nov</span><span>Dec</span>
        </div>
      </div>

      <div class="glass-panel p-6 rounded-2xl flex flex-col">
        <h3 class="text-lg font-semibold text-white mb-6">Live Operations</h3>

        <div class="flex-1 overflow-y-auto pr-2 space-y-6">
          <div
            v-for="activity in activities"
            :key="activity.id"
            class="relative flex gap-4"
          >
            <div
              class="w-2 h-2 mt-1.5 rounded-full ring-4 ring-os-bg z-10 shrink-0"
              :class="activity.dotColor"
            ></div>
            <div
              class="absolute left-1 top-3 w-px h-full bg-os-border -z-0"
            ></div>
            <div>
              <p class="text-sm text-white font-medium">{{ activity.title }}</p>
              <p class="text-xs text-os-muted mt-0.5">{{ activity.desc }}</p>
              <p class="text-[10px] text-os-muted/70 mt-1">
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
import { Plus, DollarSign, BrainCircuit, Users, Map } from "lucide-vue-next";

const stats = [
  {
    title: "Total Revenue",
    value: "$128,430",
    trend: "+14.5%",
    trendUp: true,
    icon: DollarSign,
    iconColor: "text-emerald-400",
    glowColor: "bg-emerald-500",
  },
  {
    title: "AI Tours Generated",
    value: "1,248",
    trend: "+32.1%",
    trendUp: true,
    icon: BrainCircuit,
    iconColor: "text-indigo-400",
    glowColor: "bg-indigo-500",
  },
  {
    title: "Active Bookings",
    value: "342",
    trend: "-2.4%",
    trendUp: false,
    icon: Users,
    iconColor: "text-rose-400",
    glowColor: "bg-rose-500",
  },
  {
    title: "Active Destinations",
    value: "84",
    trend: "+12%",
    trendUp: true,
    icon: Map,
    iconColor: "text-amber-400",
    glowColor: "bg-amber-500",
  },
];

const activities = [
  {
    id: 1,
    title: "AI generated new itinerary",
    desc: "HCM to Da Lat (3D2N) for FPT Corp",
    time: "2 mins ago",
    dotColor: "bg-indigo-500",
  },
  {
    id: 2,
    title: "Booking Confirmed",
    desc: "INV-2026-849 paid via Stripe ($4,200)",
    time: "15 mins ago",
    dotColor: "bg-emerald-500",
  },
  {
    id: 3,
    title: "Map Engine Alert",
    desc: "Route optimization updated for Tour #882",
    time: "1 hour ago",
    dotColor: "bg-amber-500",
  },
  {
    id: 4,
    title: "New Customer CRM",
    desc: "Vinamilk HR Team registered",
    time: "3 hours ago",
    dotColor: "bg-indigo-500",
  },
  {
    id: 5,
    title: "Guide Assigned",
    desc: "Nguyen Van A assigned to Da Nang Trip",
    time: "5 hours ago",
    dotColor: "bg-slate-400",
  },
];
</script>
