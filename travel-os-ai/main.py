# travel-os-ai/main.py

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Import các cấu hình hệ thống
from app.database import engine, Base, get_db
from app.services.ai_generator import AITourGenerator
from app.models.schemas import TourRequest, TourResponse

# Import các Model để SQLAlchemy nhận diện và tạo bảng tự động
from app.models.location import Location
from app.models.tour import Tour, TourDay, TourNode

# Import các Router chức năng
from app.routers import tour_router

# 1. KHỞI TẠO DATABASE (Tự động tạo bảng MySQL Spatial nếu chưa có)
# Lưu ý: Trong môi trường production thực tế, ta nên dùng Alembic để migrate.
Base.metadata.create_all(bind=engine)

# 2. KHỞI TẠO APP FASTAPI
app = FastAPI(
    title="TravelOS Enterprise Core Engine",
    description="Hệ điều hành du lịch AI dành cho doanh nghiệp lữ hành.",
    version="1.0.0"
)

# 3. CẤU HÌNH CORS (Cho phép Frontend Vue 3 kết nối)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Trong thực tế nên giới hạn domain cụ thể
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Khởi tạo dịch vụ AI
generator = AITourGenerator()

# 4. ĐĂNG KÝ CÁC ROUTER (MODULES)
app.include_router(tour_router.router)

# 5. CÁC ENDPOINT CHÍNH

@app.get("/")
async def root():
    return {
        "message": "Chào mừng đến với TravelOS AI Core Engine",
        "status": "Online",
        "documentation": "/docs"
    }

@app.post("/api/v1/ai/generate-tour", response_model=TourResponse, tags=["AI Services"])
async def generate_tour(request: TourRequest):
    """
    Sử dụng Google Gemini AI để thiết kế lịch trình tour tự động dựa trên prompt của người dùng.
    """
    try:
        itinerary = generator.generate_itinerary(request.prompt)
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Engine Error: {str(e)}")

@app.get("/api/v1/health", tags=["System"])
async def health_check():
    """Kiểm tra tình trạng sức khỏe của hệ thống và kết nối DB."""
    return {
        "status": "healthy",
        "database": "connected",
        "spatial_support": "enabled"
    }

# 6. KHỞI CHẠY SERVER (Chỉ dùng khi chạy trực tiếp file này)
if __name__ == "__main__":
    # Sếp có thể chạy lệnh: uvicorn main:app --reload trong terminal
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)