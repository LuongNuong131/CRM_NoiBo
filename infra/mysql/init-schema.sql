-- infra/mysql/init-schema.sql

CREATE DATABASE IF NOT EXISTS travel_os_db DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE travel_os_db;

-- Bảng Địa điểm (Locations) sử dụng tọa độ Không gian (Spatial)
CREATE TABLE locations (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL COMMENT 'HOTEL, RESTAURANT, ATTRACTION, COFFEE',
    address VARCHAR(500),
    -- Kiểu POINT lưu trữ Kinh độ/Vĩ độ, SRID 4326 là chuẩn GPS Trái Đất
    coordinates POINT NOT NULL SRID 4326, 
    base_cost DECIMAL(15, 2) DEFAULT 0.00,
    rating FLOAT DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Đánh index không gian để query bán kính cực nhanh
    SPATIAL INDEX spatial_idx_coordinates (coordinates)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Bảng Khách hàng (Leads/CRM)
CREATE TABLE crm_leads (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    budget_estimation DECIMAL(15, 2),
    ai_win_probability INT DEFAULT 0 COMMENT 'Điểm AI dự đoán chốt deal (0-100)',
    status VARCHAR(50) DEFAULT 'NEW_LEAD' COMMENT 'NEW_LEAD, CONTACTED, QUOTATION, WON',
    requirements TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insert thử 1 địa điểm mẫu (Dinh Độc Lập)
INSERT INTO locations (name, type, address, coordinates) 
VALUES ('Dinh Độc Lập', 'ATTRACTION', '135 Nam Kỳ Khởi Nghĩa, TP.HCM', ST_GeomFromText('POINT(106.6958 10.7769)', 4326));