
import streamlit as st


def metric_card(label: str, value: str, color_class: str = "") -> None:
    """Render a colored metric card."""
    st.markdown(
        f"""
        <div class="ns-metric-card {color_class}">
            <div class="ns-metric-value">{value}</div>
            <div class="ns-metric-label">{label}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def info_card(content: str) -> None:
    """Render a glass-effect info card."""
    st.markdown(f'<div class="ns-card">{content}</div>', unsafe_allow_html=True)


def section_title(title: str) -> None:
    """Render a styled section title."""
    st.markdown(f'<div class="ns-section-title">{title}</div>', unsafe_allow_html=True)


def prediction_banner(label: str, prob: float, risk_level: str, risk_color: str) -> None:
    """Render a large prediction result banner."""
    css_class = "prediction-positive" if prob >= 0.5 else "prediction-negative"
    icon = "🔴" if prob >= 0.5 else "🟢"
    st.markdown(
        f"""
        <div class="{css_class}">
            <div style="font-size:2rem;">{icon}</div>
            <div style="font-size:1.4rem;font-weight:700;margin:0.3rem 0;">{label}</div>
            <div style="font-size:1rem;color:#475569;">
                Confidence: <strong>{prob*100:.1f}%</strong> &nbsp;|&nbsp;
                <span style="color:{risk_color};font-weight:600;">{risk_level}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
