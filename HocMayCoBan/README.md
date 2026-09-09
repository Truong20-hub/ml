# HocMayCoBan

Dự án này mô phỏng một Machine Learning Gateway kết nối máy local với AI Server chạy trên Colab qua Ngrok.

## Cấu trúc dự án

```text
HocMayCoBan/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── schemas.py
│   └── config.py
│
├── colab/
│   ├── train_model.ipynb
│   └── evaluate_model.ipynb
│
├── models/
│   └── model.pkl
│
├── tests/
│   ├── test_api.py
│   └── test_model.py
│
├── venv/                         # Local development, không đưa vào Docker
│
├── .env
├── .env.example
├── .gitignore
│
├── requirements.txt              # Dependencies production
├── requirements-dev.txt          # Dependencies development/test
├── pyproject.toml
│
├── Dockerfile                    # ⭐ Build image backend
├── docker-compose.yml             # ⭐ Chạy backend bằng Docker
├── .dockerignore                  # ⭐ Loại file không cần copy
│
├── AGENTS.md
└── README.md
```

## Cài đặt

```bash
cd HocMayCoBan
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Chạy API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Test API

```bash
curl -X POST http://localhost:8000/get_prices \
  -H "Content-Type: application/json" \
  -d '{"area": 120.5, "rooms": 3, "distance": 2.4}'
```

## Biến môi trường

File `.env` chứa:

```env
SERVER_URL=https://your-ngrok-url.ngrok-free.app
PREDICT_PATH=/predict
TIMEOUT=30
PORT=8000
```
