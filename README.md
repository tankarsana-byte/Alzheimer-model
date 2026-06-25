# 🧠 NeuroSense AI
## Multimodal Explainable Alzheimer's Screening System
> An IEEE research project for early Alzheimer's detection using speech and handwriting analysis.

---

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/your-username/NeuroSense_AI.git
cd NeuroSense_AI
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add Your Trained Models
Place these files inside the `models/` folder:
- `speech_xgb.pkl`
- `handwriting_xgb.pkl`
- `feature_selector.pkl`
- `label_encoder.pkl`

> Train them using `Handwriting.ipynb` and `Speech_model.ipynb` from your notebooks.

### 3. Run the App
```bash
streamlit run app.py
```

---

## 📁 Project Structure
```
NeuroSense_AI/
├── app.py                        # Main Streamlit entry point
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml               # Theme & server config
├── models/                       # Place .pkl files here
├── backend/
│   ├── speech/
│   │   ├── feature_extractor.py  # MFCC, Chroma, Mel extraction
│   │   └── predictor.py          # Speech model inference
│   ├── handwriting/
│   │   └── predictor.py          # Handwriting model inference
│   └── fusion/
│       └── fusion.py             # Weighted fusion logic
├── frontend/
│   ├── styles/theme.py           # CSS & colors
│   ├── components/cards.py       # Reusable UI components
│   ├── charts/plots.py           # Plotly chart helpers
│   └── pages/                    # One file per sidebar page
│       ├── dashboard.py
│       ├── patient_screening.py
│       ├── speech_analysis.py
│       ├── handwriting_analysis.py
│       ├── fusion_page.py
│       ├── explainable_ai.py
│       ├── reports.py
│       └── about.py
├── assets/
├── uploads/                      # Auto-created for audio uploads
└── reports/                      # Auto-created for PDF reports
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New App**.
3. Select your repository, branch (`main`), and set **Main file** to `app.py`.
4. Under **Advanced Settings**, add any secrets if needed.
5. Click **Deploy**.

> **Note:** `.pkl` model files must be committed to the repo or loaded from an external storage (e.g. Hugging Face Hub, GCS). GitHub blocks files >100MB — use Git LFS if needed.

---

## 🧪 Model Details

| Model | Algorithm | Features |
|---|---|---|
| Speech | XGBoost (500 trees) | 65 (MFCC×13, Chroma×12, Mel×40) |
| Handwriting | XGBoost + SelectKBest | 451 → 100 |
| Fusion | Weighted Average | 60% speech + 40% handwriting |

---

## ⚠️ Disclaimer
This system is a research prototype and **not a clinical diagnostic tool**. Always consult a certified neurologist.
