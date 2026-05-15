<template>
  <div class="h-full flex flex-col space-y-6">
    <h1 class="text-3xl font-black text-white tracking-tight mb-2">
      Tài Chính & Kế Toán
    </h1>

    <div class="grid grid-cols-3 gap-6">
      <div
        class="glass-panel p-6 rounded-3xl border border-white/5 bg-gradient-to-br from-emerald-500/10 to-transparent"
      >
        <p class="text-slate-400 text-sm font-bold uppercase mb-2">
          Tiền Mặt Khả Dụng
        </p>
        <p class="text-4xl font-black text-emerald-400">1.8 Tỷ ₫</p>
      </div>
      <div
        class="glass-panel p-6 rounded-3xl border border-white/5 bg-gradient-to-br from-rose-500/10 to-transparent"
      >
        <p class="text-slate-400 text-sm font-bold uppercase mb-2">
          Công Nợ Phải Thu
        </p>
        <p class="text-4xl font-black text-rose-400">450 Tr ₫</p>
      </div>
      <div
        class="glass-panel p-6 rounded-3xl border border-white/5 bg-gradient-to-br from-indigo-500/10 to-transparent"
      >
        <p class="text-slate-400 text-sm font-bold uppercase mb-2">
          Lợi Nhuận Gộp (Tháng)
        </p>
        <p class="text-4xl font-black text-indigo-400">820 Tr ₫</p>
      </div>
    </div>

    <div
      class="flex-1 glass-panel bg-slate-900/40 border border-white/5 rounded-3xl p-6"
    >
      <h3 class="text-xl font-bold text-white mb-6">Giao Dịch Gần Đây</h3>
      <div class="space-y-4">
        <div
          v-for="i in 5"
          :key="i"
          class="flex items-center justify-between p-4 bg-white/[0.02] rounded-2xl border border-white/5"
        >
          <div class="flex items-center gap-4">
            <div
              class="w-10 h-10 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 font-bold"
            >
              ↓
            </div>
            <div>
              <p class="text-white font-bold">
                Thanh toán cọc Tour BK-260{{ i }}
              </p>
              <p class="text-xs text-slate-500">Chuyển khoản Vietcombank</p>
            </div>
          </div>
          <span class="font-black text-emerald-400">+ 150,000,000 ₫</span>
        </div>
      </div>
    </div>
  </div>
</template>
