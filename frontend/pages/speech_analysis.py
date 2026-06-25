"""Speech Analysis page."""
import streamlit as st
import numpy as np
import os
from frontend.components.cards import section_title, prediction_banner
from frontend.charts.plots import bar_chart, gauge_chart


def render() -> None:
    st.title("🎤 Speech Analysis")
    st.caption("Alzheimer's detection from audio features (MFCC, Chroma, Mel).")
    st.divider()

    audio_path = st.session_state.get("audio_path")

    if not audio_path:
        st.info("📂 No audio loaded. Please go to **Patient Screening** and upload a .wav file first.")
        uploaded = st.file_uploader("Or upload directly here:", type=["wav"])
        if uploaded:
            os.makedirs("uploads", exist_ok=True)
            audio_path = f"uploads/{uploaded.name}"
            with open(audio_path, "wb") as f:
                f.write(uploaded.getbuffer())
            st.session_state["audio_path"] = audio_path
            st.rerun()
        return

    st.audio(audio_path)

    if st.button("🔍 Run Speech Analysis", type="primary", use_container_width=True):
        with st.spinner("Extracting features and predicting…"):
            try:
                from backend.speech.predictor import predict_from_audio
                result = predict_from_audio(audio_path)
                st.session_state["speech_result"] = result
            except Exception as e:
                st.error(f"Error during speech analysis: {e}")
                return

    result = st.session_state.get("speech_result")
    if not result:
        return

    st.divider()
    section_title("Prediction Result")
    prediction_banner(
        result["label"],
        result["probability"],
        "High Risk" if result["probability"] >= 0.5 else "Low Risk",
        "#DC2626" if result["probability"] >= 0.5 else "#22C55E",
    )

    st.divider()
    section_title("Audio Metadata")
    meta = result["metadata"]
    col1, col2, col3 = st.columns(3)
    col1.metric("Duration", f"{meta['duration_sec']}s")
    col2.metric("Sample Rate", f"{meta['sample_rate']} Hz")
    col3.metric("Samples", f"{meta['num_samples']:,}")

    st.divider()
    section_title("Feature Visualizations")
    breakdown = result["breakdown"]

    tab1, tab2, tab3 = st.tabs(["MFCC (13)", "Chroma (12)", "Mel (40)"])
    with tab1:
        st.plotly_chart(bar_chart(breakdown["mfcc"], "MFCC Coefficients", "Coefficient"), use_container_width=True)
    with tab2:
        st.plotly_chart(bar_chart(breakdown["chroma"], "Chroma Features", "Pitch Class"), use_container_width=True)
    with tab3:
        st.plotly_chart(bar_chart(breakdown["mel"], "Mel Spectrogram Features", "Mel Band"), use_container_width=True)

    st.divider()
    col_g, col_i = st.columns([1, 1])
    with col_g:
        st.plotly_chart(gauge_chart(result["probability"], "Speech Risk Score"), use_container_width=True)
    with col_i:
        section_title("Feature Summary")
        st.markdown(f"""
        | Feature Group | Count |
        |---|---|
        | MFCC | 13 |
        | Chroma | 12 |
        | Mel Spectrogram | 40 |
        | **Total** | **65** |
        """)
