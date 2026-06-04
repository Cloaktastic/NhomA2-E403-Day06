# GrabFood AI Balanced Diet - Prototype (Day 06)

Đây là mã nguồn Prototype cho tính năng **Trợ lý Dinh Dưỡng AI** tích hợp trên ứng dụng GrabFood, được xây dựng cho buổi Hackathon Day 06.

## 🚀 Hướng dẫn cài đặt và chạy (Local)

Để trải nghiệm giao diện Trang chủ GrabFood và tính năng Chatbot AI (Mockup 4 luồng lõi), vui lòng làm theo các bước sau:

**Bước 1: Di chuyển vào thư mục dự án**
Mở Terminal / Command Prompt và chạy:
```cmd
cd codebase
```

**Bước 2: Khởi tạo và kích hoạt môi trường ảo (Virtual Environment)**
```cmd
python -m venv .venv
```
Kích hoạt môi trường:
- **Windows (PowerShell):** `.\.venv\Scripts\activate`
- **Windows (CMD):** `.venv\Scripts\activate.bat`

**Bước 3: Cài đặt thư viện**
```cmd
pip install fastapi uvicorn pydantic langchain langgraph langchain-google-genai
```

**Bước 4: Khởi chạy Server**
```cmd
python src/app.py
```
Sau khi Terminal báo Server đã chạy, mở trình duyệt và truy cập: 👉 **[http://localhost:8000](http://localhost:8000)**

---