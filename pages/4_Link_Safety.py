
import streamlit as st
from modules.ui_theme import apply_theme
from modules.link_checker import check_url

st.set_page_config(
    page_title="Link Safety | ScamShield AI",
    page_icon="🔗",
    layout="wide"
)

apply_theme()

# =========================================================
# PREMIUM LINK SAFETY THEME
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

.link-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.link-title {
    color: #F4F7FF;
    font-size: clamp(2.1rem, 4vw, 3.5rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
    margin-bottom: 14px;
}

.link-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.link-description {
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

div[data-testid="stTextInput"] input {
    background: #101F38;
    color: #F0F4FF;
    border: 1px solid rgba(117,153,220,.3);
    border-radius: 12px;
    min-height: 48px;
}

div[data-testid="stTextInput"] input:focus {
    border-color: #75A9FF;
    box-shadow: 0 0 0 1px #75A9FF;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 800;
    min-height: 46px;
    padding: 0.55rem 1rem;
    border: 1px solid rgba(125,170,255,.35);
    background: linear-gradient(110deg,#2868D8,#247FBF);
    color: #FFFFFF;
    transition: all .22s ease;
    box-shadow: 0 7px 20px rgba(36,91,190,.14);
}

div.stButton > button:hover {
    border-color: #A9CAFF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(65,112,220,.22);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg,rgba(20,36,65,.75),rgba(12,22,42,.88));
    border: 1px solid rgba(117,153,220,.18);
    border-radius: 17px;
}

.link-panel {
    background: linear-gradient(120deg,rgba(24,47,88,.88),rgba(19,27,57,.94));
    border: 1px solid rgba(112,157,255,.25);
    border-radius: 20px;
    padding: 25px;
}

.link-footer {
    text-align: center;
    color: #8296B8;
    font-size: .76rem;
    padding: 25px 0 10px;
    border-top: 1px solid rgba(120,155,220,.16);
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
    '<div class="link-eyebrow">SCAMSHIELD AI / URL INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="link-title">Link <span>Safety Intelligence.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="link-description">'
    'Inspect suspicious website addresses, identify common URL warning '
    'signs and make more informed decisions before clicking.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("URL ANALYSIS  /  THREAT AWARENESS  /  DIGITAL PROTECTION")

st.divider()


# =========================================================
# OVERVIEW
# =========================================================

st.subheader("🛡️ Inspection Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Protection Mode", "URL Analysis")

with col2:
    st.metric("Inspection Type", "Rule-Based")

with col3:
    st.metric("Website Access", "Not Opened")

st.divider()


# =========================================================
# URL SCANNER
# =========================================================

st.subheader("🔍 Suspicious Link Scanner")

st.write(
    "Enter a suspicious URL below. ScamShield will inspect "
    "its structure for common warning indicators without "
    "opening the destination website."
)

with st.container(border=True):

    st.markdown("### 🌐 URL Inspection")

    url = st.text_input(
        "Enter a suspicious URL",
        placeholder="https://example.com"
    )

    check_clicked = st.button(
        "🔍 Analyse URL",
        type="primary",
        use_container_width=True
    )


# =========================================================
# ANALYSIS
# =========================================================

if check_clicked:

    if not url.strip():

        st.warning("Please enter a URL to analyse.")

    else:

        result = check_url(url)

        st.divider()
        st.subheader("📊 Analysis Results")

        if not result["valid"]:

            st.error(
                result["findings"][0]
            )

        else:

            with st.container(border=True):

                st.markdown("#### 🌐 Domain Information")

                st.info(
                    f"Detected domain: {result['hostname']}"
                )

                if result["findings"]:

                    st.markdown("#### ⚠️ Warning Indicators")

                    for finding in result["findings"]:
                        st.warning(finding)

                    st.error(
                        "Caution: This URL contains one or more "
                        "characteristics that deserve further checking."
                    )

                else:

                    st.success(
                        "No basic URL warning indicators detected."
                    )

                st.info(
                    "This is a basic rule-based URL inspection, "
                    "not a malware scan or safety certification. "
                    "A URL with no detected warning signs may still "
                    "be dangerous. Do not visit unfamiliar links "
                    "just because they pass these checks."
                )


# =========================================================
# DIGITAL LINK SAFETY CENTRE
# =========================================================

st.divider()

st.subheader("🔐 Digital Link Safety Centre")

st.write(
    "Follow these essential practices before interacting "
    "with unfamiliar websites."
)

tip1, tip2 = st.columns(2)

with tip1:

    with st.container(border=True):

        st.markdown("### 🌐 Verify the Domain")

        st.write(
            "Check the spelling of website domains. "
            "Look for unexpected characters or misleading names."
        )

    with st.container(border=True):

        st.markdown("### 🔑 Protect Your Credentials")

        st.write(
            "Never enter OTPs, passwords or banking details "
            "on unfamiliar websites."
        )

with tip2:

    with st.container(border=True):

        st.markdown("### 🚫 Avoid Unexpected Links")

        st.write(
            "Be careful with unexpected messages containing "
            "login, payment or reward links."
        )

    with st.container(border=True):

        st.markdown("### 🏦 Use Official Websites")

        st.write(
            "Open trusted services through their official apps "
            "or manually typed website addresses."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="link-footer">'
    'SCAMSHIELD AI  •  LINK SAFETY INTELLIGENCE'
    '<br>EXPERIMENTAL EDUCATIONAL CYBERSECURITY TOOL'
    '</div>',
    unsafe_allow_html=True
)
