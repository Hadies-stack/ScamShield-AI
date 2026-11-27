
import streamlit as st
import json
import html

from modules.threat_engine import analyse_threat
from modules.sms_classifier import predict_sms


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Threat Intelligence | ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)


# =========================================================
# PREMIUM NAVY + ELECTRIC BLUE THEME
# =========================================================

st.markdown("""
<style>

.block-container {
    max-width: 1350px;
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

.threat-hero {
    background:
        radial-gradient(ellipse at 90% 0%,rgba(65,140,255,.18),transparent 55%),
        linear-gradient(120deg,#102746,#0D1D36);
    border: 1px solid rgba(117,153,220,.23);
    border-radius: 23px;
    padding: 36px;
    margin-bottom: 25px;
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
    max-width: 780px;
}

.info-card {
    background: linear-gradient(120deg,rgba(24,47,88,.88),rgba(13,31,57,.96));
    border: 1px solid rgba(112,157,255,.25);
    border-radius: 17px;
    padding: 21px 24px;
    margin: 18px 0 24px;
    color: #DCE7FF;
    line-height: 1.9;
}

.info-card strong {
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

/* METRIC CARDS */

div[data-testid="stMetric"] {
    background: linear-gradient(145deg,rgba(22,39,70,.96),rgba(12,22,42,.98));
    border: 1px solid rgba(117,153,220,.25);
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

/* BUTTONS */

div.stButton > button {
    background: linear-gradient(110deg,#2868D8,#247FBF);
    color: #FFFFFF;
    border: 1px solid rgba(125,170,255,.4);
    border-radius: 12px;
    font-weight: 800;
    min-height: 46px;
    transition: all .22s ease;
}

div.stButton > button:hover {
    border-color: #A9CAFF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(65,112,220,.22);
}

/* INPUTS */

div[data-testid="stTextArea"] textarea {
    background: #0D1D36;
    color: #EAF0FF;
    border: 1px solid rgba(117,153,220,.25);
    border-radius: 12px;
}

div[data-testid="stSelectbox"] > div > div,
div[data-testid="stMultiSelect"] > div > div {
    background: #0D1D36;
    border-color: rgba(117,153,220,.25);
    border-radius: 11px;
}

div[role="radiogroup"] {
    background: rgba(15,32,58,.7);
    border: 1px solid rgba(117,153,220,.18);
    border-radius: 13px;
    padding: 12px 15px;
}

/* PREMIUM OUTPUT EXPANDERS */

div[data-testid="stExpander"] {
    background: linear-gradient(145deg,#102746,#0B1B32) !important;
    border: 1px solid rgba(100,157,255,.32) !important;
    border-radius: 14px !important;
    overflow: hidden;
}

div[data-testid="stExpander"] summary {
    background: linear-gradient(110deg,#142F53,#102746) !important;
    color: #DCEAFF !important;
}

div[data-testid="stExpander"] summary p {
    color: #C8DCFF !important;
    font-weight: 700 !important;
}

div[data-testid="stExpander"] details {
    background: transparent !important;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

/* CUSTOM RESULT DATA PANELS */

.result-data {
    background: linear-gradient(145deg,#102746,#0B1B32);
    border: 1px solid rgba(100,157,255,.28);
    border-radius: 12px;
    padding: 18px;
    color: #BBD5FF;
    font-family: Consolas, monospace;
    font-size: 13px;
    line-height: 1.8;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    margin: 8px 0 14px;
}

.finding-card {
    background: linear-gradient(120deg,rgba(24,47,88,.88),rgba(13,31,57,.96));
    border: 1px solid rgba(112,157,255,.25);
    border-radius: 13px;
    padding: 16px 19px;
    margin: 10px 0;
    color: #DCE7FF;
}

.finding-title {
    color: #A9CCFF;
    font-weight: 800;
    margin-bottom: 6px;
}

.finding-description {
    color: #AABBD7;
    font-size: .86rem;
    line-height: 1.8;
}

.threat-footer {
    text-align: center;
    color: #8296B8;
    font-size: .76rem;
    letter-spacing: 1.3px;
    padding: 25px 0 10px;
    border-top: 1px solid rgba(120,155,220,.16);
}

hr {
    border-color: rgba(120,155,220,.16);
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# REUSABLE OUTPUT HELPER
# =========================================================

def render_data_panel(value):

    formatted = json.dumps(
        value,
        indent=2,
        ensure_ascii=False
    )

    safe_content = html.escape(formatted)

    st.markdown(
        f'<div class="result-data">{safe_content}</div>',
        unsafe_allow_html=True
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🛡️ Threat Intelligence")
    st.caption("SCAMSHIELD AI / DIGITAL PROTECTION")

    st.divider()

    st.page_link("app.py", label="← Back to Command Centre")

    st.divider()

    st.markdown("### PROTECTION MODES")
    st.caption("SMS Threat Analysis")
    st.caption("Guided Call Intelligence")

    st.divider()

    st.markdown("### PRIVACY")
    st.caption("User-submitted information only.")
    st.caption("No automatic phone monitoring.")


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="threat-hero">
    <div class="hero-kicker">SCAMSHIELD AI / THREAT DETECTION SYSTEM</div>
    <div class="hero-title">Threat Intelligence <span>Centre.</span></div>
    <div class="hero-description">
        Understand suspicious messages and caller behaviour.
        Identify potential warning signs, examine risk indicators
        and make more informed digital safety decisions.
    </div>
</div>

<div class="info-card">
    <strong>🛡️ Privacy-first protection</strong><br>
    Analyse suspicious messages or describe a call manually.
    ScamShield does not access your phone, read incoming SMS,
    record calls or intercept communications.
</div>
""", unsafe_allow_html=True)


