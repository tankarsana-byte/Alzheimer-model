"""
Speech Model Predictor for NeuroSense AI.
"""
import numpy as np
import joblib
from typing import Dict
from backend.speech.feature_extractor import extract_features, get_feature_breakdown, get_audio_metadata


def predict_from_audio(audio_path: str, model_path: str = "models/speech_xgb.pkl") -> Dict:
    """
    Run speech model prediction from an audio file.

    Args:
        audio_path: Path to .wav file.
        model_path: Path to the trained XGBoost model.

    Returns:
        Dictionary with probability, prediction, and metadata.
    """
    model = joblib.load(model_path)
    features = extract_features(audio_path)
    features_reshaped = features.reshape(1, -1)

    prob = model.predict_proba(features_reshaped)[0][1]
    pred = model.predict(features_reshaped)[0]
    label = "Alzheimer's Positive" if pred == 1 else "Healthy"

    metadata = get_audio_metadata(audio_path)
    breakdown = get_feature_breakdown(audio_path)

    return {
        "probability": float(prob),
        "prediction": int(pred),
        "label": label,
        "features": features,
        "breakdown": breakdown,
        "metadata": metadata,
    }
