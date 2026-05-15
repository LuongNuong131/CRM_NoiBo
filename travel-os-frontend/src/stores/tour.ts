import { defineStore } from "pinia";
import axios from "axios";

export const useTourStore = defineStore("tour", {
  state: () => ({
    isGenerating: false,
    tourTitle: "Chưa có lịch trình",
    estimatedCost: "0",
    itinerary: [] as any[],
    mapCoordinates: [] as [number, number][],
  }),

  actions: {
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
            // Dùng Nominatim API (Free, không cần token)
            const res = await axios.get(
              `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(node.title + ", Vietnam")}&limit=1`,
            );
            if (res.data && res.data.length > 0) {
              const item = res.data[0];
              const lng = parseFloat(item.lon);
              const lat = parseFloat(item.lat);
              coords.push([lng, lat]);
              node.coordinates = [lng, lat];
            }
          } catch (err) {
            console.error("Geocoding error:", node.title);
          }
        }
      }
      this.mapCoordinates = coords;
    },
  },
});
