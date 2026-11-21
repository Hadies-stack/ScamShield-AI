
import streamlit as st
import joblib
import os

from modules.scam_dna import analyse_scam_dna
from modules.language_support import detect_language
from modules.risk_engine import calculate_risk

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "scamshield_model.joblib"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

st.title("🛡️ ScamShield AI")
st.subheader("Understand the scam. Before it catches you.")

st.write(
    "An AI-powered multilingual digital safety assistant."
)

message = st.text_area(
    "Paste your SMS message:",
    height=150,
    placeholder="Enter your message here..."
)

if st.button("Analyse Message", type="primary"):

    if not message.strip():
        st.warning("Please enter a message first.")

    else:
        language = detect_language(message)
        dna = analyse_scam_dna(message)

        prediction = None
        probability = None

        if os.path.exists(MODEL_PATH):
            try:
                model = load_model()
                prediction = model.predict([message])[0]
                probabilities = model.predict_proba([message])[0]

                scam_index = list(model.classes_).index("scam")
                probability = probabilities[scam_index] * 100

            except Exception:
                st.warning("AI model could not analyse this message.")

        risk = calculate_risk(
            dna,
            prediction,
            probability
        )

        st.divider()
        st.header("📊 Analysis Results")

        st.write(f"**Detected language:** {language}")

        st.subheader("🔬 Scam DNA")

        if dna["findings"]:
            for finding in dna["findings"]:
                st.warning(f"⚠️ {finding}")
        else:
            st.success("No known warning patterns detected.")

        st.subheader("🛡️ Risk Assessment")

        st.metric("Prototype risk score", f"{risk['score']}/100")
        st.write(f"**Risk level:** {risk['level']}")
        st.write(risk["explanation"])

        if probability is not None:
            st.metric(
                "Model-estimated scam probability",
                f"{probability:.2f}%"
            )
        else:
            st.info("Machine-learning model integration is pending.")

st.divider()

st.header("🔐 Digital Safety Centre")

st.info(
    "Never share your OTP, UPI PIN or password. "
    "Verify important requests independently."
)

st.caption(
    "Educational prototype. Risk scores and AI predictions "
    "are not proof of fraud or safety."
)
