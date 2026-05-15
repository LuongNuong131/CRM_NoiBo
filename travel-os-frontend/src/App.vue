<template>
  <div class="min-h-screen bg-os-bg relative overflow-hidden flex">
    <div
      class="fixed inset-0 pointer-events-none z-0 bg-[radial-gradient(ellipse_80%_50%_at_20%_0%,rgba(99,102,241,0.08)_0%,transparent_60%),radial-gradient(ellipse_60%_40%_at_80%_100%,rgba(139,92,246,0.08)_0%,transparent_60%)]"
    ></div>

    <div
      class="relative z-10 w-full flex items-center justify-center min-h-screen"
    >
      <div
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :enter="{ opacity: 1, y: 0, transition: { duration: 800 } }"
        class="glass-panel p-10 rounded-2xl text-center max-w-md w-full"
      >
        <h1
          class="text-3xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 to-purple-400 mb-4"
        >
          TravelOS
        </h1>
        <p class="text-os-muted mb-8">Next-Generation AI Travel System</p>

        <div class="flex justify-center space-x-2">
          <div
            class="w-3 h-3 rounded-full bg-indigo-500 animate-bounce"
            style="animation-delay: 0ms"
          ></div>
          <div
            class="w-3 h-3 rounded-full bg-indigo-500 animate-bounce"
            style="animation-delay: 150ms"
          ></div>
          <div
            class="w-3 h-3 rounded-full bg-indigo-500 animate-bounce"
            style="animation-delay: 300ms"
          ></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// Logic sẽ được thêm vào ở Phần 3
</script>
