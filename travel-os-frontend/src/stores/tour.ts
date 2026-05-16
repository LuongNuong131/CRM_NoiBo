// travel-os-frontend/src/stores/tour.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useTourStore = defineStore("tour", () => {
  const isGenerating = ref(false);
  const isSaving = ref(false);
  const currentTour = ref<any>(null);

  const tourTitle = computed<string>(
    () => currentTour.value?.title ?? "Chưa có lịch trình",
  );

  const estimatedCost = computed<string>(
    () => currentTour.value?.estimated_cost_per_person ?? "---",
  );

  const itinerary = computed<any[]>(() => currentTour.value?.itinerary ?? []);

  const mapCoordinates = computed<[number, number][]>(() => {
    if (!currentTour.value?.itinerary) return [];
    const coords: [number, number][] = [];
    let i = 0;
    for (const day of currentTour.value.itinerary) {
      for (const node of day.nodes ?? []) {
        const lng = node.longitude ?? 106.6958 + i * 0.003;
        const lat = node.latitude ?? 10.7769 + i * 0.005;
        coords.push([lng, lat]);
        i++;
      }
    }
    return coords;
  });

  const generateAITour = async (prompt: string) => {
    isGenerating.value = true;
    currentTour.value = null;
    try {
      const res = await fetch("http://127.0.0.1:8000/api/v1/ai/generate-tour", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });
      if (!res.ok) throw new Error("AI đang bận, sếp thử lại nhé!");
      currentTour.value = await res.json();
    } catch (error) {
      console.error(error);
      alert(
        "Không thể kết nối với Bộ não AI (FastAPI). Sếp check lại cổng 8000 nhé!",
      );
    } finally {
      isGenerating.value = false;
    }
  };

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
      alert("🎉 Đã lưu Hành trình vào Cơ sở dữ liệu thành công!");
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
    tourTitle,
    estimatedCost,
    itinerary,
    mapCoordinates,
    generateAITour,
    saveTourToDatabase,
  };
});
