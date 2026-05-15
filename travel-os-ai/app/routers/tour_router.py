from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tour import Tour, TourDay, TourNode
from app.models.schemas import TourResponse # Schema AI đã tạo ở bài trước
from typing import List

router = APIRouter(prefix="/api/v1/tours", tags=["Tours Management"])

@router.post("/save", status_code=status.HTTP_201_CREATED)
def save_tour_from_ai(tour_data: TourResponse, db: Session = Depends(get_db)):
    """
    Lưu toàn bộ lịch trình Tour (do AI hoặc User làm thủ công) vào Database
    """
    try:
        # 1. Tạo Tour cha
        new_tour = Tour(
            title=tour_data.title,
            estimated_cost=tour_data.estimated_cost_per_person,
            status="DRAFT"
        )
        db.add(new_tour)
        db.flush() # Lấy ID của Tour ngay lập tức mà chưa cần commit

        # 2. Tạo từng Ngày và Điểm dừng
        for day_plan in tour_data.itinerary:
            new_day = TourDay(tour_id=new_tour.id, day_number=day_plan.day)
            db.add(new_day)
            db.flush()

            for node in day_plan.nodes:
                new_node = TourNode(
                    day_id=new_day.id,
                    title=node.title,
                    type=node.type,
                    time=node.time,
                    description=node.description,
                    longitude=node.coordinates[0] if hasattr(node, 'coordinates') and node.coordinates else None,
                    latitude=node.coordinates[1] if hasattr(node, 'coordinates') and node.coordinates else None
                )
                db.add(new_node)

        # 3. Chốt giao dịch (Commit transaction)
        db.commit()
        db.refresh(new_tour)
        return {"message": "Đã lưu Tour thành công!", "tour_id": new_tour.id}
        
    except Exception as e:
        db.rollback() # Nếu lỗi, hủy toàn bộ thao tác để bảo toàn dữ liệu
        raise HTTPException(status_code=500, detail=f"Lỗi khi lưu Tour: {str(e)}")

@router.get("/")
def get_all_tours(db: Session = Depends(get_db)):
    """Lấy danh sách các Tour hiện có trong hệ thống"""
    tours = db.query(Tour).order_by(Tour.created_at.desc()).all()
    return tours