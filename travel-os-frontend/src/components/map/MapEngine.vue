<template>
  <div
    class="relative w-full h-full rounded-2xl overflow-hidden glass-panel border border-os-border/50 shadow-2xl"
  >
    <div id="map" class="absolute inset-0 z-0"></div>

    <div class="absolute top-4 right-4 flex flex-col space-y-2 z-[1000]">
      <button
        @click="resetView"
        class="bg-os-panel/80 backdrop-blur border border-os-border p-2 rounded-lg text-white hover:text-os-accent transition shadow-lg"
      >
        <Navigation class="w-5 h-5" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import { Navigation } from "lucide-vue-next";
import { useTourStore } from "@/stores/tour";

const tourStore = useTourStore();
let map: L.Map | null = null;
let polyline: L.Polyline | null = null;
let markers: L.Marker[] = [];

onMounted(() => {
  // Khởi tạo bản đồ với OpenStreetMap (Free 100%)
  map = L.map("map", { zoomControl: false }).setView([10.7769, 106.6958], 13);

  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution: "&copy; OpenStreetMap contributors",
  }).addTo(map);
});

const resetView = () => {
  if (map && tourStore.mapCoordinates.length > 0) {
    const bounds = L.latLngBounds(
      tourStore.mapCoordinates.map((c) => [c[1], c[0]]),
    );
    map.fitBounds(bounds, { padding: [50, 50] });
  }
};

// Theo dõi tọa độ từ Store để vẽ lại
watch(
  () => tourStore.mapCoordinates,
  (newCoords) => {
    if (!map || newCoords.length === 0) return;

    // Xóa Marker và Line cũ
    markers.forEach((m) => m.remove());
    markers = [];
    if (polyline) polyline.remove();

    const leafletCoords = newCoords.map((c) => L.latLng(c[1], c[0]));

    // Vẽ Marker mới
    leafletCoords.forEach((latlng, index) => {
      const marker = L.circleMarker(latlng, {
        radius: 10,
        fillColor: "#8b5cf6",
        color: "#fff",
        weight: 3,
        opacity: 1,
        fillOpacity: 0.8,
      })
        .addTo(map!)
        .bindPopup(`Trạm ${index + 1}`);
      markers.push(marker);
    });

    // Vẽ đường nối
    polyline = L.polyline(leafletCoords, {
      color: "#8b5cf6",
      weight: 4,
      dashArray: "10, 10",
      opacity: 0.7,
    }).addTo(map);

    // Tự động bay tới khu vực có tour
    map.fitBounds(L.latLngBounds(leafletCoords), { padding: [50, 50] });
  },
  { deep: true },
);
</script>

<style>
/* Ẩn logo Leaflet cho chuyên nghiệp */
.leaflet-control-attribution {
  display: none !important;
}
.glass-panel {
  background: rgba(15, 23, 42, 0.6);
  backdrop-filter: blur(12px);
}
</style>
