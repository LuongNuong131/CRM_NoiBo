import os
import random
import time
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from google.api_core.exceptions import ResourceExhausted, TooManyRequests, NotFound
from app.models.schemas import TourResponse

load_dotenv()

class AITourGenerator:
    def __init__(self):
        # Lấy danh sách 20 keys từ file .env
        keys_string = os.getenv("GOOGLE_API_KEYS", "")
        self.api_keys = [k.strip() for k in keys_string.split(',') if k.strip()]
        
        if not self.api_keys:
            raise ValueError("Không tìm thấy GOOGLE_API_KEYS trong file .env!")
            
        self.parser = PydanticOutputParser(pydantic_object=TourResponse)
        
        # DANH SÁCH MODEL FALLBACK ĐÃ ĐƯỢC FIX CHUẨN
        # Lưu ý: Mã API có thể khác tên hiển thị. Nếu lỗi 404, thử thêm "models/" ở trước.
        self.models_fallback = [
            "gemini-2.5-flash",         # Top 1: Cân bằng tốt nhất giữa tốc độ và độ thông minh
            "gemini-2.5-flash-lite",    # Top 2: Tốc độ cực nhanh, quota cao
            "gemini-2-flash",           # Top 3: Ổn định
            "gemini-pro"                # Top 4: Model dự phòng huyền thoại, key nào cũng chạy được
        ]
        
        # Random một key bất kỳ để bắt đầu (tránh dồn tải vào key đầu tiên)
        self.current_key_index = random.randint(0, len(self.api_keys) - 1)

    def _get_llm(self, key: str, model_name: str):
        """Khởi tạo LLM với Key và Model cụ thể"""
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0.7,
            google_api_key=key,
            max_retries=0 # Tắt retry mặc định, để mình tự điều khiển luồng
        )

    def generate_itinerary(self, user_prompt: str) -> TourResponse:
        prompt_template = PromptTemplate(
            template="""You are an elite, world-class travel agent and tour designer.
            Based on the user's request, generate a highly optimized, logical, and attractive travel itinerary.
            Ensure the route makes geographic sense and balances activities, meals, and rest.
            
            User Request: {query}
            
            Format the output strictly according to the following instructions. Do not include markdown code blocks like ```json in the output, just raw JSON:
            {format_instructions}
            """,
            input_variables=["query"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()}
        )

        _input = prompt_template.format_prompt(query=user_prompt)
        
        # ==========================================
        # THUẬT TOÁN FALLBACK 2 CHIỀU (MODEL & KEY)
        # ==========================================
        
        # Vòng lặp 1: Duyệt qua từng Model (Từ xịn -> thấp)
        for model_name in self.models_fallback:
            print(f"\n🔄 Đang kích hoạt Model: {model_name}...")
            
            # Vòng lặp 2: Thử tối đa số lượng Key đang có cho Model này
            for attempt in range(len(self.api_keys)):
                current_key = self.api_keys[self.current_key_index]
                
                try:
                    llm = self._get_llm(current_key, model_name)
                    print(f" ├── 🚀 Chạy Prompt (Key Index {self.current_key_index})")
                    
                    # Gọi AI
                    output = llm.invoke(_input.to_string())
                    
                    # Parse dữ liệu
                    parsed_result = self.parser.parse(output.content)
                    print(f" └── ✅ Thành công mỹ mãn với {model_name}!")
                    return parsed_result
                    
                except (ResourceExhausted, TooManyRequests) as e:
                    print(f" ├── ⚠️ Key {self.current_key_index} cạn Token/RPM. Xoay Key...")
                    self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
                    time.sleep(1) # Nghỉ nhịp chống spam
                    
                except NotFound as e:
                    print(f" ├── ⚠️ Key {self.current_key_index} không hỗ trợ model {model_name}. Xoay Key...")
                    self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
                    
                except Exception as e:
                    error_msg = str(e).lower()
                    if "429" in error_msg or "404" in error_msg or "quota" in error_msg:
                        print(f" ├── ⚠️ Phát hiện Rate Limit/Not Found. Xoay Key...")
                        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
                        time.sleep(1)
                    else:
                        print(f" └── ❌ Lỗi không xác định: {str(e)}")
                        raise e
            
            # Nếu chạy hết vòng lặp Key mà vẫn thất bại -> Hạ cấp Model
            print(f"📉 Toàn bộ {len(self.api_keys)} Keys đều kiệt sức hoặc không hỗ trợ {model_name}. Tiến hành hạ cấp Model...")

        # Nếu tèo cả 4 models và 20 keys (Siêu hiếm)
        raise Exception("🚨 BÁO ĐỘNG ĐỎ: Toàn bộ Hệ sinh thái Keys và Models đều đã cạn kiệt! Vui lòng thử lại sau.")