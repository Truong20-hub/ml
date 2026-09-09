# AGENTS.md

## Mục tiêu

Dự án này xây dựng một gateway machine learning kết nối máy local với AI server chạy trên Colab qua Ngrok.

## Cấu trúc chính

- `app/`: code API và cấu hình
- `colab/`: notebook dùng để train và evaluate model
- `models/`: lưu model đã train
- `tests/`: kiểm thử API và model
- `Dockerfile` và `docker-compose.yml`: chạy backend bằng Docker

## Quy tắc làm việc

1. Khởi động API bằng FastAPI.
2. Dùng `.env` để lưu biến môi trường.
3. Giữ API sạch, dễ test, dễ mở rộng.
4. Khi cần chạy thử, ưu tiên `uvicorn app.main:app --reload`.
5. Khi cần chạy bằng Docker, ưu tiên `docker-compose up --build`.
