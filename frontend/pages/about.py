"""About page."""
import streamlit as st


def render() -> None:
    st.title("ℹ️ About NeuroSense AI")
    st.divider()
    st.markdown("""
    ## 🧠 NeuroSense AI
    ### Multimodal Explainable Alzheimer's Screening System

    NeuroSense AI is an IEEE research project that combines **speech** and **handwriting** analysis 
    to screen for Alzheimer's Disease using explainable machine learning.

    ---

    ### Architecture
    | Component | Technology |
    |---|---|
    | Speech Model | XGBoost (65 acoustic features) |
    | Handwriting Model | XGBoost + SelectKBest (451 → 100 features) |
    | Fusion | Weighted average (60% speech, 40% handwriting) |
    | Frontend | Streamlit |
    | Explainability | XGBoost Feature Importance + SHAP |

    ---

    ### How It Works
    1. **Patient Screening** — Enter patient details and upload data.
    2. **Speech Analysis** — MFCC, Chroma, and Mel features are extracted from a .wav file and passed to the speech XGBoost model.
    3. **Handwriting Analysis** — 451 biomechanical features are reduced to 100 via SelectKBest (ANOVA F-score) and classified.
    4. **Fusion** — `final_prob = 0.6 × speech_prob + 0.4 × handwriting_prob`
    5. **Report** — A downloadable PDF report is generated.

    ---

    ### Disclaimer
    > This system is designed as a **clinical screening aid** and should not be used as a standalone 
    > diagnostic tool. Always consult a qualified neurologist.

    ---

    **Version:** 1.0.0  
    **Framework:** IEEE Research Project  
    **Stack:** Python · XGBoost · Librosa · Scikit-learn · Streamlit · Plotly
    """)
