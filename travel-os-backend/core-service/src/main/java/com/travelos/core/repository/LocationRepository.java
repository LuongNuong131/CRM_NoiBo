package com.travelos.core.repository;

import com.travelos.core.entity.Location;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface LocationRepository extends JpaRepository<Location, String> {

    // Truy vấn Native siêu tốc dùng ST_Distance_Sphere để tìm các địa điểm lân cận theo bán kính (mét)
    @Query(value = "SELECT * FROM locations l WHERE ST_Distance_Sphere(l.coordinates, ST_GeomFromText(CONCAT('POINT(', ?1, ' ', ?2, ')'), 4326)) <= ?3", nativeQuery = true)
    List<Location> findNearbyLocations(double longitude, double latitude, double radiusInMeters);
}