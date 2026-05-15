<template>
  <div class="fixed bottom-6 right-6 z-[9999] flex flex-col items-end">
    <transition name="scale-up">
      <div
        v-if="isOpen"
        class="mb-4 w-[380px] h-[500px] glass-panel bg-slate-900/80 backdrop-blur-2xl border border-white/10 rounded-3xl shadow-[0_10px_50px_rgba(0,0,0,0.5)] flex flex-col overflow-hidden relative"
      >
        <div
          class="absolute -top-20 -right-20 w-40 h-40 bg-indigo-500/20 blur-3xl rounded-full"
        ></div>
        <div
          class="absolute -bottom-20 -left-20 w-40 h-40 bg-purple-500/20 blur-3xl rounded-full"
        ></div>

        <div
          class="p-4 border-b border-white/5 flex items-center justify-between bg-white/[0.02] relative z-10"
        >
          <div class="flex items-center gap-3">
            <div
              class="w-8 h-8 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-lg"
            >
              <Sparkles class="w-4 h-4 text-white" />
            </div>
            <div>
              <h3 class="text-sm font-bold text-white">TravelOS Copilot</h3>
              <p
                class="text-[10px] text-emerald-400 font-medium flex items-center gap-1"
              >
                <span
                  class="w-1.5 h-1.5 bg-emerald-400 rounded-full animate-pulse"
                ></span>
                Đang trực tuyến
              </p>
            </div>
          </div>
          <button
            @click="isOpen = false"
            class="text-slate-400 hover:text-white transition-colors bg-white/5 hover:bg-white/10 p-1.5 rounded-lg"
          >
            <X class="w-4 h-4" />
          </button>
        </div>

        <div
          class="flex-1 overflow-y-auto p-4 space-y-4 custom-scrollbar relative z-10"
          ref="chatContainer"
        >
          <div
            v-for="(msg, index) in messages"
            :key="index"
            class="flex"
            :class="msg.role === 'user' ? 'justify-end' : 'justify-start'"
          >
            <div
              v-if="msg.role === 'ai'"
              class="w-6 h-6 rounded-full bg-indigo-500/20 border border-indigo-500/50 flex items-center justify-center shrink-0 mr-2 mt-1"
            >
              <Bot class="w-3 h-3 text-indigo-400" />
            </div>

            <div
              class="max-w-[80%] p-3 rounded-2xl text-sm leading-relaxed shadow-md"
              :class="
                msg.role === 'user'
                  ? 'bg-gradient-to-br from-indigo-500 to-purple-600 text-white rounded-tr-sm'
                  : 'bg-white/5 border border-white/5 text-slate-200 rounded-tl-sm'
              "
            >
              {{ msg.content }}
            </div>
          </div>

          <div v-if="isTyping" class="flex justify-start">
            <div
              class="w-6 h-6 rounded-full bg-indigo-500/20 border border-indigo-500/50 flex items-center justify-center shrink-0 mr-2"
            >
              <Bot class="w-3 h-3 text-indigo-400" />
            </div>
            <div
              class="bg-white/5 border border-white/5 p-3 rounded-2xl rounded-tl-sm flex items-center gap-1"
            >
              <div
                class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"
                style="animation-delay: 0ms"
              ></div>
              <div
                class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"
                style="animation-delay: 150ms"
              ></div>
              <div
                class="w-1.5 h-1.5 bg-slate-400 rounded-full animate-bounce"
                style="animation-delay: 300ms"
              ></div>
            </div>
          </div>
        </div>

        <div class="p-3 border-t border-white/5 bg-black/20 relative z-10">
          <div
            class="relative flex items-center bg-white/5 border border-white/10 rounded-xl p-1 focus-within:border-indigo-500/50 focus-within:bg-white/10 transition-colors shadow-inner"
          >
            <input
              v-model="currentInput"
              @keyup.enter="sendMessage"
              type="text"
              placeholder="Hỏi tôi bất cứ điều gì..."
              class="flex-1 bg-transparent border-none text-white text-sm px-3 focus:outline-none placeholder-slate-500"
            />
            <button
              @click="sendMessage"
              :disabled="!currentInput.trim() || isTyping"
              class="w-8 h-8 rounded-lg bg-indigo-500 hover:bg-indigo-600 disabled:bg-white/5 disabled:text-slate-500 text-white flex items-center justify-center transition-colors shrink-0"
            >
              <Send class="w-4 h-4 ml-0.5" />
            </button>
          </div>
        </div>
      </div>
    </transition>

    <button
      v-if="!isOpen"
      @click="isOpen = true"
      class="group relative w-14 h-14 rounded-full bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-[0_10px_30px_rgba(99,102,241,0.5)] hover:shadow-[0_10px_40px_rgba(99,102,241,0.7)] transition-all duration-300 hover:-translate-y-1"
    >
      <div
        class="absolute inset-0 rounded-full bg-white/20 scale-0 group-hover:scale-100 transition-transform duration-300"
      ></div>
      <Sparkles
        class="w-6 h-6 text-white relative z-10 group-hover:animate-pulse"
      />

      <div
        class="absolute inset-0 rounded-full border-2 border-indigo-400 animate-ping opacity-20"
      ></div>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, nextTick } from "vue";
import { Sparkles, X, Send, Bot } from "lucide-vue-next";

const isOpen = ref(false);
const currentInput = ref("");
const isTyping = ref(false);
const chatContainer = ref<HTMLElement | null>(null);

const messages = ref([
  {
    role: "ai",
    content:
      "Xin chào LuNu! Tôi là trợ lý AI của hệ thống TravelOS. Tôi có thể giúp gì cho sếp hôm nay?",
  },
]);

const scrollToBottom = async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

const sendMessage = () => {
  if (!currentInput.value.trim() || isTyping.value) return;

  // Thêm tin nhắn user
  messages.value.push({ role: "user", content: currentInput.value });
  const userQuery = currentInput.value;
  currentInput.value = "";
  scrollToBottom();

  // Giả lập AI trả lời (Sau này bạn có thể nối với FastAPI Gemini)
  isTyping.value = true;
  scrollToBottom();

  setTimeout(() => {
    isTyping.value = false;
    messages.value.push({
      role: "ai",
      content: `Sếp vừa hỏi về: "${userQuery}". Tính năng gọi API cho Chat tự do đang được team kỹ sư xây dựng. Tạm thời sếp hãy dùng chức năng Thiết Kế Tour AI nhé!`,
    });
    scrollToBottom();
  }, 1500);
};
</script>

<style scoped>
.scale-up-enter-active,
.scale-up-leave-active {
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: bottom right;
}
.scale-up-enter-from,
.scale-up-leave-to {
  opacity: 0;
  transform: scale(0.8) translateY(20px);
}

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
