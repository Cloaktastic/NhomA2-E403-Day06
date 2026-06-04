from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn
from pydantic import BaseModel
from datetime import datetime

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
    last_bot_message: str = ""

# Serve the index.html on root
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = Path(__file__).parent / "index.html"
    return index_path.read_text(encoding="utf-8")

# Handle chat logic
@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    # Determine current time of day
    current_hour = datetime.now().hour
    if 5 <= current_hour < 11:
        session = "Sáng"
    elif 11 <= current_hour < 14:
        session = "Trưa"
    elif 14 <= current_hour < 18:
        session = "Chiều"
    else:
        session = "Tối"

    # Dựa vào path type từ frontend để xử lý
    path_type = req.path
    last_bot_message = req.last_bot_message
    
    if path_type == "greeting":
        reply = f"👋 Chào bạn! Buổi {session} rồi, bạn muốn ăn gì?"
    else:
        # Nếu là luồng custom (tin nhắn tự do của user), gọi LLM thực tế
        try:
            from core.llm import LLMProvider
            import json
            
            # Đọc toàn bộ file json trong folder data
            menu_context = []
            data_dir = Path(__file__).parent.parent / "data"
            if data_dir.exists():
                for filepath in data_dir.glob("*.json"):
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            stores = data if isinstance(data, list) else [data]
                            for store in stores:
                                store_name = store.get("name", "")
                                for item in store.get("menu", []):
                                    item_name = item.get("name", "")
                                    calories = item.get("calories", "")
                                    price = item.get("price", 0)
                                    price_str = f"{price:,}".replace(",", ".") + "đ"
                                    img_url = item.get("image_url", "")
                                    menu_context.append(f"- Quán: {store_name} | Món: {item_name} ({price_str}) ({calories} kcal) | Ảnh: {img_url}")
                    except Exception:
                        pass
            
            menu_text = "\n".join(menu_context) if menu_context else "Hiện chưa có dữ liệu menu."

            llm = LLMProvider()
            
            system_prompt = f"""
            Bạn là GrabBot - Trợ lý Dinh Dưỡng thông minh của GrabFood. Bây giờ đang là buổi {session}.
            
            LỊCH SỬ HỘI THOẠI NGẮN (Câu nói gần nhất của bạn):
            "{last_bot_message}"
            
            📋 DANH SÁCH MENU CÁC QUÁN HIỆN CÓ TRONG HỆ THỐNG (kèm link Ảnh và Giá tiền):
            {menu_text}
            
            RULE QUAN TRỌNG:
            1. KHÔNG BAO GIỜ chào dài dòng kiểu robot ("Xin chào quý khách...").
            2. Nếu user CHỈ CÓ ý chào hỏi (VD: "Chào", "Hello") và KHÔNG HỀ yêu cầu gợi ý món, thì MỚI phản hồi ngắn gọn: "👋 Chào bạn! Buổi {session} rồi, bạn muốn ăn gì? Mình có thể gợi ý theo Giá cả, Khẩu vị, hoặc Chế độ ăn..."
            3. NẾU USER GÕ LINH TINH, VÔ NGHĨA (VD: "nkjgknfk", "asdasd"), HOẶC HỎI NHỮNG KIẾN THỨC BÊN NGOÀI (VD: Bạn là AI à, Lịch sử, khoa học, toán học, tin tức...), HÃY TRẢ LỜI LÀ BẠN KHÔNG HIỂU VÀ HỎI LẠI XEM HỌ MUỐN ĂN GÌ. (Ví dụ: "Xin lỗi, mình chưa hiểu ý bạn lắm. Bạn đang thèm món gì để mình tìm giúp nhé?"). TUYỆT ĐỐI KHÔNG lặp lại câu chào mặc định.
            4. NẾU USER HỎI QUÁ CHUNG CHUNG VÀ HOÀN TOÀN CHƯA CÓ TIÊU CHÍ GÌ (VD: "Không biết ăn gì", "Gợi ý bừa đi", "Ăn gì ngon"): BẠN MỚI ĐẶT CÂU HỎI LẠI để thu hẹp phạm vi. Trả lời bằng TEXT thường, không dùng HTML.
            5. NẾU USER ĐÃ ĐƯA RA BẤT KỲ TIÊU CHÍ NÀO DÙ LÀ NHỎ NHẤT (VD: "Tìm món rẻ", "Dưới 50k", "Tìm món keto", "Thèm thịt"): BẠN BẮT BUỘC PHẢI GỢI Ý MÓN. Bạn phải tuân thủ THUẬT TOÁN TÌM MÓN sau đây:
               - Bước 1: Lọc ra các món khớp với từ khóa (ví dụ: "thịt bò").
               - Bước 2: KIỂM TRA NGÂN SÁCH (TOÁN HỌC STRICT): Nếu user có nhắc đến ngân sách (VD: "91k", "dưới 50k"), bạn PHẢI CHUYỂN ĐỔI sang số (91k = 91.000đ). BẠN BẮT BUỘC phải so sánh số tiền này với GIÁ TIỀN của món ăn. Ví dụ: Nếu ngân sách là 91.000đ, món 150.000đ là đắt hơn -> LẬP TỨC LOẠI BỎ. Bạn CHỈ ĐƯỢC GIỮ LẠI món có giá <= Ngân sách.
               - Bước 3: NẾU KHÔNG CÒN MÓN NÀO THỎA MÃN (ví dụ tìm bò dưới 91k nhưng các món bò toàn > 91k): BẠN KHÔNG ĐƯỢC PHÉP IN RA THẺ HTML. Bạn chỉ được phép trả lời bằng TEXT để xin lỗi, nói rõ lý do (VD: "Xin lỗi, các món thịt bò hiện tại đều có giá từ 120k trở lên, vượt quá ngân sách 91k của bạn. Mình gợi ý món Bánh Mì Bò Né (45k) nhé?").
               - Bước 4: NẾU TÌM ĐƯỢC MÓN THỎA MÃN: Bắt buộc chọn đúng 2 món từ 2 quán khác nhau để in ra theo mẫu HTML div class="combo-card" bên dưới.
            7. NẾU USER ĐÁP LẠI BẰNG BẤT KỲ CÂU NÀO THỂ HIỆN SỰ ĐỒNG Ý CHỌN MÓN (VD: "ok", "oke", "chốt", "được", "chọn món đó đi"): HÃY ĐỌC "LỊCH SỬ HỘI THOẠI". Nếu trước đó bạn CHỈ MỚI ĐỀ XUẤT bằng CHỮ (VD: "Mình gợi ý món Bánh Mì nhé?"), thì HÃY TÌM CHÍNH XÁC MÓN ĐÓ VÀ IN RA LẠI BLOCK HTML `combo-card`. NHƯNG, nếu trước đó bạn ĐÃ HIỂN THỊ THẺ MÓN ĂN RỒI (họ đồng ý mua món trên thẻ), thì BẠN CHỈ ĐƯỢC PHÉP TRẢ LỜI BẰNG TEXT, TUYỆT ĐỐI KHÔNG IN RA HTML NỮA. Hãy nói: "Tuyệt vời! Bạn vui lòng bấm nút 'Đến quán ngay' màu xanh ở phía trên để đặt hàng nhé. Chúc bạn ngon miệng!".
            8. NẾU USER ĐÁP LẠI BẰNG BẤT KỲ CÂU NÀO THỂ HIỆN Ý MUỐN TÌM THÊM/ĐỔI MÓN (VD: "có", "thêm đi", "món khác", "đổi món", "chưa ưng"): HÃY ĐỌC LỊCH SỬ HỘI THOẠI, nếu bạn vừa hỏi "Có muốn xem món khác không?", thì hãy QUÉT LẠI MENU, chọn 2 MÓN HOÀN TOÀN MỚI khác với món cũ và in ra HTML `combo-card`. Câu mở đầu ví dụ: "Dạ vâng, mình có 2 món mới cực kỳ hấp dẫn để bạn đổi vị đây:".
            Bạn phải xem xét việc bây giờ là buổi {session} để chọn món cho hợp lý. BẠN PHẢI MỞ ĐẦU BẰNG 1-2 CÂU GIAO TIẾP "VĂN VỞ", TỰ NHIÊN. LƯU Ý QUAN TRỌNG: LUÔN THAY ĐỔI VÀ ĐA DẠNG HÓA CÁCH DIỄN ĐẠT TRONG PHẦN "VĂN VỞ" NÀY MỖI LẦN TRẢ LỜI. SAU ĐÓ BẮT BUỘC Trả về phần thẻ món ăn dưới dạng HTML div class="combo-card" NHƯ MẪU SAU (NẾU CÓ MÓN THỎA MÃN).
            LƯU Ý: Phần "Phân tích" BẮT BUỘC PHẢI RẤT NGẮN GỌN (TỐI ĐA 1 CÂU). AI tự dùng kiến thức dinh dưỡng để phân tích điểm nổi bật nhất của món ăn, tuyệt đối không viết dài dòng lê thê. Đừng quên điền đúng [URL ẢNH CỦA MÓN ĐÓ] và [GIÁ TIỀN] lấy từ menu.
            
            [1-2 CÂU GIAO TIẾP VĂN VỞ CỦA BẠN TẠI ĐÂY]<br><br>
            <div class="combo-card">
                <img src="[URL ẢNH CỦA MÓN TỪ QUÁN 1]" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <b>🥗 [TÊN MÓN ĂN TỪ QUÁN 1]</b>
                    <b style="color: #FF5E1F; font-size: 15px; white-space: nowrap;">[GIÁ TIỀN]</b>
                </div>
                <i>Quán: [TÊN QUÁN 1 TRONG MENU]</i><br>
                <div style="color: #444; font-size: 13px; margin-top: 8px;">
                    📝 <b>Phân tích:</b> <i>[1 CÂU phân tích CỰC KỲ NGẮN GỌN]</i>
                </div>
                <button style="width: 100%; padding: 8px; margin-top: 10px; background: #00B14F; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Đến quán ngay</button>
            </div>
            
            <div class="combo-card">
                <img src="[URL ẢNH CỦA MÓN TỪ QUÁN 2]" style="width: 100%; height: 150px; object-fit: cover; border-radius: 8px; margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <b>🍲 [TÊN MÓN ĂN TỪ QUÁN 2 (PHẢI KHÁC QUÁN 1)]</b>
                    <b style="color: #FF5E1F; font-size: 15px; white-space: nowrap;">[GIÁ TIỀN]</b>
                </div>
                <i>Quán: [TÊN QUÁN 2 TRONG MENU]</i><br>
                <div style="color: #444; font-size: 13px; margin-top: 8px;">
                    📝 <b>Phân tích:</b> <i>[1 CÂU phân tích CỰC KỲ NGẮN GỌN]</i>
                </div>
                <button style="width: 100%; padding: 8px; margin-top: 10px; background: #00B14F; color: white; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">Đến quán ngay</button>
            </div>
            """
            
            llm_reply = llm.generate(prompt=req.message, system_prompt=system_prompt)
            # Dọn dẹp markdown code blocks nếu model vô tình sinh ra
            if llm_reply.startswith("```html"):
                llm_reply = llm_reply.strip("```html").strip("```").strip()
            
            reply = llm_reply
        except Exception as e:
            reply = f"""
            <div class="combo-card">
                <b style="color:red;">Lỗi kết nối tới AI Model:</b><br>
                {str(e)}
            </div>
            """
        
    return JSONResponse(content={"reply_html": reply})

if __name__ == "__main__":
    print("🚀 Starting AI Diet Agent Mockup Server...")
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
