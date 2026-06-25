"""Multimodal Fusion page."""
import streamlit as st
from frontend.components.cards import section_title, prediction_banner
from frontend.charts.plots import gauge_chart, fusion_comparison_chart


def render() -> None:
    st.title("🔀 Multimodal Fusion")
    st.caption("Combined speech + handwriting prediction using weighted fusion.")
    st.divider()

    speech_res = st.session_state.get("speech_result")
    hand_res = st.session_state.get("handwriting_result")

    col1, col2 = st.columns(2)
    with col1:
        section_title("Speech Model")
        if speech_res:
            st.success(f"✅ Probability: **{speech_res['probability']*100:.2f}%**")
            st.caption(f"Prediction: {speech_res['label']}")
        else:
            st.warning("⚠️ No speech result yet. Run Speech Analysis first.")

    with col2:
        section_title("Handwriting Model")
        if hand_res:
            st.success(f"✅ Probability: **{hand_res['probability']*100:.2f}%**")
            st.caption(f"Prediction: {hand_res['label']}")
        else:
            st.warning("⚠️ No handwriting result yet. Run Handwriting Analysis first.")

    st.divider()

    # Allow manual override
    with st.expander("⚙️ Manual Probability Override (for demo)"):
        sp_manual = st.slider("Speech Probability", 0.0, 1.0, speech_res["probability"] if speech_res else 0.5, 0.01)
        hw_manual = st.slider("Handwriting Probability", 0.0, 1.0, hand_res["probability"] if hand_res else 0.5, 0.01)

    sp = speech_res["probability"] if speech_res else sp_manual
    hw = hand_res["probability"] if hand_res else hw_manual

    if st.button("⚡ Run Fusion Analysis", type="primary", use_container_width=True):
        from backend.fusion.fusion import fuse_predictions
        result = fuse_predictions(sp, hw)
        st.session_state["fusion_result"] = result

    fusion = st.session_state.get("fusion_result")
    if not fusion:
        return

    st.divider()
    section_title("Fusion Result")
    prediction_banner(
        fusion["prediction"],
        fusion["final_prob"],
        fusion["risk_level"],
        fusion["risk_color"],
    )

    st.divider()
    section_title("Fusion Formula")
    st.code(
        "final_prob = 0.6 × speech_prob + 0.4 × handwriting_prob\n"
        f"           = 0.6 × {fusion['speech_prob']:.4f} + 0.4 × {fusion['handwriting_prob']:.4f}\n"
        f"           = {fusion['final_prob']:.4f}  →  {fusion['confidence_pct']}%",
        language="python",
    )

    col_g, col_c = st.columns([1, 1])
    with col_g:
        st.plotly_chart(gauge_chart(fusion["final_prob"], "Overall Risk Score"), use_container_width=True)
    with col_c:
        st.plotly_chart(fusion_comparison_chart(fusion["speech_prob"], fusion["handwriting_prob"], fusion["final_prob"]), use_container_width=True)

    st.divider()
    section_title("Doctor-Friendly Summary")
    risk_icon = "🔴" if fusion["final_prob"] >= 0.5 else "🟢"
    st.markdown(f"""
    > {risk_icon} The NeuroSense AI system analysed the patient's **speech** and **handwriting** data 
    > and computed a combined Alzheimer's risk score of **{fusion['confidence_pct']}%**.
    > 
    > Based on this multimodal assessment, the patient is classified as: **{fusion['prediction']}** 
    > ({fusion['risk_level']}).
    > 
    > *This is a screening aid — please consult a qualified neurologist for clinical diagnosis.*
    """)

    # Save to session history
    patient = st.session_state.get("current_patient", {})
    from datetime import datetime
    history_entry = {
        **patient,
        "speech_prob": fusion["speech_prob"],
        "handwriting_prob": fusion["handwriting_prob"],
        "final_prob": fusion["final_prob"],
        "prediction": fusion["prediction"],
        "risk_level": fusion["risk_level"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    history = st.session_state.get("screening_history", [])
    if not any(h.get("timestamp") == history_entry["timestamp"] for h in history):
        history.append(history_entry)
        st.session_state["screening_history"] = history
