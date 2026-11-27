
import streamlit as st
from modules.ui_theme import apply_theme

st.set_page_config(
    page_title="Family Safety | ScamShield AI",
    page_icon="👨‍👩‍👧‍👦",
    layout="wide"
)

apply_theme()

# =========================================================
# PREMIUM FAMILY SAFETY THEME
# =========================================================

st.markdown("""
<style>
.block-container {
    max-width: 1450px;
    padding: 2rem 2rem 3rem;
}

.stApp {
    background:
        radial-gradient(ellipse at 90% 0%, rgba(65,120,255,.13), transparent 35%),
        linear-gradient(145deg, #080F1D, #0B162A 55%, #080F1D);
    color: #EAF0FF;
}

h1, h2, h3 {
    color: #F0F4FF !important;
    letter-spacing: -0.5px;
}

p, label, li {
    color: #AABBD7;
    line-height: 1.8;
}

.family-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.family-title {
    color: #F4F7FF;
    font-size: clamp(2.1rem, 4vw, 3.5rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
    margin-bottom: 14px;
}

.family-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.family-description {
    color: #A5B5D1;
    font-size: .96rem;
    line-height: 1.9;
    max-width: 800px;
}

div[data-testid="stMetric"] {
    background: linear-gradient(145deg,rgba(22,39,70,.96),rgba(12,22,42,.98));
    border: 1px solid rgba(117,153,220,.19);
    border-radius: 17px;
    padding: 19px;
}

div[data-testid="stMetricLabel"] {
    color: #AABBD7 !important;
}

div[data-testid="stMetricValue"] {
    color: #8CB9FF !important;
    font-weight: 800;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg,rgba(20,36,65,.75),rgba(12,22,42,.88));
    border: 1px solid rgba(117,153,220,.18);
    border-radius: 17px;
}

div[data-testid="stCheckbox"] {
    background: rgba(17,31,56,.75);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 11px;
    padding: 12px;
    margin-bottom: 8px;
}

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
    margin-bottom: 10px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg,#2868D8,#72D9FF);
}

a {
    color: #9FC5FF !important;
}

hr {
    border-color: rgba(120,155,220,.16);
}

.family-footer {
    text-align: center;
    color: #8296B8;
    font-size: .76rem;
    padding: 25px 0 10px;
    border-top: 1px solid rgba(120,155,220,.16);
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="family-eyebrow">SCAMSHIELD AI / FAMILY PROTECTION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="family-title">Family <span>Digital Protection.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="family-description">'
    'A safer digital world starts with an informed family. '
    'Learn essential safety habits, recognise common threats '
    'and build stronger digital awareness together.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("FAMILY PROTECTION  /  DIGITAL AWARENESS  /  ONLINE SAFETY")

st.divider()


# =========================================================
# PROTECTION OVERVIEW
# =========================================================

st.subheader("🛡️ Family Protection Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Golden Safety Rules", "05")

with col2:
    st.metric("Threat Scenarios", "04")

with col3:
    st.metric("Protection Checklist", "05 Items")

st.divider()


# =========================================================
# GOLDEN RULES
# =========================================================

st.subheader("🚨 Five Golden Rules")

st.write(
    "Simple habits that can help protect every family member "
    "from common digital threats."
)

rules = [
    (
        "01",
        "🔐 Protect Your OTP",
        "Never share an OTP with anyone, even someone claiming to be an official."
    ),
    (
        "02",
        "🏦 Secure Banking Details",
        "Never share your UPI PIN or banking password."
    ),
    (
        "03",
        "🎁 Question Unexpected Rewards",
        "Do not trust unexpected prize or lottery messages."
    ),
    (
        "04",
        "💳 Verify Every Payment",
        "Check payment requests carefully before approving them."
    ),
    (
        "05",
        "📞 Verify Official Contacts",
        "Contact organisations using their independently verified official details."
    )
]

for start in range(0, len(rules), 2):

    columns = st.columns(2)

    for column, rule in zip(columns, rules[start:start + 2]):

        number, title, description = rule

        with column:
            with st.container(border=True):

                st.caption(f"FAMILY SAFETY RULE {number}")
                st.markdown(f"### {title}")
                st.write(description)


# =========================================================
# COMMON THREAT SCENARIOS
# =========================================================

st.divider()

st.subheader("⚠️ Recognise Common Threat Situations")

st.caption(
    "Learn how to respond when someone in your family "
    "encounters suspicious communication."
)

with st.expander("🏦 Someone claims to be from your bank"):

    st.warning("Do not share confidential information.")

    st.write(
        "End the conversation and contact your bank "
        "using its independently verified official contact details."
    )

with st.expander("🎁 Someone promises a lottery prize"):

    st.warning("Unexpected prize claims deserve caution.")

    st.write(
        "Be especially careful when a prize message asks "
        "for advance payment or personal information."
    )

with st.expander("💳 Someone sends an unexpected payment request"):

    st.warning("Never approve a payment under pressure.")

    st.write(
        "Check the recipient and purpose carefully. "
        "Verify the request independently before making a payment."
    )

with st.expander("🚨 A family member may have experienced online fraud"):

    st.error("Act promptly and use official reporting channels.")

    st.write(
        "Stay calm. Contact the bank or payment provider "
        "immediately if money is involved."
    )

    st.markdown(
        "**India: Call 1930 promptly for financial cyber fraud reporting.**"
    )

    st.markdown(
        "[Official National Cyber Crime Portal](https://cybercrime.gov.in/)"
    )


# =========================================================
# FAMILY CHECKLIST
# =========================================================

st.divider()

st.subheader("✅ Family Digital Safety Checklist")

st.write(
    "Complete these basic security checks together."
)

checklist = [
    "Important accounts have strong, unique passwords.",
    "Multi-factor authentication is enabled where available.",
    "Family members know never to share OTPs or PINs.",
    "Devices and applications are updated.",
    "Everyone knows how to contact their bank officially."
]

completed = 0

for item in checklist:

    if st.checkbox(item, key=f"family_{item}"):
        completed += 1


# =========================================================
# CHECKLIST PROGRESS
# =========================================================

progress = completed / len(checklist)

st.markdown("### Protection Readiness")

st.progress(progress)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Completed Checks",
        f"{completed}/{len(checklist)}"
    )

with col2:
    st.metric(
        "Checklist Progress",
        f"{int(progress * 100)}%"
    )

if completed == len(checklist):

    st.success(
        "All five awareness checks have been completed!"
    )

else:

    st.info(
        "Continue reviewing the checklist with your family."
    )


# =========================================================
# SAFETY REMINDER
# =========================================================

st.divider()

st.subheader("💡 Remember")

st.info(
    "A suspicious message or call should never force you "
    "to make a rushed decision. Pause, verify independently "
    "and ask a trusted person for help."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="family-footer">'
    'SCAMSHIELD AI  •  FAMILY DIGITAL PROTECTION CENTRE'
    '<br>EXPERIMENTAL EDUCATIONAL CYBERSECURITY PROJECT'
    '</div>',
    unsafe_allow_html=True
)
