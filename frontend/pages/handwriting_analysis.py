"""Handwriting Analysis page."""
import streamlit as st
import pandas as pd
from frontend.components.cards import section_title, prediction_banner
from frontend.charts.plots import bar_chart, gauge_chart


def render() -> None:
    st.title("✍️ Handwriting Analysis")
    st.caption("Alzheimer's detection from handwriting biomechanical features.")
    st.divider()

    hw_df: pd.DataFrame = st.session_state.get("handwriting_df")

    if hw_df is None:
        st.info("📂 No handwriting CSV loaded. Please go to **Patient Screening** first.")
        uploaded = st.file_uploader("Or upload directly here:", type=["csv"])
        if uploaded:
            hw_df = pd.read_csv(uploaded)
            st.session_state["handwriting_df"] = hw_df
            st.rerun()
        return

    st.success(f"✅ Handwriting CSV loaded — {hw_df.shape[1]} features, {hw_df.shape[0]} row(s)")

    section_title("Feature Preview (first 10 columns)")
    st.dataframe(hw_df.iloc[:, :10], use_container_width=True)

    # Drop ID/class if present
    drop_cols = [c for c in ["ID", "class", "label"] if c in hw_df.columns]
    feature_df = hw_df.drop(columns=drop_cols, errors="ignore")

    st.markdown(f"**Original features available:** {feature_df.shape[1]}")
    st.markdown("**Features after SelectKBest:** 100")

    row_idx = 0
    if feature_df.shape[0] > 1:
        row_idx = st.number_input("Select row to analyze:", min_value=0, max_value=feature_df.shape[0] - 1, value=0)

    row = feature_df.iloc[row_idx].values

    if st.button("🔍 Run Handwriting Analysis", type="primary", use_container_width=True):
        with st.spinner("Running SelectKBest + XGBoost…"):
            try:
                from backend.handwriting.predictor import predict_from_csv_row
                result = predict_from_csv_row(row)
                st.session_state["handwriting_result"] = result
            except Exception as e:
                st.error(f"Error: {e}")
                return

    result = st.session_state.get("handwriting_result")
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
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(gauge_chart(result["probability"], "Handwriting Risk Score"), use_container_width=True)
    with col2:
        section_title("Feature Summary")
        st.markdown(f"""
        | Metric | Value |
        |---|---|
        | Original Features | {result['original_features']} |
        | Selected Features (K=100) | {result['selected_features']} |
        | Raw Label | {result['raw_label']} |
        | Probability | {result['probability']*100:.2f}% |
        | Prediction | {result['label']} |
        """)

    st.divider()
    section_title("Top 100 Selected Feature Values")
    st.plotly_chart(
        bar_chart(result["selected_values"], "Selected Feature Values after SelectKBest", "Feature Index"),
        use_container_width=True,
    )
