-- travel-os-enterprise/infra/mysql/init-schema.sql

CREATE DATABASE IF NOT EXISTS travel_os_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE travel_os_db;

-- ====================================================
-- 1. AUTHENTICATION & SECURITY (RBAC)
-- ====================================================
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY, -- Dùng UUID
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    avatar_url VARCHAR(500),
    role ENUM('SUPER_ADMIN', 'ADMIN', 'SALES', 'OPERATOR', 'GUIDE', 'ACCOUNTANT', 'CUSTOMER_CARE') DEFAULT 'SALES',
    status ENUM('ACTIVE', 'INACTIVE', 'BANNED') DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE user_sessions (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    refresh_token VARCHAR(500) NOT NULL,
    device_info VARCHAR(255),
    ip_address VARCHAR(45),
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- ====================================================
-- 2. CRM & CUSTOMERS
-- ====================================================
CREATE TABLE customers (
    id VARCHAR(36) PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    customer_type ENUM('INDIVIDUAL', 'CORPORATE', 'VIP') DEFAULT 'INDIVIDUAL',
    company_name VARCHAR(255),
    assigned_to VARCHAR(36), -- Sales phụ trách
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (assigned_to) REFERENCES users(id) ON DELETE SET NULL
);

-- ====================================================
-- 3. SPATIAL DATA: LOCATIONS & SUPPLIERS
-- ====================================================
CREATE TABLE locations (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category ENUM('ATTRACTION', 'HOTEL', 'RESTAURANT', 'REST_STOP', 'HOSPITAL', 'GAS_STATION') NOT NULL,
    -- Trường lưu trữ tọa độ POINT (Longitude, Latitude)
    coordinates POINT NOT NULL SRID 4326, 
    address TEXT,
    city VARCHAR(100),
    province VARCHAR(100),
    rating DECIMAL(3,2) DEFAULT 0.0,
    base_price DECIMAL(15,2) DEFAULT 0.00,
    metadata JSON, -- Lưu các thông tin linh hoạt (hình ảnh, giờ mở cửa...)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Đánh index không gian để search nearby siêu nhanh
    SPATIAL INDEX idx_coordinates (coordinates)
);

-- ====================================================
-- 4. CORE: SMART TOUR & ITINERARY (Trái tim hệ thống)
-- ====================================================
CREATE TABLE tours (
    id VARCHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    days INT NOT NULL,
    nights INT NOT NULL,
    budget_per_person DECIMAL(15,2) NOT NULL,
    start_location_id VARCHAR(36),
    status ENUM('DRAFT', 'ACTIVE', 'ARCHIVED') DEFAULT 'DRAFT',
    created_by VARCHAR(36),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (start_location_id) REFERENCES locations(id) ON DELETE SET NULL,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);

-- Bảng chứa các điểm dừng trên Timeline kéo thả
CREATE TABLE itinerary_nodes (
    id VARCHAR(36) PRIMARY KEY,
    tour_id VARCHAR(36) NOT NULL,
    location_id VARCHAR(36) NOT NULL,
    day_number INT NOT NULL,
    sequence_order INT NOT NULL,
    arrival_time TIME,
    departure_time TIME,
    distance_from_previous INT DEFAULT 0, -- Tính bằng mét
    estimated_travel_time INT DEFAULT 0,  -- Tính bằng phút
    estimated_cost DECIMAL(15,2) DEFAULT 0.00,
    transport_mode ENUM('BUS', 'CAR', 'FLIGHT', 'TRAIN', 'WALKING') DEFAULT 'BUS',
    notes TEXT,
    FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES locations(id) ON DELETE RESTRICT
);

-- ====================================================
-- 5. BOOKING & FINANCE
-- ====================================================
CREATE TABLE bookings (
    id VARCHAR(36) PRIMARY KEY,
    booking_code VARCHAR(20) UNIQUE NOT NULL,
    tour_id VARCHAR(36) NOT NULL,
    customer_id VARCHAR(36) NOT NULL,
    total_guests INT NOT NULL,
    total_amount DECIMAL(15,2) NOT NULL,
    paid_amount DECIMAL(15,2) DEFAULT 0.00,
    status ENUM('PENDING', 'CONFIRMED', 'PAID', 'CANCELLED', 'REFUNDED') DEFAULT 'PENDING',
    created_by VARCHAR(36),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tour_id) REFERENCES tours(id) ON DELETE RESTRICT,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE RESTRICT,
    FOREIGN KEY (created_by) REFERENCES users(id) ON DELETE SET NULL
);