"""Plotly chart helpers for NeuroSense AI."""
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from typing import List


PRIMARY = "#2563EB"
SECONDARY = "#14B8A6"
ACCENT = "#DC2626"


def bar_chart(values: np.ndarray, title: str, x_label: str = "Feature Index") -> go.Figure:
    """Simple bar chart for feature arrays."""
    fig = px.bar(
        x=list(range(len(values))),
        y=values,
        title=title,
        labels={"x": x_label, "y": "Value"},
        color_discrete_sequence=[PRIMARY],
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
        title_font_size=14,
        height=300,
    )
    return fig


def gauge_chart(value: float, title: str = "Risk Score") -> go.Figure:
    """Gauge meter for probability display."""
    color = ACCENT if value >= 0.5 else SECONDARY
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number+delta",
            value=value * 100,
            title={"text": title, "font": {"size": 16}},
            delta={"reference": 50},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1},
                "bar": {"color": color},
                "steps": [
                    {"range": [0, 25], "color": "#DCFCE7"},
                    {"range": [25, 50], "color": "#FEF9C3"},
                    {"range": [50, 75], "color": "#FEE2E2"},
                    {"range": [75, 100], "color": "#FECACA"},
                ],
                "threshold": {
                    "line": {"color": "#1E293B", "width": 3},
                    "thickness": 0.75,
                    "value": 50,
                },
            },
            number={"suffix": "%", "font": {"size": 28}},
        )
    )
    fig.update_layout(
        height=300,
        paper_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
    )
    return fig


def fusion_comparison_chart(speech_prob: float, handwriting_prob: float, final_prob: float) -> go.Figure:
    """Horizontal bar comparison of all three probabilities."""
    labels = ["Speech Model", "Handwriting Model", "Fusion Result"]
    values = [speech_prob * 100, handwriting_prob * 100, final_prob * 100]
    colors = [PRIMARY, SECONDARY, ACCENT if final_prob >= 0.5 else "#22C55E"]

    fig = go.Figure(
        go.Bar(
            y=labels,
            x=values,
            orientation="h",
            marker_color=colors,
            text=[f"{v:.1f}%" for v in values],
            textposition="outside",
        )
    )
    fig.add_vline(x=50, line_dash="dash", line_color="#94A3B8", annotation_text="Threshold (50%)")
    fig.update_layout(
        xaxis=dict(range=[0, 110], title="Probability (%)"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
        height=280,
        title="Model Probability Comparison",
    )
    return fig


def feature_importance_chart(importances: np.ndarray, feature_names: List[str], title: str) -> go.Figure:
    """Top-N feature importance horizontal bar chart."""
    n = min(20, len(importances))
    idx = np.argsort(importances)[-n:]
    fig = go.Figure(
        go.Bar(
            x=importances[idx],
            y=[feature_names[i] for i in idx],
            orientation="h",
            marker_color=PRIMARY,
        )
    )
    fig.update_layout(
        title=title,
        xaxis_title="Importance",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
        height=420,
    )
    return fig


def risk_distribution_pie(healthy: int, positive: int) -> go.Figure:
    """Pie chart for risk distribution."""
    fig = go.Figure(
        go.Pie(
            labels=["Healthy", "Alzheimer's Positive"],
            values=[healthy, positive],
            hole=0.5,
            marker_colors=[SECONDARY, ACCENT],
        )
    )
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_family="Inter",
        height=300,
        showlegend=True,
    )
    return fig
