from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Tour(Base):
    __tablename__ = "tours"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    estimated_cost = Column(String(100))
    status = Column(String(50), default="DRAFT") # DRAFT, PUBLISHED, ARCHIVED
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Quan hệ 1-N với TourDay
    days = relationship("TourDay", back_populates="tour", cascade="all, delete-orphan")


class TourDay(Base):
    __tablename__ = "tour_days"

    id = Column(Integer, primary_key=True, index=True)
    tour_id = Column(Integer, ForeignKey("tours.id", ondelete="CASCADE"), nullable=False)
    day_number = Column(Integer, nullable=False)

    tour = relationship("Tour", back_populates="days")
    nodes = relationship("TourNode", back_populates="day", cascade="all, delete-orphan")


class TourNode(Base):
    __tablename__ = "tour_nodes"

    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("tour_days.id", ondelete="CASCADE"), nullable=False)
    
    title = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False) # HOTEL, RESTAURANT, ATTRACTION
    time = Column(String(50))
    description = Column(Text)
    
    # Lưu tọa độ để vẽ lên bản đồ (Float cho nhẹ, vì ta không cần query bán kính trên lộ trình có sẵn)
    longitude = Column(Float, nullable=True)
    latitude = Column(Float, nullable=True)

    day = relationship("TourDay", back_populates="nodes")