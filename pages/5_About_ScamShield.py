
import streamlit as st
from modules.ui_theme import apply_theme

st.set_page_config(
    page_title="About ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

apply_theme()

# =========================================================
# PREMIUM NAVY + ELECTRIC BLUE DESIGN
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
        linear-gradient(145deg, #061326, #081B31 55%, #061326);
    color: #EAF0FF;
}

h1, h2, h3 {
    color: #F1F5FF !important;
    letter-spacing: -0.5px;
}

p, label, li {
    color: #AABBD7;
    line-height: 1.8;
}

.about-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.about-title {
    color: #F4F7FF;
    font-size: clamp(2.1rem, 4vw, 3.5rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
    margin-bottom: 14px;
}

.about-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF,#A4C9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.about-description {
    color: #A5B5D1;
    font-size: .96rem;
    line-height: 1.9;
    max-width: 850px;
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
    color: #72B7FF !important;
    font-weight: 800;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg,rgba(20,36,65,.75),rgba(12,22,42,.88));
    border: 1px solid rgba(117,153,220,.18);
    border-radius: 17px;
}

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
}

a {
    color: #9FC5FF !important;
}

hr {
    border-color: rgba(120,155,220,.16);
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="about-eyebrow">SCAMSHIELD AI / PROJECT PROFILE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="about-title">Meet <span>ScamShield AI.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="about-description">'
    'Understand the scam before it catches you. '
    'Intelligent awareness, responsible technology '
    'and safer digital decisions.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("ARTIFICIAL INTELLIGENCE  /  CYBERSECURITY  /  DIGITAL PROTECTION")

st.divider()


# =========================================================
# PROJECT INTRODUCTION
# =========================================================

left, right = st.columns([1.7, 1])

with left:
    st.subheader("🎯 The Vision")

    st.write("""
    ScamShield AI is a student-developed Artificial Intelligence
    and cybersecurity awareness project.

    Its purpose is to help people understand suspicious digital
    communication, recognise possible warning signs and make
    more informed online decisions.

    Rather than simply displaying a warning, ScamShield aims
    to explain why a message deserves attention and what safer
    steps a person can take.
    """)

with right:
    with st.container(border=True):
        st.markdown("### ✨ Project Identity")
        st.markdown("**Name:** ScamShield AI")
        st.markdown("**Domain:** AI + Cybersecurity")
        st.markdown("**Focus:** Digital Threat Awareness")
        st.markdown("**Project Type:** Educational Prototype")
        st.markdown("**Development:** Class 12 AI Capstone")


# =========================================================
# PROJECT OVERVIEW
# =========================================================

st.divider()
st.subheader("📊 Project at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Core Domains", "04")

with col2:
    st.metric("Language Modes", "03")

with col3:
    st.metric("Analysis Channels", "02")

with col4:
    st.metric("Design Principle", "Privacy First")


# =========================================================
# HOW IT WORKS
# =========================================================

st.divider()
st.subheader("🧠 Inside the ScamShield Intelligence System")

st.write(
    "The analysis process is designed to turn an unfamiliar "
    "message into understandable safety information."
)

pipeline = [
    ("01", "📩 Message Input",
     "The user voluntarily provides a message or call summary."),
    ("02", "🌐 Language Detection",
     "The system estimates whether the content is English, Hindi or Hinglish."),
    ("03", "🧬 Scam DNA",
     "The system searches for potentially suspicious communication patterns."),
    ("04", "🤖 Classification",
     "An optional trained machine-learning model can provide an additional classification."),
    ("05", "📊 Risk Assessment",
     "Available indicators are combined into an experimental risk score."),
    ("06", "🛡️ Safety Guidance",
     "The user receives explanations and practical safety recommendations.")
]

for number, title, description in pipeline:
    with st.container(border=True):
        col1, col2 = st.columns([1, 5])

        with col1:
            st.markdown(f"## {number}")

        with col2:
            st.markdown(f"### {title}")
            st.write(description)


# =========================================================
# SIGNATURE FEATURE
# =========================================================

st.divider()
st.subheader("🧬 Our Signature Concept — Scam DNA")

with st.container(border=True):
    st.markdown("## Understand WHY a message looks suspicious.")

    st.write("""
    Scam DNA is designed to explain potentially suspicious
    characteristics instead of presenting only a basic label.

    It can highlight patterns such as:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        - Urgency and pressure
        - Requests for sensitive information
        - Payment demands
        """)

    with col2:
        st.markdown("""
        - Prize and reward claims
        - Suspicious link language
        - Potential impersonation indicators
        """)

    st.info(
        "These are pattern-based indicators, not proof that "
        "a particular sender or message is fraudulent."
    )


# =========================================================
# PRIVACY PRINCIPLES
# =========================================================

st.divider()
st.subheader("🔐 Privacy by Design")

privacy = [
    ("🔒", "No unnecessary data collection",
     "The project should avoid collecting personal information it does not need."),
    ("🚫", "No credential requests",
     "ScamShield never needs your OTP, UPI PIN or banking password."),
    ("👁️", "Transparent analysis",
     "Users should understand the methods and limitations behind an assessment."),
    ("🧑‍⚖️", "User control",
     "Any optional threat report should require clear user consent.")
]

for icon, title, description in privacy:
    with st.container(border=True):
        st.markdown(f"### {icon} {title}")
        st.write(description)


# =========================================================
# LIMITATIONS
# =========================================================

st.divider()
st.subheader("⚠️ Transparency & Limitations")

st.warning("""
ScamShield AI is an experimental educational prototype.

It cannot guarantee that a message, phone call or website is safe.
It does not independently verify bank accounts, identify callers,
monitor live phone calls or automatically block threats.

Its risk score is experimental and must not be treated as a
verified probability of fraud.

It does not directly submit reports to police or telecom systems.
Use official reporting channels for real incidents.
""")


# =========================================================
# DEVELOPMENT ROADMAP
# =========================================================

st.divider()
st.subheader("🚀 Development Roadmap")

roadmap = [
    ("01", "Multilingual Message Analysis",
     "English, Hindi and Hinglish support"),
    ("02", "Scam DNA Intelligence",
     "Explainable suspicious-pattern detection"),
    ("03", "Link Safety",
     "Basic URL warning-indicator inspection"),
    ("04", "Threat Network",
     "Community-oriented pattern reporting prototype"),
    ("05", "Advanced Protection",
     "Future research into authorised mobile security features")
]

for number, title, description in roadmap:
    with st.container(border=True):
        st.markdown(f"### {number} — {title}")
        st.write(description)


# =========================================================
# TRUSTED RESOURCES
# =========================================================

st.divider()
st.subheader("🌐 Trusted Cybersecurity Resources")

resources = [
    ("CERT-In", "https://www.cert-in.org.in/"),
    ("OWASP", "https://owasp.org/"),
    ("National Cyber Crime Portal", "https://cybercrime.gov.in/"),
    ("Google Safe Browsing", "https://safebrowsing.google.com/")
]

for title, url in resources:
    st.markdown(f"- [{title}]({url})")


# =========================================================
# CLOSING
# =========================================================

st.divider()

st.markdown("""
<div style="text-align:center; padding:25px 10px;">
    <div style="
        font-size:clamp(1.4rem,3vw,2rem);
        font-weight:900;
        color:#EAF0FF;
        margin-bottom:12px;">
        A safer digital future begins with awareness.
    </div>
    <div style="
        color:#9AACC9;
        letter-spacing:2px;
        font-size:.72rem;
        font-weight:800;">
        SCAMSHIELD AI • BUILT WITH PURPOSE • POWERED BY RESPONSIBLE AI
    </div>
</div>
""", unsafe_allow_html=True)

st.caption("Class 12 Artificial Intelligence Capstone Project")
