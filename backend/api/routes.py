from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.risk_engine import InjuryRiskModel

router = APIRouter()
model = InjuryRiskModel()

class AthleteData(BaseModel):
    athlete_id: str
    weekly_load: float
    sleep_quality: float
    stress_level: float
    asymmetry_score: float
    four_week_avg: float

@router.post("/predict-risk")
async def predict_risk(data: AthleteData):
    try:
        features = {
            "weekly_load": data.weekly_load,
            "4wk_avg_load": data.four_week_avg,
            "asymmetry_score": data.asymmetry_score,
            "sleep_quality": data.sleep_quality,
            "stress_level": data.stress_level
        }
        risk_score = model.predict(features)
        return {"athlete_id": data.athlete_id, "risk_score": risk_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))