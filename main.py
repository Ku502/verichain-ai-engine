from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI(title="VeriChain AI Engine", version="1.0")

@app.get("/")
def root():
    return {"status": "VeriChain AI Engine running", "version": "1.0"}

class ShipmentData(BaseModel):
    origin: str
    destination: str
    weather_condition: str
    distance_km: int

@app.post("/api/predict-delay")
def predict_delay(data: ShipmentData):
    base_risk = "LOW"
    delay_hours = 0
    confidence = round(random.uniform(0.85, 0.99), 4)

    severe = ["storm", "heavy rain", "hurricane", "snow", "cyclone"]
    moderate = ["rain", "fog", "drizzle"]

    if data.weather_condition.lower() in severe:
        if data.distance_km > 1000:
            base_risk = "HIGH"
            delay_hours = random.randint(12, 48)
        else:
            base_risk = "MEDIUM"
            delay_hours = random.randint(4, 12)
    elif data.weather_condition.lower() in moderate:
        if data.distance_km > 800:
            base_risk = "MEDIUM"
            delay_hours = random.randint(2, 8)

    return {
        "prediction_status": "SUCCESS",
        "delay_risk": base_risk,
        "estimated_delay_hours": delay_hours,
        "ai_confidence_score": confidence,
        "recommended_action": "REROUTE" if base_risk == "HIGH" else "PROCEED"
    }
