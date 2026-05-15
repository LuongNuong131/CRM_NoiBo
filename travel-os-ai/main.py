from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db, engine, Base
from app.models.location import Location
from app.services.ai_generator import AITourGenerator
from app.models.schemas import TourRequest, TourResponse
from geoalchemy2.functions import ST_Distance_Sphere, ST_GeomFromText

# Tự động tạo bảng nếu chưa có
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TravelOS AI Engine & Core")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

generator = AITourGenerator()

@app.post("/api/v1/ai/generate-tour", response_model=TourResponse)
async def generate_tour(request: TourRequest):
    return generator.generate_itinerary(request.prompt)

@app.get("/api/v1/locations/nearby")
def get_nearby(lng: float, lat: float, radius: float = 5000, db: Session = Depends(get_db)):
    """Tìm địa điểm trong bán kính radius (mét) dùng Spatial Query"""
    point = f'POINT({lng} {lat})'
    locations = db.query(Location).filter(
        ST_Distance_Sphere(Location.coordinates, ST_GeomFromText(point, 4326)) <= radius
    ).all()
    return locations

@app.get("/health")
def health_check():
    return {"status": "online", "engine": "FastAPI + Spatial MySQL"}