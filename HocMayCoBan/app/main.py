from fastapi import FastAPI
from app.schemas import PropertyData
from app.config import settings

app = FastAPI(title="Machine Learning Gateway")


@app.get("/")
def read_root():
    return {"message": "Machine Learning Gateway is running"}


@app.post("/get_prices")
def get_prices(payload: PropertyData):
    # Placeholder logic for ML prediction gateway
    predicted_price = payload.area * 1200 + payload.rooms * 25000 - payload.distance * 5000
    return {
        "predicted_price": round(predicted_price, 2),
        "currency": "USD",
        "input_data": payload.model_dump(),
        "status": "success",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=settings.PORT, reload=True)
