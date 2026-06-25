"""CSS and styling constants for NeuroSense AI."""

CUSTOM_CSS = """
<style>
/* ── Global ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* ── Cards ── */
.ns-card {
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 1.5rem;
    border: 1px solid rgba(37, 99, 235, 0.1);
    box-shadow: 0 4px 24px rgba(0,0,0,0.06);
    margin-bottom: 1rem;
}

.ns-metric-card {
    background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
    color: white;
    border-radius: 16px;
    padding: 1.25rem 1.5rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(37,99,235,0.3);
}

.ns-metric-card.teal {
    background: linear-gradient(135deg, #14B8A6 0%, #0D9488 100%);
    box-shadow: 0 4px 20px rgba(20,184,166,0.3);
}

.ns-metric-card.red {
    background: linear-gradient(135deg, #DC2626 0%, #B91C1C 100%);
    box-shadow: 0 4px 20px rgba(220,38,38,0.3);
}

.ns-metric-card.slate {
    background: linear-gradient(135deg, #64748B 0%, #475569 100%);
    box-shadow: 0 4px 20px rgba(100,116,139,0.3);
}

.ns-metric-value {
    font-size: 2rem;
    font-weight: 700;
    line-height: 1;
}

.ns-metric-label {
    font-size: 0.8rem;
    opacity: 0.85;
    margin-top: 0.25rem;
}

/* ── Risk Badge ── */
.risk-badge {
    display: inline-block;
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}

/* ── Section Headers ── */
.ns-section-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 0.5rem;
    border-left: 4px solid #2563EB;
    padding-left: 0.75rem;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
}

section[data-testid="stSidebar"] * {
    color: #E2E8F0 !important;
}

/* ── Prediction banner ── */
.prediction-positive {
    background: linear-gradient(135deg, #FEF2F2, #FEE2E2);
    border: 2px solid #DC2626;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    text-align: center;
}

.prediction-negative {
    background: linear-gradient(135deg, #F0FDF4, #DCFCE7);
    border: 2px solid #22C55E;
    border-radius: 12px;
    padding: 1rem 1.5rem;
    text-align: center;
}
</style>
"""

PRIMARY = "#2563EB"
SECONDARY = "#14B8A6"
ACCENT = "#DC2626"
BG = "#F8FAFC"
