<template>
  <header class="h-16 border-b border-os-border/30 bg-os-bg/50 backdrop-blur-md px-8 flex items-center justify-between sticky top-0 z-40">
    <div class="flex items-center space-x-4">
      <h2 class="text-lg font-medium text-os-muted">Overview</h2>
    </div>
    
    <div class="flex items-center space-x-4">
      <div class="relative group">
        <input 
          type="text" 
          placeholder="Search everything..." 
          class="bg-white/5 border border-os-border/50 rounded-full px-5 py-1.5 text-sm w-64 focus:outline-none focus:border-os-accent/50 transition-all focus:w-80"
        />
        <div class="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] bg-os-border px-1.5 py-0.5 rounded border border-white/10 text-os-muted">
          ⌘ K
        </div>
      </div>
      <button class="p-2 hover:bg-white/5 rounded-full relative">
        <div class="w-2 h-2 bg-red-500 rounded-full absolute top-2 right-2 border-2 border-os-bg"></div>
        <Bell class="w-5 h-5 text-os-muted" />
      </button>
    </div>
  </header>
</template>

<script setup lang="ts">
import { Bell } from 'lucide-vue-next'
</script>