
import streamlit as st
import joblib
import os

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
    "An AI-powered SMS scam detection prototype "
    "designed to promote digital safety."
)

if not os.path.exists(MODEL_PATH):
    st.warning(
        "The AI model has not been uploaded yet. "
        "Model integration is under development."
    )
else:
    model = load_model()

    message = st.text_area(
        "Paste a suspicious SMS message:",
        height=150,
        placeholder="Enter your message here..."
    )

    if st.button("Analyse Message", type="primary"):
        if not message.strip():
            st.warning("Please enter a message first.")
        else:
            prediction = model.predict([message])[0]
            probabilities = model.predict_proba([message])[0]

            scam_index = list(model.classes_).index("scam")
            probability = probabilities[scam_index] * 100

            st.divider()
            st.subheader("Analysis Results")

            st.metric(
                "Estimated scam probability",
                f"{probability:.2f}%"
            )

            if prediction == "scam":
                st.error("⚠️ Suspicious message pattern detected.")
            else:
                st.success("No strong scam pattern detected.")

st.divider()

st.subheader("🔐 Digital Safety Reminder")
st.info(
    "Never share your OTP, UPI PIN or password. "
    "Independently verify suspicious messages and links."
)

st.caption(
    "Educational prototype. AI predictions can be incorrect."
)
