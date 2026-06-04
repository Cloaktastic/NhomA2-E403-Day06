from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn
from pydantic import BaseModel

app = FastAPI(title="GrabFood AI Balanced Diet API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    path: str
    message: str

# Serve the index.html on root
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = Path(__file__).parent / "index.html"
    return index_path.read_text(encoding="utf-8")

# Handle chat logic
@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    # Dựa vào path type từ frontend để trả về mockup phù hợp
    path_type = req.path
    
    if path_type == "happy":
        reply = """
        <b>Đã tìm thấy combo phù hợp cho bạn!</b><br>
        <div class="combo-card">
            <b>🥗 Cơm gà luộc xé + Canh rau cải thịt bằm</b><br>
            <i>Quán: Cơm Gà Healthy 99</i><br>
            <div style="margin-top: 8px;">
                <span class="macro-badge macro-cal">🔥 580 kcal</span>
                <span class="macro-badge macro-pro">🥩 45g Pro</span>
                <span class="macro-badge macro-carb">🍚 50g Carb</span>
                <span class="macro-badge macro-fat">🥑 12g Fat</span>
            </div>
        </div>
        """
    elif path_type == "failure":
        reply = """
        <b>Gợi ý cho chế độ Keto của bạn:</b><br>
        <div class="combo-card">
            <b>🥩 Salad Bò Xốt Mayonnaise</b><br>
            <div style="margin-top: 8px;">
                <span class="macro-badge macro-cal">🔥 450 kcal</span>
            </div>
            <div class="warning-label">⚠️ Chú ý: Nước sốt Mayonnaise/kèm theo có thể chứa đường hoặc bột tinh luyện ẩn. Bạn nên yêu cầu quán để riêng sốt để không phá vỡ chế độ Keto.</div>
        </div>
        """
    elif path_type == "low_conf":
        reply = """
        <b>Món này nguyên liệu hơi đa dạng:</b><br>
        <div class="combo-card">
            <b>🍛 Cơm thập cẩm đặc biệt</b><br>
            <div style="margin-top: 8px;">
                <span class="macro-badge macro-cal">🔥 600 - 900 kcal (Ước tính rộng)</span>
            </div>
            <div style="color: #666; font-size: 12px; margin-top: 5px;">
                💡 <i>Chỉ số mang tính chất tham khảo. Do "thập cẩm" có nhiều loại topping, lượng calo có thể dao động lớn. Khuyên bạn nên chọn món ghi rõ nguyên liệu!</i>
            </div>
        </div>
        """
    elif path_type == "correction":
        reply = """
        <b>Đã cập nhật lại Macros cho bạn:</b><br>
        <div class="combo-card">
            <b>🥗 Gà luộc xé + Canh cải + Rau luộc (Ít cơm)</b><br>
            <div style="margin-top: 8px;">
                <span class="macro-badge macro-cal">🔥 420 kcal <i>(Giảm 160)</i></span>
                <span class="macro-badge macro-pro">🥩 46g Pro</span>
                <span class="macro-badge macro-carb">🍚 20g Carb <i>(Giảm)</i></span>
                <span class="macro-badge macro-fat">🥑 12g Fat</span>
            </div>
        </div>
        """
    else:
        # Custom message logic (fallback for general chatting)
        reply = """
        Dạ, tính năng này đang trong quá trình phát triển với LangGraph AI. 
        Vui lòng sử dụng các nút Demo bên trên để kiểm tra các luồng cơ bản nhé!
        """
        
    return JSONResponse(content={"reply_html": reply})

if __name__ == "__main__":
    print("🚀 Starting AI Diet Agent Mockup Server...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
