from typing import Dict


def fuse_predictions(speech_prob: float, handwriting_prob: float) -> Dict:
  
    final_prob = 0.6 * speech_prob + 0.4 * handwriting_prob

    if final_prob >= 0.5:
        prediction = "Alzheimer's Positive"
        predicted_class = 1
    else:
        prediction = "Healthy"
        predicted_class = 0

    if final_prob >= 0.75:
        risk_level = "High Risk"
        risk_color = "#DC2626"
    elif final_prob >= 0.5:
        risk_level = "Moderate Risk"
        risk_color = "#F59E0B"
    elif final_prob >= 0.25:
        risk_level = "Low Risk"
        risk_color = "#14B8A6"
    else:
        risk_level = "Very Low Risk"
        risk_color = "#22C55E"

    return {
        "speech_prob": speech_prob,
        "handwriting_prob": handwriting_prob,
        "final_prob": final_prob,
        "prediction": prediction,
        "predicted_class": predicted_class,
        "risk_level": risk_level,
        "risk_color": risk_color,
        "confidence_pct": round(final_prob * 100, 2),
    }
