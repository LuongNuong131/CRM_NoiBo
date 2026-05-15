package com.travelos.core.entity;

import jakarta.persistence.*;
import lombok.*;
import org.locationtech.jts.geom.Point;
import java.math.BigDecimal;
import java.time.LocalDateTime;

@Entity
@Table(name = "locations")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Location {
    @Id
    @Column(length = 36)
    private String id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String category;

    // Mapping kiểu dữ liệu POINT (Tọa độ Bản đồ)
    @Column(columnDefinition = "POINT SRID 4326", nullable = false)
    private Point coordinates;

    @Column(columnDefinition = "TEXT")
    private String address;

    private String city;
    private String province;

    @Column(precision = 3, scale = 2)
    private BigDecimal rating;

    @Column(name = "base_price", precision = 15, scale = 2)
    private BigDecimal basePrice;

    @Column(name = "created_at", insertable = false, updatable = false)
    private LocalDateTime createdAt;
}