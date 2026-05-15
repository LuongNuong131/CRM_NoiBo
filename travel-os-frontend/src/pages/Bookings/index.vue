<template>
  <div class="h-full flex flex-col space-y-6">
    <div class="flex items-center justify-between shrink-0">
      <div>
        <h1 class="text-3xl font-black text-white tracking-tight mb-2">
          Hợp Đồng & Đặt Chỗ
        </h1>
        <p class="text-sm text-slate-400 font-medium">
          Quản lý vé, hợp đồng, và tình trạng thanh toán của khách hàng.
        </p>
      </div>
      <button
        class="bg-indigo-500 hover:bg-indigo-600 text-white px-6 py-2.5 rounded-xl text-sm font-bold transition-all shadow-[0_0_20px_rgba(99,102,241,0.4)]"
      >
        + Tạo Đặt Chỗ Mới
      </button>
    </div>

    <div
      class="flex-1 glass-panel bg-slate-900/40 border border-white/5 rounded-3xl overflow-hidden shadow-2xl flex flex-col"
    >
      <div class="overflow-x-auto">
        <table class="w-full text-left border-collapse">
          <thead>
            <tr
              class="bg-white/[0.02] border-b border-white/5 text-xs uppercase tracking-wider text-slate-400"
            >
              <th class="p-5 font-bold">Mã Booking</th>
              <th class="p-5 font-bold">Khách Hàng / Công Ty</th>
              <th class="p-5 font-bold">Tên Tour</th>
              <th class="p-5 font-bold">Ngày Khởi Hành</th>
              <th class="p-5 font-bold">Tổng Tiền</th>
              <th class="p-5 font-bold">Trạng Thái</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-white/5">
            <tr
              v-for="bk in bookings"
              :key="bk.id"
              class="hover:bg-white/[0.02] transition-colors cursor-pointer group"
            >
              <td class="p-5 text-sm font-bold text-indigo-400">
                {{ bk.code }}
              </td>
              <td class="p-5">
                <p class="text-sm font-bold text-white">{{ bk.client }}</p>
                <p class="text-xs text-slate-500">{{ bk.pax }} Khách</p>
              </td>
              <td class="p-5 text-sm text-slate-300 font-medium">
                {{ bk.tour }}
              </td>
              <td class="p-5 text-sm text-slate-300">{{ bk.date }}</td>
              <td class="p-5 text-sm font-black text-white">{{ bk.amount }}</td>
              <td class="p-5">
                <span
                  class="px-3 py-1 text-xs font-bold rounded-lg border"
                  :class="{
                    'bg-emerald-500/10 text-emerald-400 border-emerald-500/20':
                      bk.status === 'Đã Thanh Toán',
                    'bg-amber-500/10 text-amber-400 border-amber-500/20':
                      bk.status === 'Đặt Cọc',
                    'bg-slate-500/10 text-slate-400 border-slate-500/20':
                      bk.status === 'Đang Chờ',
                  }"
                >
                  {{ bk.status }}
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const bookings = [
  {
    id: 1,
    code: "BK-2609",
    client: "Tập đoàn FPT",
    pax: 150,
    tour: "Đà Lạt Mộng Mơ 3N2Đ",
    date: "25/08/2026",
    amount: "600,000,000 ₫",
    status: "Đặt Cọc",
  },
  {
    id: 2,
    code: "BK-2610",
    client: "Gia đình chị Hoa",
    pax: 4,
    tour: "Phú Quốc Nghỉ Dưỡng",
    date: "12/09/2026",
    amount: "45,000,000 ₫",
    status: "Đã Thanh Toán",
  },
  {
    id: 3,
    code: "BK-2611",
    client: "Công ty ABC",
    pax: 45,
    tour: "Team Building Vũng Tàu",
    date: "01/10/2026",
    amount: "112,500,000 ₫",
    status: "Đang Chờ",
  },
];
</script>
