def calculate_acwr(weekly_load: float, four_week_avg: float) -> float:
    return weekly_load / four_week_avg if four_week_avg != 0 else 0.0

def classify_risk(acwr: float) -> str:
    if acwr < 0.8:
        return "Low Risk"
    elif 0.8 <= acwr <= 1.3:
        return "Normal Risk"
    elif 1.3 < acwr <= 1.5:
        return "High Risk"
    else:
        return "Very High Risk"