# =========================================================
# MODE SELECTION
# =========================================================

st.markdown(
    '<div class="section-kicker">01 / SELECT ANALYSIS MODE</div>',
    unsafe_allow_html=True
)

st.subheader("What would you like to check?")

mode = st.radio(
    "Choose analysis type",
    ["📩 SMS Protection", "📞 Call Intelligence"],
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()


# =========================================================
# INPUT COLLECTION
# =========================================================

message = ""

if mode == "📩 SMS Protection":

    st.markdown(
        '<div class="section-kicker">02 / MESSAGE SCANNER</div>',
        unsafe_allow_html=True
    )

    st.subheader("📩 Analyse a suspicious SMS")

    st.write(
        "Copy the suspicious message from your phone "
        "and paste it below."
    )

    message = st.text_area(
        "SMS message",
        placeholder=(
            "Example: Your bank account will be blocked. "
            "Verify your details immediately..."
        ),
        height=180,
        key="sms_message"
    )

    st.caption(
        "Remove personal details such as account numbers, "
        "phone numbers and OTPs before submitting."
    )

else:

    st.markdown(
        '<div class="section-kicker">02 / CALL BEHAVIOUR ANALYSIS</div>',
        unsafe_allow_html=True
    )

    st.subheader("📞 Guided Call Intelligence")

    st.write(
        "Select the things the caller said or asked you to do. "
        "You do not need to record or upload the call."
    )

    caller_type = st.selectbox(
        "Who did the caller claim to be?",
        [
            "Select an option",
            "Bank employee",
            "Government official",
            "Police or investigation officer",
            "Courier or delivery agent",
            "Customer support representative",
            "Job recruiter",
            "Unknown person",
            "Other"
        ]
    )

    warning_signs = st.multiselect(
        "What happened during the call?",
        [
            "Asked for an OTP",
            "Asked for UPI PIN or banking password",
            "Demanded an immediate payment",
            "Threatened account suspension or legal action",
            "Promised a prize, refund or reward",
            "Asked me to install an application",
            "Asked me to share my screen",
            "Sent a suspicious link",
            "Claimed to be from a bank or government department",
            "Asked for personal or financial information",
            "None of these"
        ]
    )

    extra_details = st.text_area(
        "Anything else you remember? (Optional)",
        placeholder=(
            "Example: The caller said my bank account "
            "would be blocked unless I verified it."
        ),
        height=130
    )

    parts = []

    if caller_type != "Select an option":
        parts.append("Caller claimed to be: " + caller_type)

    if warning_signs:
        parts.append(
            "Call warning signs: " + ", ".join(warning_signs)
        )

    if extra_details.strip():
        parts.append("Additional details: " + extra_details.strip())

    message = "\n".join(parts)


# =========================================================
# ANALYSIS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-kicker">03 / AI THREAT ANALYSIS</div>',
    unsafe_allow_html=True
)

