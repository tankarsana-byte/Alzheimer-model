"""Dashboard overview page."""
import streamlit as st
import pandas as pd
from datetime import datetime
from frontend.components.cards import metric_card, section_title
from frontend.charts.plots import risk_distribution_pie


def render() -> None:
    st.title("🧠 NeuroSense AI — Dashboard")
    st.caption("Multimodal Explainable Alzheimer's Screening System")
    st.divider()

    history = st.session_state.get("screening_history", [])
    total = len(history)
    high_risk = sum(1 for h in history if h["final_prob"] >= 0.5)
    healthy = total - high_risk
    avg_risk = (sum(h["final_prob"] for h in history) / total * 100) if total else 0.0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Total Screenings", str(total))
    with col2:
        metric_card("High Risk Cases", str(high_risk), "red")
    with col3:
        metric_card("Healthy Cases", str(healthy), "teal")
    with col4:
        metric_card("Avg Risk Score", f"{avg_risk:.1f}%", "slate")

    st.divider()

    col_left, col_right = st.columns([3, 2])

    with col_left:
        section_title("Recent Patients")
        if history:
            rows = []
            for h in reversed(history[-10:]):
                rows.append({
                    "Patient": h.get("name", "N/A"),
                    "Age": h.get("age", "—"),
                    "Gender": h.get("gender", "—"),
                    "Risk Score": f"{h['final_prob']*100:.1f}%",
                    "Prediction": h["prediction"],
                    "Time": h.get("timestamp", "—"),
                })
            st.dataframe(pd.DataFrame(rows), use_container_width=True)
        else:
            st.info("No screenings yet. Go to **Patient Screening** to start.")

    with col_right:
        section_title("Risk Distribution")
        fig = risk_distribution_pie(healthy, high_risk)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        section_title("Model Status")
        st.success("✅ Speech Model (XGBoost) — Ready")
        st.success("✅ Handwriting Model (XGBoost + SelectKBest) — Ready")
        st.success("✅ Fusion Engine — Ready")
    with col_s2:
        section_title("System Info")
        st.markdown("""
        - **Speech Features:** 65 (MFCC × 13, Chroma × 12, Mel × 40)
        - **Handwriting Features:** 451 → 100 selected
        - **Fusion Weights:** Speech 60% · Handwriting 40%
        - **Classifier:** XGBoost (n_estimators=500)
        """)
