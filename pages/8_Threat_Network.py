
import streamlit as st

from modules.ui_theme import apply_theme
from modules.threat_database import (
    add_report,
    get_reports,
    get_report_stats,
    find_similar_reports
)

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Threat Network | ScamShield AI",
    page_icon="🌐",
    layout="wide"
)

apply_theme()

# ==================================================
# PREMIUM NAVY + ELECTRIC BLUE DESIGN
# ==================================================

st.markdown("""
<style>
.block-container {
    max-width: 1400px;
    padding: 2rem 2rem 3rem;
}

.stApp {
    background:
        radial-gradient(ellipse at 5% 0%, rgba(65,120,255,.14), transparent 33%),
        radial-gradient(ellipse at 95% 5%, rgba(30,170,220,.09), transparent 30%),
        linear-gradient(145deg,#061326,#081B31 55%,#061326);
    color: #EAF0FF;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#0B1427,#080F1D);
    border-right: 1px solid rgba(120,155,220,.16);
}

section[data-testid="stSidebar"] * {
    color: #DCE7FF;
}

h1, h2, h3 {
    color: #F1F5FF !important;
    letter-spacing: -.6px;
}

p, label, li {
    color: #AABBD7;
    line-height: 1.8;
}

.network-hero {
    background:
        radial-gradient(ellipse at 90% 0%,rgba(65,140,255,.18),transparent 55%),
        linear-gradient(120deg,#102746,#0D1D36);
    border: 1px solid rgba(117,153,220,.23);
    border-radius: 23px;
    padding: 36px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.hero-kicker {
    color: #91B9FF;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.hero-title {
    color: #F4F7FF;
    font-size: clamp(2rem,4vw,3.1rem);
    font-weight: 900;
    letter-spacing: -1.8px;
    line-height: 1.15;
    margin-bottom: 15px;
}

.hero-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    color: #A5B5D1;
    font-size: .92rem;
    line-height: 1.9;
    max-width: 800px;
}

.network-card {
    background: linear-gradient(120deg,rgba(24,47,88,.88),rgba(13,31,57,.96));
    border: 1px solid rgba(112,157,255,.25);
    border-radius: 17px;
    padding: 22px 24px;
    margin: 18px 0 24px;
    color: #DCE7FF;
    line-height: 1.9;
}

.network-card strong {
    color: #A9CCFF;
    font-size: 1rem;
}

.section-kicker {
    color: #91B9FF;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 9px;
}

div[data-testid="stMetric"] {
    background: linear-gradient(145deg,rgba(22,39,70,.96),rgba(12,22,42,.98));
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 17px;
    padding: 20px;
}

div[data-testid="stMetricValue"] {
    color: #72B7FF !important;
    font-weight: 800;
}

div[data-testid="stMetricLabel"] {
    color: #AABBD7 !important;
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(110deg,#2868D8,#247FBF);
    color: #FFFFFF;
    border: 1px solid rgba(125,170,255,.4);
    border-radius: 12px;
    font-weight: 800;
    min-height: 46px;
    transition: all .22s ease;
}

div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] button:hover {
    border-color: #A9CAFF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(65,112,220,.22);
}

div[data-testid="stTextArea"] textarea {
    background: #0D1D36;
    color: #EAF0FF;
    border: 1px solid rgba(117,153,220,.25);
    border-radius: 12px;
}

div[data-testid="stSelectbox"] > div > div {
    background: #0D1D36;
    border-color: rgba(117,153,220,.25);
    border-radius: 11px;
}

div[data-testid="stCheckbox"] label {
    color: #C5D5F0;
}

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg,#2868D8,#55B9FF);
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

div[data-testid="stVegaLiteChart"],
div[data-testid="stArrowVegaLiteChart"] {
    background: rgba(13,29,54,.55);
    border: 1px solid rgba(117,153,220,.15);
    border-radius: 15px;
    padding: 10px;
}

hr {
    border-color: rgba(120,155,220,.16);
}

.network-footer {
    text-align: center;
    color: #8296B8;
    font-size: .76rem;
    letter-spacing: 1.3px;
    line-height: 2;
    padding: 25px 0 10px;
    border-top: 1px solid rgba(120,155,220,.16);
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("## 🌐 Threat Network")
    st.caption("SCAMSHIELD AI / COMMUNITY INTELLIGENCE")

    st.divider()

    st.page_link("app.py", label="← Back to Command Centre")

    st.divider()

    st.markdown("### NETWORK MODULES")
    st.caption("Local threat database")
    st.caption("Community reporting")
    st.caption("Pattern similarity")

    st.divider()

    st.markdown("### DATA PRIVACY")
    st.caption("Reports stored locally.")
    st.caption("No automatic external sharing.")


# ==================================================
# HEADER
# ==================================================

st.markdown("""
<div class="network-hero">
    <div class="hero-kicker">SCAMSHIELD AI / COMMUNITY INTELLIGENCE</div>
    <div class="hero-title">Threat Intelligence <span>Network.</span></div>
    <div class="hero-description">
        Connect suspicious patterns, build local awareness
        and understand emerging digital threats through
        anonymised community incident reporting.
    </div>
</div>

<div class="network-card">
    <strong>🌐 Privacy-first community intelligence</strong><br>
    Contribute a carefully anonymised description of a suspicious
    communication. Reports are stored locally on this computer.
</div>
""", unsafe_allow_html=True)


# ==================================================
# NETWORK STATUS
# ==================================================

st.markdown('<div class="section-kicker">01 / SYSTEM STATUS</div>',
            unsafe_allow_html=True)

st.subheader("Network Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("DATABASE", "CONNECTED")

with col2:
    st.metric("REPORT SYSTEM", "ACTIVE")

with col3:
    st.metric("STORAGE", "LOCAL")

st.info(
    "This is a local prototype. Reports are not automatically "
    "shared with other users, uploaded to a central server, "
    "or sent to cyber authorities."
)


# ==================================================
# ANALYTICS
# ==================================================

st.divider()

st.markdown('<div class="section-kicker">02 / NETWORK ANALYTICS</div>',
            unsafe_allow_html=True)

st.subheader("📊 Network Analytics")

stats = get_report_stats()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("TOTAL REPORTS", stats["total"])

with col2:
    st.metric("THREAT CATEGORIES", len(stats["categories"]))

with col3:
    st.metric("CHANNELS TRACKED", len(stats["channels"]))

left, right = st.columns(2)

with left:

    st.markdown("#### Threat Category Distribution")

    if stats["categories"]:
        st.bar_chart(stats["categories"])

    else:
        st.info("Category analytics will appear after reports are submitted.")

with right:

    st.markdown("#### Communication Channels")

    if stats["channels"]:
        st.bar_chart(stats["channels"])

    else:
        st.info("Channel analytics will appear after reports are submitted.")


# ==================================================
# NETWORK INSIGHTS
# ==================================================

st.divider()

st.markdown('<div class="section-kicker">03 / INTELLIGENCE INSIGHTS</div>',
            unsafe_allow_html=True)

st.subheader("🧠 Network Insights")

if stats["total"] > 0:

    most_reported = max(
        stats["categories"],
        key=stats["categories"].get
    ) if stats["categories"] else "Not available"

    col1, col2 = st.columns(2)

    with col1:
        st.metric("MOST REPORTED CATEGORY", most_reported)

    with col2:
        st.metric("LOCAL INCIDENT RECORDS", stats["total"])

else:

    st.info(
        "The network is ready. Submit a sample report "
        "to begin building local intelligence."
    )


# ==================================================
# REPORT SUBMISSION
# ==================================================

st.divider()

st.markdown('<div class="section-kicker">04 / COMMUNITY REPORTING</div>',
            unsafe_allow_html=True)

st.subheader("📡 Contribute to the Threat Network")

st.write(
    "Share a short description of the suspicious behaviour. "
    "Do not paste the original private message or call transcript."
)

st.warning(
    "Never include names, phone numbers, OTPs, passwords, "
    "UPI PINs, bank details, addresses, email addresses "
    "or other identifying information."
)

with st.form("threat_report_form"):

    channel = st.selectbox(
        "COMMUNICATION CHANNEL",
        ["SMS", "Phone Call", "WhatsApp", "Website / Link", "Other"]
    )

    category = st.selectbox(
        "THREAT CATEGORY",
        [
            "Phishing",
            "Impersonation",
            "UPI / Payment Fraud",
            "Fake Reward",
            "Remote Access Request",
            "Threatening / Pressure Tactics",
            "Suspicious Link",
            "Other"
        ]
    )

    description = st.text_area(
        "ANONYMISED INCIDENT SUMMARY",
        max_chars=300,
        placeholder=(
            "Example: A caller claimed to represent a bank "
            "and requested a one-time verification code."
        )
    )

    consent = st.checkbox(
        "I have checked this summary and confirm it contains "
        "no personal or sensitive information."
    )

    submitted = st.form_submit_button(
        "🌐 SUBMIT TO LOCAL NETWORK",
        use_container_width=True
    )


# ==================================================
# PROCESS REPORT
# ==================================================

if submitted:

    if not description.strip():

        st.error("Please enter an incident summary.")

    elif not consent:

        st.error("Please confirm that the summary is safe to share.")

    else:

        try:

            similar_reports = find_similar_reports(
                channel,
                category,
                description
            )

            report_id = add_report(
                channel,
                category,
                description
            )

            if report_id is None:

                st.warning("This exact report already exists.")

            else:

                st.success(
                    f"Report #{report_id} saved to this computer."
                )

                if similar_reports:

                    st.subheader("🔎 Possible Related Patterns")

                    st.caption(
                        "Text similarity is experimental. "
                        "It does not prove that incidents are connected."
                    )

                    for match in similar_reports:

                        with st.expander(
                            f"Report #{match['id']} — "
                            f"{match['similarity']}% text similarity"
                        ):

                            st.write(match["description"])

                            st.progress(
                                max(
                                    0,
                                    min(
                                        100,
                                        int(match["similarity"])
                                    )
                                )
                            )

                st.rerun()

        except Exception as error:

            st.error("Report processing failed.")
            st.code(str(error))


# ==================================================
# RECENT REPORTS
# ==================================================

st.divider()

st.markdown('<div class="section-kicker">05 / LOCAL THREAT RECORDS</div>',
            unsafe_allow_html=True)

st.subheader("📋 Recent Threat Records")

reports = get_reports(10)

if reports:

    for report in reports:

        with st.expander(
            f"REPORT #{report['id']}  |  {report['category']}"
        ):

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**CHANNEL**")
                st.write(report["channel"])

            with col2:
                st.markdown("**CATEGORY**")
                st.write(report["category"])

            st.markdown("**INCIDENT SUMMARY**")
            st.write(report["description"])

            st.caption("Saved: " + report["created_at"])

else:

    st.info("No reports have been submitted yet.")


# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown("""
<div class="network-footer">
    🌐 SCAMSHIELD AI — THREAT INTELLIGENCE NETWORK
    <br>
    COMMUNITY AWARENESS • PRIVACY • DIGITAL SAFETY
    <br>
    <small>Experimental educational cybersecurity prototype</small>
</div>
""", unsafe_allow_html=True)
