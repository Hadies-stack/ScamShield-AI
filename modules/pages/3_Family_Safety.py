
import streamlit as st

st.set_page_config(
    page_title="Family Safety | ScamShield AI",
    page_icon="👨‍👩‍👧‍👦",
    layout="wide"
)

st.title("👨‍👩‍👧‍👦 Family Safety Centre")

st.subheader("Digital safety starts with awareness.")

st.write(
    "Simple safety guidance to help families "
    "recognise suspicious online activity."
)

st.divider()

st.header("🚨 Five Golden Rules")

rules = [
    "Never share an OTP with anyone.",
    "Never share your UPI PIN or banking password.",
    "Do not trust unexpected prize or lottery messages.",
    "Verify payment requests before approving them.",
    "Contact organisations using their official contact details."
]

for index, rule in enumerate(rules, 1):
    st.write(f"**{index}.** {rule}")

st.divider()

st.header("📱 Common Situations")

with st.expander("Someone claims to be from your bank"):
    st.write(
        "Do not share confidential information. "
        "End the conversation and contact your bank "
        "using its official contact details."
    )

with st.expander("Someone promises a lottery prize"):
    st.write(
        "Be cautious of unexpected prize claims, "
        "especially when payment or personal details are requested."
    )

with st.expander("Someone sends an unexpected payment request"):
    st.write(
        "Check the recipient and purpose carefully. "
        "Never approve a payment just because someone pressures you."
    )

with st.expander("A family member may have experienced online fraud"):
    st.write(
        "Stay calm. Contact the bank or payment provider "
        "immediately if money is involved. In India, "
        "call 1930 for financial cyber fraud reporting "
        "and use the official cybercrime portal."
    )

st.divider()

st.header("💡 Family Safety Checklist")

checklist = [
    "Important accounts have strong, unique passwords.",
    "Multi-factor authentication is enabled where available.",
    "Family members know never to share OTPs or PINs.",
    "Devices and applications are updated.",
    "Everyone knows how to contact their bank officially."
]

for item in checklist:
    st.checkbox(item)

st.caption(
    "ScamShield AI promotes awareness and responsible "
    "digital behaviour. It does not replace professional support."
)
