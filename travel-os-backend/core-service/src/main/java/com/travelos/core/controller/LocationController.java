package com.travelos.core.controller;

import com.travelos.core.entity.Location;
import com.travelos.core.repository.LocationRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/locations")
@RequiredArgsConstructor
@CrossOrigin(origins = "*") // Tạm thời mở CORS cho Frontend Vue 3 gọi
public class LocationController {

    private final LocationRepository locationRepository;

    // API tìm kiếm địa điểm xung quanh tọa độ
    // Ví dụ: GET /api/v1/locations/nearby?lng=106.6958&lat=10.7769&radius=5000
    @GetMapping("/nearby")
    public ResponseEntity<List<Location>> getNearbyLocations(
            @RequestParam double lng,
            @RequestParam double lat,
            @RequestParam(defaultValue = "5000") double radius) { // Mặc định tìm trong bán kính 5km
        
        List<Location> nearby = locationRepository.findNearbyLocations(lng, lat, radius);
        return ResponseEntity.ok(nearby);
    }
    
    // API lấy tất cả
    @GetMapping
    public ResponseEntity<List<Location>> getAllLocations() {
        return ResponseEntity.ok(locationRepository.findAll());
    }
}