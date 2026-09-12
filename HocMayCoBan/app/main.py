from typing import Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.model import mushroom_model


app = FastAPI(
    title="Mushroom Classification API",
    description="Phân loại nấm ăn được hoặc nấm độc bằng Naive Bayes",
    version="1.0.0"
)


class PredictionRequest(BaseModel):
    features: Dict[str, str]


@app.get("/")
def root():
    return {
        "message": "Mushroom Naive Bayes API đang hoạt động",
        "docs": "/docs",
        "health": "/health",
        "model_info": "/model-info"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "model_trained": mushroom_model.is_trained
    }


@app.get("/model-info")
def model_info():
    return mushroom_model.get_info()


@app.get("/features")
def get_features():
    return {
        "target_column": mushroom_model.target_column,
        "features": mushroom_model.feature_columns
    }


@app.post("/predict")
def predict_mushroom(request: PredictionRequest):
    try:
        result = mushroom_model.predict(request.features)

        return {
            "success": True,
            "data": result
        }

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )