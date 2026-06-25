"""
NeuroSense AI — Main Streamlit Application Entry Point
Multimodal Explainable Alzheimer's Screening System
"""
import streamlit as st
from frontend.styles.theme import CUSTOM_CSS

# ── Page config ──
st.set_page_config(
    page_title="NeuroSense AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject global CSS ──
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── Sidebar navigation ──
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;padding:1rem 0 0.5rem;">
            <div style="font-size:2.5rem;">🧠</div>
            <div style="font-size:1.2rem;font-weight:700;color:#E2E8F0;">NeuroSense AI</div>
            <div style="font-size:0.75rem;color:#94A3B8;margin-top:0.2rem;">Alzheimer's Screening</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "👤 Patient Screening",
            "🎤 Speech Analysis",
            "✍️ Handwriting Analysis",
            "🔀 Multimodal Fusion",
            "🔬 Explainable AI",
            "📄 Reports",
            "ℹ️ About",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    patient = st.session_state.get("current_patient")
    if patient:
        st.markdown(
            f"""
            <div style="background:rgba(37,99,235,0.2);border-radius:10px;padding:0.75rem;">
                <div style="font-size:0.7rem;color:#94A3B8;">ACTIVE PATIENT</div>
                <div style="font-weight:600;color:#E2E8F0;">{patient['name']}</div>
                <div style="font-size:0.8rem;color:#94A3B8;">{patient['age']} · {patient['gender']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ── Route pages ──
from frontend.pages import (
    dashboard,
    patient_screening,
    speech_analysis,
    handwriting_analysis,
    fusion_page,
    explainable_ai,
    reports,
    about,
)

routes = {
    "🏠 Dashboard": dashboard,
    "👤 Patient Screening": patient_screening,
    "🎤 Speech Analysis": speech_analysis,
    "✍️ Handwriting Analysis": handwriting_analysis,
    "🔀 Multimodal Fusion": fusion_page,
    "🔬 Explainable AI": explainable_ai,
    "📄 Reports": reports,
    "ℹ️ About": about,
}

routes[page].render()
