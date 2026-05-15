import os  # <-- Đã thêm dòng này
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.schemas import TourRequest, TourResponse
from app.services.ai_generator import AITourGenerator
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="TravelOS AI Engine",
    description="AI-powered tour generation for Next-Gen Travel OS",
    version="1.0.0"
)

# Cấu hình CORS cho Frontend gọi
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Mở all trong môi trường dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ai_generator = AITourGenerator()

@app.post("/api/v1/ai/generate-tour", response_model=TourResponse)
async def generate_tour(request: TourRequest):
    try:
        # Gọi LangChain Service để sinh lịch trình
        result = ai_generator.generate_itinerary(request.prompt)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "AI Engine is running optimally"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 8000)), reload=True)