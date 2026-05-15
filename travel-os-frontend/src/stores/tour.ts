import { defineStore } from "pinia";
import axios from "axios";

export const useTourStore = defineStore("tour", {
  state: () => ({
    isGenerating: false,
    tourTitle: "Hành trình mới",
    estimatedCost: "0 ₫",
    itinerary: [] as any[],
    mapCoordinates: [] as [number, number][],
    searchResults: [] as any[], // Kết quả tìm kiếm thủ công
    isSearching: false,
  }),

  actions: {
    // --- PHẦN 1: AI GENERATOR ---
    async generateAITour(prompt: string) {
      this.isGenerating = true;
      this.mapCoordinates = [];
      try {
        const response = await axios.post(
          "http://localhost:8000/api/v1/ai/generate-tour",
          { prompt },
        );
        this.tourTitle = response.data.title;
        this.estimatedCost = response.data.estimated_cost_per_person;
        this.itinerary = response.data.itinerary;
        await this.geocodeItinerary();
      } catch (error) {
        console.error("AI Error:", error);
      } finally {
        this.isGenerating = false;
      }
    },

    async geocodeItinerary() {
      const coords: [number, number][] = [];
      for (const day of this.itinerary) {
        for (const node of day.nodes) {
          try {
            const res = await axios.get(
              `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(node.title + ", Vietnam")}&limit=1`,
            );
            if (res.data && res.data.length > 0) {
              const lng = parseFloat(res.data[0].lon);
              const lat = parseFloat(res.data[0].lat);
              coords.push([lng, lat]);
              node.coordinates = [lng, lat];
            }
          } catch (err) {}
        }
      }
      this.mapCoordinates = coords;
    },

    // --- PHẦN 2: THỦ CÔNG (MANUAL BUILDER) ---
    async searchLocationManual(query: string) {
      if (!query.trim()) {
        this.searchResults = [];
        return;
      }
      this.isSearching = true;
      try {
        const res = await axios.get(
          `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(query)}&limit=5`,
        );
        this.searchResults = res.data;
      } catch (error) {
        console.error("Search Error:", error);
      } finally {
        this.isSearching = false;
      }
    },

    addNewDay() {
      const newDayNum = this.itinerary.length + 1;
      this.itinerary.push({ day: newDayNum, nodes: [] });
    },

    addManualNode(dayIndex: number, place: any, type: string = "attraction") {
      const lng = parseFloat(place.lon);
      const lat = parseFloat(place.lat);

      const newNode = {
        title: place.display_name.split(",")[0],
        type: type,
        time: "Tùy chỉnh",
        description: place.display_name,
        coordinates: [lng, lat],
      };

      this.itinerary[dayIndex].nodes.push(newNode);

      // Cập nhật lại đường vẽ trên bản đồ
      this.mapCoordinates.push([lng, lat]);
      this.searchResults = []; // Xóa kết quả sau khi thêm
    },
  },
});
