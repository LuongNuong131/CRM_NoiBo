// travel-os-frontend/src/stores/tour.ts
import { defineStore } from "pinia";
import { ref } from "vue";

export const useTourStore = defineStore("tour", () => {
  const isGenerating = ref(false);
  const isSaving = ref(false);
  const currentTour = ref<any>(null);

  // Hàm gọi AI Gemini từ FastAPI
  const generateAITour = async (prompt: string) => {
    isGenerating.value = true;
    try {
      const res = await fetch("http://127.0.0.1:8000/api/v1/ai/generate-tour", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });
      if (!res.ok) throw new Error("AI đang bận, sếp thử lại nhé!");

      const data = await res.json();
      currentTour.value = data; // Lưu kết quả AI vào biến
    } catch (error) {
      console.error(error);
      alert(
        "Không thể kết nối với Bộ não AI (FastAPI). Sếp check lại cổng 8000 nhé!",
      );
    } finally {
      isGenerating.value = false;
    }
  };

  // Hàm lưu Hành trình vào MySQL Spatial
  const saveTourToDatabase = async () => {
    if (!currentTour.value) return;
    isSaving.value = true;
    try {
      const res = await fetch("http://127.0.0.1:8000/api/v1/tours/save", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(currentTour.value),
      });
      if (!res.ok) throw new Error("Lưu Database thất bại!");

      alert(
        "🎉 Đã lưu Hành trình Kỳ Lân vào Cơ sở dữ liệu Không gian thành công!",
      );
    } catch (error) {
      console.error(error);
      alert("Lỗi khi cất vào nhà kho MySQL!");
    } finally {
      isSaving.value = false;
    }
  };

  return {
    isGenerating,
    isSaving,
    currentTour,
    generateAITour,
    saveTourToDatabase,
  };
});
