from pydantic import BaseModel

class AthleteBio(BaseModel):
    athlete_id: str
    height_cm: float
    weight_kg: float
    position: str

class BiomechanicalData(BaseModel):
    session_id: str
    left_force: float
    right_force: float
    asymmetry_score: float

class RiskPrediction(BaseModel):
    risk_score: float
    recommendation: str