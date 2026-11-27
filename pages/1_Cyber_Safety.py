
import streamlit as st
from modules.ui_theme import apply_theme

st.set_page_config(
    page_title="Cyber Safety | ScamShield AI",
    page_icon="🔐",
    layout="wide"
)

apply_theme()

# =========================================================
# PREMIUM CYBER SAFETY THEME
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

.cyber-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.cyber-title {
    color: #F4F7FF;
    font-size: clamp(2.1rem, 4vw, 3.5rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
    margin-bottom: 14px;
}

.cyber-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.cyber-description {
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

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
    margin-bottom: 10px;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 800;
    min-height: 45px;
    border: 1px solid rgba(125,170,255,.35);
    background: linear-gradient(110deg,#2868D8,#247FBF);
    color: white;
}

div.stButton > button:hover {
    border-color: #A9CAFF;
    color: white;
}

a {
    color: #9FC5FF !important;
}

hr {
    border-color: rgba(120,155,220,.16);
}

.cyber-footer {
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
    '<div class="cyber-eyebrow">SCAMSHIELD AI / SECURITY OPERATIONS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="cyber-title">Your Digital <span>Safety Centre.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="cyber-description">'
    'Understand digital threats, strengthen your online security '
    'and develop safer habits with practical cybersecurity guidance.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("SECURITY AWARENESS  /  DIGITAL DEFENCE  /  PROTECTION")

st.divider()


# =========================================================
# SECURITY OVERVIEW
# =========================================================

st.subheader("🛡️ Security Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Protection Domains", "04")

with col2:
    st.metric("Safety Practices", "12+")

with col3:
    st.metric("Official Resources", "03")

with col4:
    st.metric("Awareness Mode", "ACTIVE")

st.divider()


# =========================================================
# SECURITY DOMAINS
# =========================================================

st.subheader("📡 Digital Protection Domains")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 💳 01 — UPI SECURITY")
        st.write(
            "Protect payment activity and recognise "
            "suspicious financial requests."
        )
        st.markdown("""
- Never enter your UPI PIN to receive money.
- Verify the recipient before making a payment.
- Never share your UPI PIN or OTP.
- Be cautious of unexpected collect requests.
- Contact your bank through official channels.
""")

with col2:
    with st.container(border=True):
        st.markdown("### 🎣 02 — PHISHING DEFENCE")
        st.write(
            "Recognise deceptive messages and suspicious "
            "website links."
        )
        st.markdown("""
- Question unexpected account warnings.
- Avoid sharing personal information through messages.
- Be careful with urgent payment requests.
- Check website domains independently.
- Never open unfamiliar links without verification.
""")

col3, col4 = st.columns(2)

with col3:
    with st.container(border=True):
        st.markdown("### 🔑 03 — ACCOUNT SECURITY")
        st.write(
            "Build stronger protection for your online identity."
        )
        st.markdown("""
- Use unique passwords for important accounts.
- Enable multi-factor authentication.
- Never share login verification codes.
- Review account activity regularly.
- Keep devices and applications updated.
""")

with col4:
    with st.container(border=True):
        st.markdown("### 📱 04 — DEVICE AWARENESS")
        st.write(
            "Develop safer habits while using digital devices."
        )
        st.markdown("""
- Install applications from trusted sources.
- Review application permissions.
- Avoid unknown downloads.
- Install security updates.
- Lock devices when not in use.
""")


# =========================================================
# THREAT AWARENESS
# =========================================================

st.divider()

st.subheader("⚠️ Common Threat Indicators")

st.write(
    "These behaviours deserve caution and independent verification."
)

with st.expander("🚨 Urgent messages and account warnings"):
    st.write(
        "Messages claiming that an account will be blocked "
        "unless you act immediately may be designed to create panic."
    )
    st.info(
        "Verify the claim using the organisation's official app "
        "or independently confirmed contact details."
    )

with st.expander("🎁 Unexpected prizes and rewards"):
    st.write(
        "Unexpected prize claims that demand payment or "
        "sensitive information should be treated cautiously."
    )
    st.info(
        "Do not pay an unexpected fee or share confidential details "
        "just to claim a reward."
    )

with st.expander("📞 Impersonation and suspicious calls"):
    st.write(
        "A caller may claim to represent a bank, government office "
        "or law-enforcement organisation."
    )
    st.info(
        "End the conversation if pressured and independently "
        "contact the organisation using verified details."
    )


# =========================================================
# OFFICIAL RESOURCES
# =========================================================

st.divider()

st.subheader("🌐 Official Cybersecurity Resources")

st.write(
    "Use trusted sources for cybersecurity information "
    "and incident reporting."
)

resources = [
    (
        "🇮🇳 CERT-In",
        "Indian Computer Emergency Response Team",
        "https://www.cert-in.org.in/"
    ),
    (
        "🚨 National Cyber Crime Portal",
        "Official portal for reporting cybercrime in India",
        "https://cybercrime.gov.in/"
    ),
    (
        "🛡️ OWASP",
        "Open Worldwide Application Security Project",
        "https://owasp.org/"
    )
]

for title, description, url in resources:
    with st.container(border=True):
        st.markdown(f"### {title}")
        st.write(description)
        st.markdown(f"[Visit Official Resource]({url})")


# =========================================================
# EMERGENCY GUIDANCE
# =========================================================

st.divider()

st.subheader("🚨 If Financial Cyber Fraud Happens")

st.error(
    "Act quickly. Contact your bank or payment provider "
    "immediately if money may have been lost."
)

st.markdown("""
1. Contact your bank through its official support channel.
2. Call **1930** promptly for financial cyber fraud reporting in India.
3. Submit a report through the official National Cyber Crime Portal.
4. Preserve relevant transaction details and communications.
""")

st.markdown(
    "[Open National Cyber Crime Reporting Portal](https://cybercrime.gov.in/)"
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="cyber-footer">'
    'SCAMSHIELD AI  •  CYBER SECURITY OPERATIONS CENTRE'
    '<br>EDUCATIONAL DIGITAL SAFETY PLATFORM'
    '</div>',
    unsafe_allow_html=True
)
