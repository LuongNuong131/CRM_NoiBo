from sqlalchemy import Column, Integer, String, Float, DateTime, Numeric
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
from app.database import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False) # HOTEL, RESTAURANT, ATTRACTION
    address = Column(String(500))
    # Lưu tọa độ chuẩn GPS (SRID 4326)
    coordinates = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    base_cost = Column(Numeric(15, 2), default=0.00)
    rating = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())