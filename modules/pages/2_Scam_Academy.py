
import streamlit as st

st.set_page_config(
    page_title="Scam Academy | ScamShield AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Scam Academy")
st.subheader("Learn to recognise digital scams.")

st.write(
    "Test your cybersecurity awareness with these short quizzes."
)

questions = [
    {
        "question": "Someone asks for your OTP to receive a prize. What should you do?",
        "options": [
            "Share the OTP",
            "Ignore the request and verify independently",
            "Forward the OTP to a friend"
        ],
        "answer": "Ignore the request and verify independently",
        "explanation": "An OTP is private. Never share it with anyone."
    },
    {
        "question": "You receive an unexpected UPI collect request. What should you do?",
        "options": [
            "Approve immediately",
            "Check the request and sender before taking action",
            "Share your UPI PIN"
        ],
        "answer": "Check the request and sender before taking action",
        "explanation": "Review unexpected payment requests carefully."
    },
    {
        "question": "A message says your bank account will be blocked unless you click a link. What is safest?",
        "options": [
            "Click the link immediately",
            "Reply with your bank details",
            "Contact the bank through its official app or website"
        ],
        "answer": "Contact the bank through its official app or website",
        "explanation": "Independent verification helps avoid phishing."
    }
]

for index, item in enumerate(questions):
    st.divider()
    st.subheader(f"Question {index + 1}")

    choice = st.radio(
        item["question"],
        item["options"],
        key=f"question_{index}"
    )

    if st.button("Check Answer", key=f"check_{index}"):
        if choice == item["answer"]:
            st.success("Correct! " + item["explanation"])
        else:
            st.error("Not quite. " + item["explanation"])

st.divider()

st.info(
    "Remember: Never share your OTP, UPI PIN or password."
)
