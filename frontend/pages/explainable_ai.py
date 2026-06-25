"""Explainable AI page."""
import streamlit as st
import numpy as np
from frontend.components.cards import section_title
from frontend.charts.plots import feature_importance_chart


def render() -> None:
    st.title("🔬 Explainable AI")
    st.caption("Feature importance and interpretability for both models.")
    st.divider()

    tab1, tab2 = st.tabs(["🎤 Speech Model", "✍️ Handwriting Model"])

    with tab1:
        section_title("Speech Feature Importance")
        try:
            import joblib
            model = joblib.load("models/speech_xgb.pkl")
            importances = model.feature_importances_
            feature_names = (
                [f"mfcc_{i+1}" for i in range(13)]
                + [f"chroma_{i+1}" for i in range(12)]
                + [f"mel_{i+1}" for i in range(40)]
            )
            fig = feature_importance_chart(importances, feature_names, "Top 20 Speech Features")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load speech model: {e}")

        section_title("Feature Groups")
        st.markdown("""
        | Group | Features | Role |
        |---|---|---|
        | MFCC | 13 | Vocal tract shape & articulation |
        | Chroma | 12 | Pitch & harmonic content |
        | Mel Spectrogram | 40 | Overall spectral energy |
        """)

    with tab2:
        section_title("Handwriting Feature Importance")
        try:
            import joblib
            model = joblib.load("models/handwriting_xgb.pkl")
            selector = joblib.load("models/feature_selector.pkl")
            importances = model.feature_importances_
            n_features = len(importances)
            feature_names = [f"hw_feat_{i+1}" for i in range(n_features)]
            fig = feature_importance_chart(importances, feature_names, "Top 20 Handwriting Features (post-selection)")
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load handwriting model: {e}")

        section_title("SelectKBest Summary")
        st.markdown("""
        | Step | Detail |
        |---|---|
        | Original Features | 451 handwriting biomechanical features |
        | Selection Method | SelectKBest with ANOVA F-score |
        | Selected Features | Top 100 |
        | Classifier | XGBoost (n_estimators=500, max_depth=6) |
        """)

    st.divider()
    section_title("SHAP Integration")
    st.info(
        "🔮 SHAP (SHapley Additive exPlanations) integration is available. "
        "Install `shap` and load the models to generate waterfall plots and beeswarm charts. "
        "This requires the `shap` package in requirements.txt."
    )
    st.code("""
import shap, joblib, numpy as np

model = joblib.load("models/speech_xgb.pkl")
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test)
    """, language="python")
