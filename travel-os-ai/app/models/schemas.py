from pydantic import BaseModel, Field
from typing import List

class TourRequest(BaseModel):
    prompt: str = Field(..., example="Create a 3D2N trip from HCM to Da Lat for 40 people under 4M/person")

class ItineraryNode(BaseModel):
    title: str = Field(description="Tên địa điểm (VD: Thác Prenn)")
    type: str = Field(description="Loại địa điểm: 'attraction', 'restaurant', 'hotel', 'coffee'")
    time: str = Field(description="Thời gian dự kiến (VD: 08:30 AM)")
    description: str = Field(description="Mô tả ngắn gọn hoạt động")

class DailyPlan(BaseModel):
    day: int = Field(description="Ngày thứ mấy")
    nodes: List[ItineraryNode] = Field(description="Danh sách các điểm dừng trong ngày")

class TourResponse(BaseModel):
    title: str = Field(description="Tên tour du lịch do AI đặt")
    estimated_cost_per_person: str = Field(description="Ước tính chi phí một người")
    itinerary: List[DailyPlan] = Field(description="Lịch trình chi tiết từng ngày")