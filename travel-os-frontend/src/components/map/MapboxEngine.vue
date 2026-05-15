<template>
  <div
    class="relative w-full h-full rounded-2xl overflow-hidden glass-panel border border-os-border/50 shadow-2xl"
  >
    <div ref="mapContainer" class="absolute inset-0"></div>

    <div class="absolute top-4 right-4 flex flex-col space-y-2 z-10">
      <button
        class="bg-os-panel/80 backdrop-blur border border-os-border p-2 rounded-lg text-white hover:text-os-accent transition"
      >
        <Map class="w-5 h-5" />
      </button>
      <button
        class="bg-os-panel/80 backdrop-blur border border-os-border p-2 rounded-lg text-white hover:text-os-accent transition"
      >
        <Navigation class="w-5 h-5" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from "vue";
import mapboxgl from "mapbox-gl";
import "mapbox-gl/dist/mapbox-gl.css";
import { Map, Navigation } from "lucide-vue-next";

const mapContainer = ref<HTMLElement | null>(null);
let map: mapboxgl.Map | null = null;

// Bạn cần thay thế MAPBOX_TOKEN bằng token thực tế lấy từ mapbox.com
const MAPBOX_TOKEN =
  "pk.eyJ1IjoiZGVtbyIsImEiOiJjbGo3b2w5bGEwMWhsM2xvM3h5cHgxM3V6In0.XXXX"; // <-- ĐỔI TOKEN Ở ĐÂY

onMounted(() => {
  if (!mapContainer.value) return;

  mapboxgl.accessToken = MAPBOX_TOKEN;

  map = new mapboxgl.Map({
    container: mapContainer.value,
    style: "mapbox://styles/mapbox/dark-v11", // Dark mode cinematic
    center: [106.6958, 10.7769], // Tọa độ mặc định: Hồ Chí Minh
    zoom: 13,
    pitch: 45, // Góc nghiêng 3D
    bearing: -17.6,
    antialias: true,
  });

  map.on("load", () => {
    // Thêm hiệu ứng 3D Building
    const layers = map?.getStyle().layers;
    const labelLayerId = layers?.find(
      (layer) => layer.type === "symbol" && layer.layout?.["text-field"],
    )?.id;

    map?.addLayer(
      {
        id: "add-3d-buildings",
        source: "composite",
        "source-layer": "building",
        filter: ["==", "extrude", "true"],
        type: "fill-extrusion",
        minzoom: 15,
        paint: {
          "fill-extrusion-color": "#1e293b",
          "fill-extrusion-height": [
            "interpolate",
            ["linear"],
            ["zoom"],
            15,
            0,
            15.05,
            ["get", "height"],
          ],
          "fill-extrusion-base": [
            "interpolate",
            ["linear"],
            ["zoom"],
            15,
            0,
            15.05,
            ["get", "min_height"],
          ],
          "fill-extrusion-opacity": 0.6,
        },
      },
      labelLayerId,
    );
  });
});

onUnmounted(() => {
  if (map) {
    map.remove();
  }
});
</script>

<style>
/* Ẩn logo mapbox để giao diện clean hơn (Chỉ dùng cho nội bộ/Dev) */
.mapboxgl-ctrl-logo,
.mapboxgl-ctrl-attrib {
  display: none !important;
}
</style>
