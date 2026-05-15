from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# ==========================================
# SCHEMAS CHO AI TOUR GENERATOR
# ==========================================

class ItineraryNode(BaseModel):
    title: str = Field(..., description="Tên địa điểm hoặc hoạt động")
    type: str = Field(..., description="Loại điểm dừng (HOTEL, RESTAURANT, ATTRACTION, COFFEE)")
    time: str = Field(..., description="Thời gian diễn ra (VD: 08:00 AM)")
    description: str = Field(..., description="Mô tả chi tiết hoạt động tại điểm dừng")

class DailyPlan(BaseModel):
    day: int = Field(..., description="Thứ tự ngày trong hành trình")
    nodes: List[ItineraryNode] = Field(..., description="Danh sách các điểm dừng trong ngày")

class TourRequest(BaseModel):
    prompt: str = Field(..., description="Câu lệnh yêu cầu từ người dùng")

class TourResponse(BaseModel):
    title: str = Field(..., description="Tiêu đề hấp dẫn cho chuyến đi")
    estimated_cost_per_person: str = Field(..., description="Ước tính chi phí trên mỗi hành khách")
    itinerary: List[DailyPlan] = Field(..., description="Lịch trình chi tiết từng ngày")

# ==========================================
# SCHEMAS CHO CORE BACKEND (LOCATION CRM)
# ==========================================

class LocationBase(BaseModel):
    name: str = Field(..., description="Tên địa điểm")
    type: str = Field(..., description="Loại địa điểm (HOTEL, RESTAURANT, v.v.)")
    address: Optional[str] = Field(None, description="Địa chỉ chi tiết")
    base_cost: float = Field(0.0, description="Chi phí cơ bản dự kiến")
    rating: float = Field(0.0, description="Đánh giá chất lượng (0-5)")

class LocationCreate(LocationBase):
    longitude: float = Field(..., description="Kinh độ")
    latitude: float = Field(..., description="Vĩ độ")

class LocationRead(LocationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True # Cho phép chuyển đổi từ SQLAlchemy model sang Pydantic

# ==========================================
# SCHEMAS CHO CRM PIPELINE
# ==========================================

class LeadUpdate(BaseModel):
    status: str
    ai_win_probability: Optional[int] = None