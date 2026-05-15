import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
# Lấy key đầu tiên để test
first_key = os.getenv("GOOGLE_API_KEYS").split(',')[0].strip()
genai.configure(api_key=first_key)

print("Danh sách Model thực tế API hỗ trợ:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        # Bạn copy cái m.name (bỏ chữ models/ đi) và dán vào self.models_fallback
        print(f"- {m.name}")