if st.button("🔍 Analyse Threat", use_container_width=True):

    if not message.strip():

        st.warning(
            "Please enter an SMS or select/describe at least "
            "one call detail before analysing."
        )

    else:

        with st.spinner("ScamShield AI is analysing the information..."):

            try:

                channel = (
                    "SMS"
                    if mode == "📩 SMS Protection"
                    else "CALL"
                )

                result = analyse_threat(
                    message.strip(),
                    channel=channel
                )

                ml_result = None
                ml_error = None

                if channel == "SMS":
                    try:
                        ml_result = predict_sms(message.strip())
                    except Exception as error:
                        ml_error = str(error)

                st.session_state["latest_threat_result"] = result
                st.session_state["latest_threat_ml"] = ml_result
                st.session_state["latest_threat_ml_error"] = ml_error
                st.session_state["latest_threat_channel"] = channel

            except Exception as error:

                st.error("Analysis could not be completed.")
                st.code(str(error))


# =========================================================
# RESULTS
# =========================================================

if "latest_threat_result" in st.session_state:

    result = st.session_state["latest_threat_result"]
    ml_result = st.session_state.get("latest_threat_ml")
    ml_error = st.session_state.get("latest_threat_ml_error")
    result_channel = st.session_state.get("latest_threat_channel")

    st.divider()

    st.markdown(
        '<div class="section-kicker">04 / ANALYSIS REPORT</div>',
        unsafe_allow_html=True
    )

    st.header("📊 Threat Analysis Results")

    if isinstance(result, dict):

        # ---------------------------------------------
        # FRAUD RISK
        # ---------------------------------------------

        risk = result.get("risk", {})

        if isinstance(risk, dict):

            risk_score = risk.get("score")
            risk_level = risk.get("level")
            risk_explanation = risk.get("explanation")

            col1, col2 = st.columns(2)

            with col1:
                if risk_score is not None:
                    st.metric(
                        "Fraud Risk Score",
                        f"{risk_score}/100"
                    )

            with col2:
                if risk_level is not None:
                    st.metric(
                        "Fraud Risk Level",
                        risk_level
                    )

            if risk_explanation:
                st.markdown(
                    f"""
                    <div class="info-card">
                        <strong>Risk explanation</strong><br>
                        {html.escape(str(risk_explanation))}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        # ---------------------------------------------
        # MACHINE LEARNING CLASSIFICATION
        # ---------------------------------------------

        if result_channel == "SMS":

            st.subheader("🤖 ML SMS Classification")

            if ml_result:

                ml_col1, ml_col2 = st.columns(2)

                with ml_col1:
                    st.metric(
                        "Spam Probability",
                        f"{ml_result['spam_probability']:.2f}%"
                    )

                with ml_col2:
                    st.metric(
                        "ML Prediction",
                        ml_result["prediction"].upper()
                    )

                if ml_result["prediction"] == "spam":
                    st.warning(
                        "The ML model classified this message as "
                        "spam-like. This is an estimate, not proof of fraud."
                    )
                else:
                    st.success(
                        "The ML model classified this message as "
                        "likely legitimate. This does not guarantee safety."
                    )

                st.caption(ml_result["disclaimer"])

            elif ml_error:

                st.warning(
                    "ML classification is unavailable. "
                    "Rule-based analysis is still available."
                )

                st.caption(ml_error)

        # ---------------------------------------------
        # FINDINGS
        # ---------------------------------------------

        st.subheader("Detailed Findings")

        findings = result.get("findings", [])

        if findings:

            for finding in findings:

                st.markdown(
                    f"""
                    <div class="finding-card">
                        <div class="finding-title">
                            ⚠️ {html.escape(str(finding))}
                        </div>
                        <div class="finding-description">
                            A matching warning pattern was identified.
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No known rule-based warning patterns were identified."
            )

        # ---------------------------------------------
        # EXPLANATIONS
        # ---------------------------------------------

        explanations = result.get("explanations", [])

        if explanations:

            with st.expander(
                "🔎 Indicator Explanations",
                expanded=True
            ):

                for item in explanations:

                    indicator = html.escape(
                        str(item.get("indicator", "Indicator"))
                    )

                    explanation = html.escape(
                        str(item.get("explanation", ""))
                    )

                    st.markdown(
                        f"""
                        <div class="finding-card">
                            <div class="finding-title">
                                {indicator}
                            </div>
                            <div class="finding-description">
                                {explanation}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

       
       
               # ---------------------------------------------
        # MATCHED PHRASES
        # ---------------------------------------------

        matched_phrases = result.get("matched_phrases", {})

        if matched_phrases:

            with st.expander(
                "🧩 Matched Phrases",
                expanded=True
            ):

                for category, phrases in matched_phrases.items():

                    if not phrases:
                        continue

                    phrase_list = (
                        phrases
                        if isinstance(phrases, list)
                        else [phrases]
                    )

                    phrase_html = "".join(
                        f'<div class="finding-description">'
                        f'• {html.escape(str(phrase))}'
                        f'</div>'
                        for phrase in phrase_list
                    )

                    st.markdown(
                        f"""
                        <div class="finding-card">
                            <div class="finding-title">
                                {html.escape(str(category))}
                            </div>
                            {phrase_html}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


        # ---------------------------------------------
        # OTHER DETAILS
        # ---------------------------------------------

        language = result.get("language")

        if language:
            st.caption(f"Detected language: {language}")

        disclaimer = result.get("disclaimer")

        if disclaimer:
            st.caption(disclaimer)

       # ---------------------------------------------
    # SAFETY ACTIONS
    # ---------------------------------------------

    st.divider()

    st.subheader("🛡️ Recommended Safety Actions")

    safety_actions = result.get("safety_actions", [])

    if safety_actions:

        for action in safety_actions:

            st.markdown(
                f"""
                <div class="finding-card">
                    <div class="finding-description">
                        🛡️ {html.escape(str(action))}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        default_actions = [
            "Never share your OTP, UPI PIN or banking password.",
            "Do not install applications at the request of unknown callers.",
            "Do not transfer money under pressure.",
            "Verify claims using official contact details.",
            "Do not open unexpected links."
        ]

        for action in default_actions:

            st.markdown(
                f"""
                <div class="finding-card">
                    <div class="finding-description">
                        🛡️ {html.escape(action)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "If you suspect financial cyber fraud in India, "
        "call 1930 promptly or visit https://cybercrime.gov.in/."
    )

# =========================================================
# PRIVACY AND LIMITATIONS
# =========================================================

st.divider()

st.markdown(
    '<div class="section-kicker">05 / TRANSPARENCY & PRIVACY</div>',
    unsafe_allow_html=True
)

with st.expander("🔐 Privacy, permissions and limitations"):

    st.markdown("""
    **ScamShield works through information you choose to submit.**

    - No automatic SMS reading.
    - No call interception or recording.
    - No access to your contacts.
    - No automatic phone monitoring.
    - You choose what information to analyse.

    **Machine Learning limitations:**

    - The ML model estimates SMS spam likelihood.
    - Spam does not automatically mean fraud.
    - A legitimate-looking message can still be unsafe.
    - Rule-based fraud indicators are shown separately.
    - Neither result guarantees that a message is safe or fraudulent.

    Analysis is experimental and may make mistakes.
    Always verify suspicious claims independently.
    """)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="threat-footer">'
    'SCAMSHIELD AI • THREAT INTELLIGENCE • DIGITAL PROTECTION'
    '</div>',
    unsafe_allow_html=True
)
