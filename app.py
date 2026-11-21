
import streamlit as st
import joblib
import os

from modules.scam_dna import analyse_scam_dna
from modules.language_support import detect_language

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
    "Your AI-powered digital safety companion."
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

        st.divider()
        st.header("📊 Message Analysis")

        st.write(f"**Detected language:** {language}")

        st.header("🔬 Scam DNA")

        if dna["findings"]:
            for finding in dna["findings"]:
                st.warning(f"⚠️ {finding}")
        else:
            st.success("No known warning patterns detected.")

        st.write(
            f"Risk indicators identified: "
            f"{dna['risk_indicators_count']}"
        )

        st.divider()
        st.header("🤖 AI Detection")

        if os.path.exists(MODEL_PATH):
            try:
                model = load_model()
                prediction = model.predict([message])[0]
                probabilities = model.predict_proba([message])[0]

                scam_index = list(model.classes_).index("scam")
                probability = probabilities[scam_index] * 100

                st.metric(
                    "Estimated scam probability",
                    f"{probability:.2f}%"
                )

                if prediction == "scam":
                    st.error("Suspicious message pattern detected.")
                else:
                    st.success("No strong scam pattern detected.")

            except Exception:
                st.error("The AI model could not analyse this message.")

        else:
            st.info(
                "Machine-learning model integration is pending."
            )

st.divider()
st.header("🔐 Digital Safety Centre")

st.info(
    "Never share your OTP, UPI PIN or password. "
    "Always independently verify suspicious messages."
)

st.caption(
    "Educational prototype. Language detection, "
    "AI predictions and warning indicators can be incorrect."
)
