"""Patient Screening intake page."""
import streamlit as st
from datetime import datetime
from frontend.components.cards import section_title


def render() -> None:
    st.title("👤 Patient Screening")
    st.caption("Enter patient details and upload data for analysis.")
    st.divider()

    with st.form("patient_form"):
        section_title("Patient Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Patient Name", placeholder="e.g. John Doe")
            age = st.number_input("Age", min_value=1, max_value=120, value=65)
            gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        with col2:
            language = st.selectbox("Language", ["English", "Hindi", "Marathi", "Other"])
            notes = st.text_area("Clinical Notes", placeholder="Optional observations…", height=100)

        st.divider()
        section_title("Upload Data")
        col3, col4 = st.columns(2)
        with col3:
            audio_file = st.file_uploader(
                "🎤 Speech Audio (.wav)", type=["wav"], help="Upload a .wav recording for speech analysis."
            )
        with col4:
            csv_file = st.file_uploader(
                "✍️ Handwriting Features (.csv)", type=["csv"], help="Single-row CSV with 451 handwriting features."
            )

        submitted = st.form_submit_button("💾 Save Patient & Prepare Analysis", use_container_width=True, type="primary")

    if submitted:
        if not name:
            st.error("Please enter a patient name.")
        else:
            st.session_state["current_patient"] = {
                "name": name,
                "age": age,
                "gender": gender,
                "language": language,
                "notes": notes,
            }
            if audio_file:
                # Save to uploads/
                import os, shutil
                os.makedirs("uploads", exist_ok=True)
                path = f"uploads/{audio_file.name}"
                with open(path, "wb") as f:
                    f.write(audio_file.getbuffer())
                st.session_state["audio_path"] = path
                st.success(f"✅ Audio saved: {audio_file.name}")
            if csv_file:
                import pandas as pd
                df = pd.read_csv(csv_file)
                st.session_state["handwriting_df"] = df
                st.success(f"✅ Handwriting CSV loaded — {df.shape[1]} features, {df.shape[0]} row(s)")

            st.success(f"✅ Patient **{name}** registered! Navigate to the analysis pages from the sidebar.")
            st.balloons()

    # Show current session patient
    if "current_patient" in st.session_state:
        st.divider()
        p = st.session_state["current_patient"]
        section_title("Current Patient Session")
        st.markdown(f"""
        | Field | Value |
        |---|---|
        | **Name** | {p['name']} |
        | **Age** | {p['age']} |
        | **Gender** | {p['gender']} |
        | **Language** | {p['language']} |
        | **Notes** | {p['notes'] or '—'} |
        """)
