"""
Lab 6 - FastAPI Inference Service (Jenkins CI/CD)
Wine Quality Prediction API deployed via Jenkins Pipeline
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pickle
import numpy as np
from typing import List
import json
import os

# Initialize FastAPI app
app = FastAPI(
    title="Wine Quality Prediction API - Lab 6",
    description="MLOps Jenkins CI/CD Pipeline for ML Model Deployment",
    version="1.0.0"
)

# Student information - UPDATE THIS
STUDENT_INFO = {
    "name": "Your Name",  # Update with your name
    "roll_no": "2022BCD0026",
    "lab": "Lab 6 - Jenkins CI/CD Pipeline"
}

# Load model and metrics
MODEL_PATH = "model.pkl"
METRICS_PATH = "metrics.json"

try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    print(f"✅ Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None

try:
    with open(METRICS_PATH, 'r') as f:
        metrics = json.load(f)
    print(f"✅ Metrics loaded: {metrics}")
except Exception as e:
    print(f"⚠️ Metrics file not found: {e}")
    metrics = {}


class WineFeatures(BaseModel):
    """Wine chemical features for quality prediction"""
    alcohol: float = Field(..., description="Alcohol content")
    malic_acid: float = Field(..., description="Malic acid")
    ash: float = Field(..., description="Ash content")
    alcalinity_of_ash: float = Field(..., description="Alcalinity of ash")
    magnesium: float = Field(..., description="Magnesium content")
    total_phenols: float = Field(..., description="Total phenols")
    flavanoids: float = Field(..., description="Flavanoids")
    nonflavanoid_phenols: float = Field(..., description="Non-flavanoid phenols")
    proanthocyanins: float = Field(..., description="Proanthocyanins")
    color_intensity: float = Field(..., description="Color intensity")
    hue: float = Field(..., description="Hue")
    od280_od315: float = Field(..., description="OD280/OD315 of diluted wines")
    proline: float = Field(..., description="Proline")

    class Config:
        json_schema_extra = {
            "example": {
                "alcohol": 13.2,
                "malic_acid": 2.77,
                "ash": 2.51,
                "alcalinity_of_ash": 18.5,
                "magnesium": 96.0,
                "total_phenols": 2.45,
                "flavanoids": 2.53,
                "nonflavanoid_phenols": 0.29,
                "proanthocyanins": 1.54,
                "color_intensity": 4.6,
                "hue": 1.04,
                "od280_od315": 2.77,
                "proline": 562.0
            }
        }


class PredictionResponse(BaseModel):
    """Prediction result"""
    quality_class: int
    confidence: float
    student_info: dict
    model_metrics: dict


@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "status": "running",
        "service": "Wine Quality Prediction API",
        "lab": "Lab 6 - Jenkins CI/CD Pipeline",
        "student": STUDENT_INFO,
        "endpoints": {
            "health": "/health",
            "predict": "/predict",
            "metrics": "/metrics",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health():
    """Service health status"""
    model_loaded = model is not None
    return {
        "status": "healthy" if model_loaded else "unhealthy",
        "model_loaded": model_loaded,
        "metrics_available": bool(metrics)
    }


@app.get("/metrics")
async def get_metrics():
    """Get model performance metrics"""
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not available")
    
    return {
        "student": STUDENT_INFO,
        "model_metrics": metrics
    }


@app.post("/predict", response_model=PredictionResponse)
async def predict(features: WineFeatures):
    """Predict wine quality class"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Convert features to array
        feature_array = np.array([[
            features.alcohol,
            features.malic_acid,
            features.ash,
            features.alcalinity_of_ash,
            features.magnesium,
            features.total_phenols,
            features.flavanoids,
            features.nonflavanoid_phenols,
            features.proanthocyanins,
            features.color_intensity,
            features.hue,
            features.od280_od315,
            features.proline
        ]])
        
        # Make prediction
        prediction = model.predict(feature_array)[0]
        probabilities = model.predict_proba(feature_array)[0]
        confidence = float(max(probabilities))
        
        return PredictionResponse(
            quality_class=int(prediction),
            confidence=round(confidence, 4),
            student_info=STUDENT_INFO,
            model_metrics=metrics
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
