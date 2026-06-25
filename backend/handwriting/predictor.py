"""
Handwriting Model Predictor for NeuroSense AI.
"""
import numpy as np
import pandas as pd
import joblib
from typing import Dict, Union


def predict_from_csv_row(
    row: Union[pd.Series, np.ndarray, dict],
    model_path: str = "models/handwriting_xgb.pkl",
    selector_path: str = "models/feature_selector.pkl",
    encoder_path: str = "models/label_encoder.pkl",
) -> Dict:
    """
    Run handwriting model prediction from a feature row.

    Args:
        row: A single row of handwriting features (451 features).
        model_path: Path to trained XGBoost model.
        selector_path: Path to SelectKBest selector.
        encoder_path: Path to LabelEncoder.

    Returns:
        Dictionary with probability, prediction, and feature summary.
    """
    model = joblib.load(model_path)
    selector = joblib.load(selector_path)
    le = joblib.load(encoder_path)

    if isinstance(row, dict):
        row = pd.Series(row)
    if isinstance(row, pd.Series):
        row = row.values

    row = row.reshape(1, -1)
    selected = selector.transform(row)

    prob = model.predict_proba(selected)[0][1]
    pred = model.predict(selected)[0]
    label = le.inverse_transform([pred])[0]
    readable_label = "Alzheimer's Positive" if label == "P" else "Healthy"

    return {
        "probability": float(prob),
        "prediction": int(pred),
        "label": readable_label,
        "raw_label": label,
        "original_features": int(row.shape[1]),
        "selected_features": int(selected.shape[1]),
        "selected_values": selected[0],
    }
