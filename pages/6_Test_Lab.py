
import streamlit as st
from modules.ui_theme import apply_theme
from modules.scam_dna import analyse_scam_dna
from modules.language_support import detect_language

st.set_page_config(
    page_title="ScamShield AI | Research Lab",
    page_icon="🧪",
    layout="wide"
)
apply_theme()
# =========================================================
# PREMIUM NAVY + ELECTRIC BLUE THEME
# =========================================================

st.markdown("""
<style>
.block-container {
    max-width: 1450px;
    padding: 2rem 2rem 3rem;
}

.stApp {
    background:
        radial-gradient(ellipse at 85% 0%, rgba(65,120,255,.14), transparent 35%),
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

.lab-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.lab-title {
    color: #F4F7FF;
    font-size: clamp(2rem, 4vw, 3.3rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
}

.lab-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF,#A4C9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.lab-description {
    color: #A5B5D1;
    font-size: .9rem;
    line-height: 1.8;
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

div.stButton > button {
    background: linear-gradient(110deg,#2868D8,#247FBF);
    color: #FFFFFF;
    border: 1px solid rgba(125,170,255,.4);
    border-radius: 12px;
    font-weight: 800;
    min-height: 46px;
    transition: all .22s ease;
    box-shadow: 0 7px 20px rgba(36,91,190,.14);
}

div.stButton > button:hover {
    border-color: #A9CAFF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(65,112,220,.22);
}

div[data-testid="stTextArea"] textarea {
    background: #0C1B32;
    color: #EAF0FF;
    border: 1px solid rgba(100,157,255,.3);
    border-radius: 13px;
}

div[data-testid="stTextArea"] textarea:focus {
    border-color: #64A8FF;
    box-shadow: 0 0 0 1px #64A8FF;
}

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
}

div[data-testid="stProgressBar"] {
    background: #172943;
    border-radius: 20px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg,#2868D8,#72D9FF);
    border-radius: 20px;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

hr {
    border-color: rgba(120,155,220,.16);
}

.lab-footer {
    text-align: center;
    color: #8296B8;
    font-size: .76rem;
    letter-spacing: 1.5px;
    padding: 25px 0 10px;
    border-top: 1px solid rgba(120,155,220,.16);
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# TEST DATA
# =========================================================

tests = [
    {
        "name": "English scam sample",
        "message": "Congratulations! You won a prize. Click this link and pay a processing fee immediately.",
        "language": "English",
        "indicators": [
            "Urgency",
            "Payment pressure",
            "Prize or reward claim",
            "Suspicious link language"
        ]
    },
    {
        "name": "Hindi scam sample",
        "message": "बधाई हो! आपने इनाम जीता है। तुरंत इस लिंक पर क्लिक करें और प्रोसेसिंग फीस जमा करें।",
        "language": "Hindi",
        "indicators": [
            "Urgency",
            "Payment pressure",
            "Prize or reward claim",
            "Suspicious link language"
        ]
    },
    {
        "name": "Hinglish scam sample",
        "message": "Congratulations! Aapne prize jeeta hai. Turant is link par click karo aur processing fee pay karo.",
        "language": "Hinglish",
        "indicators": [
            "Urgency",
            "Payment pressure",
            "Prize or reward claim",
            "Suspicious link language"
        ]
    },
    {
        "name": "Harmless Hinglish sample",
        "message": "Kal school ke baad library mein milte hain. Main apne notes bhi le aaunga.",
        "language": "Hinglish",
        "indicators": []
    },
    {
        "name": "Harmless English sample",
        "message": "I will meet you at the library after school tomorrow.",
        "language": "English",
        "indicators": []
    }
]


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="lab-eyebrow">SCAMSHIELD AI / RESEARCH DIVISION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lab-title">AI <span>Research Lab.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="lab-description">'
    'System testing, intelligence validation and diagnostic analysis. '
    'An experimental environment for evaluating ScamShield capabilities.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("LABORATORY / SYSTEM DIAGNOSTICS / EXPERIMENTAL ENVIRONMENT")

st.divider()


# =========================================================
# LAB OVERVIEW
# =========================================================

st.subheader("⚡ Laboratory Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("TEST SCENARIOS", len(tests))

with col2:
    st.metric("LANGUAGE MODES", "03")

with col3:
    st.metric("ENGINE STATUS", "ACTIVE")


# =========================================================
# TEST CONTROL
# =========================================================

st.divider()

st.subheader("🖥️ Testing Control Centre")

st.write(
    "Execute the predefined test suite to evaluate "
    "language detection and suspicious-pattern identification."
)

run_tests = st.button(
    "▶ EXECUTE ALL TESTS",
    type="primary",
    use_container_width=True
)

if run_tests:

    passed = 0
    results = []

    for test in tests:

        language = detect_language(test["message"])
        dna = analyse_scam_dna(test["message"])

        language_ok = language == test["language"]

        indicators_ok = (
            set(dna["findings"]) == set(test["indicators"])
        )

        success = language_ok and indicators_ok

        if success:
            passed += 1

        results.append({
            "name": test["name"],
            "expected_language": test["language"],
            "detected_language": language,
            "expected_indicators": test["indicators"],
            "detected_indicators": dna["findings"],
            "success": success
        })

    st.session_state["test_lab_results"] = results
    st.session_state["test_lab_passed"] = passed


# =========================================================
# TEST REPORT
# =========================================================

if "test_lab_results" in st.session_state:

    results = st.session_state["test_lab_results"]
    passed = st.session_state["test_lab_passed"]
    total = len(results)

    st.divider()

    st.subheader("📊 System Performance Report")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("TOTAL TESTS", total)

    with col2:
        st.metric("PASSED", passed)

    with col3:
        st.metric("NEEDS REVIEW", total - passed)

    pass_rate = (passed / total) * 100 if total else 0

    st.markdown("### Test Completion Performance")

    st.progress(pass_rate / 100)

    st.write(f"**Measured test pass rate: {pass_rate:.1f}%**")

    if passed == total:
        st.success("ALL PREDEFINED TESTS PASSED")

    elif passed > 0:
        st.warning("Some test cases require further review.")

    else:
        st.error("All test cases require review.")

    st.divider()

    st.subheader("🔬 Individual Diagnostic Results")

    for result in results:

        with st.expander(result["name"]):

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**Expected Language**")
                st.write(result["expected_language"])

            with col2:
                st.markdown("**Detected Language**")
                st.write(result["detected_language"])

            st.markdown("**Expected Indicators**")
            st.write(result["expected_indicators"])

            st.markdown("**Detected Indicators**")
            st.write(result["detected_indicators"])

            if result["success"]:
                st.success("✓ TEST PASSED")
            else:
                st.warning("⚠ REVIEW REQUIRED")

    st.info(
        "This report evaluates five predefined functional examples. "
        "It does not measure real-world fraud detection accuracy."
    )

else:

    st.info(
        "LAB READY — Execute the test suite to generate a report."
    )


# =========================================================
# CUSTOM ANALYSIS
# =========================================================

st.divider()

st.subheader("🧬 Custom Intelligence Testing")

st.write(
    "Enter a sample message to inspect the language "
    "and suspicious patterns identified by the system."
)

custom_message = st.text_area(
    "MESSAGE INPUT TERMINAL",
    placeholder="Enter an English, Hindi or Hinglish message...",
    height=150
)

analyse_clicked = st.button(
    "🔍 ANALYSE INPUT",
    use_container_width=True
)

if analyse_clicked:

    if not custom_message.strip():

        st.warning("Enter a message before starting analysis.")

    else:

        language = detect_language(custom_message)
        dna = analyse_scam_dna(custom_message)

        st.divider()

        st.subheader("📋 Analysis Output")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("DETECTED LANGUAGE", language)

        with col2:
            st.metric(
                "WARNING INDICATORS",
                dna["risk_indicators_count"]
            )

        if dna["findings"]:

            st.markdown("### ⚠️ Identified Patterns")

            for item in dna["explanations"]:

                with st.expander(item["indicator"]):

                    st.write(item["explanation"])

                    phrases = dna["matched_phrases"].get(
                        item["indicator"], []
                    )

                    if phrases:

                        st.markdown("**Matched phrases**")

                        for phrase in phrases:
                            st.code(phrase)

        else:

            st.success(
                "No known warning patterns were identified. "
                "This does not guarantee that the message is safe."
            )

        st.info(
            "This is an experimental rule-based analysis, "
            "not a definitive fraud assessment."
        )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="lab-footer">'
    'SCAMSHIELD AI • RESEARCH LAB • RESPONSIBLE CYBERSECURITY'
    '</div>',
    unsafe_allow_html=True
)
