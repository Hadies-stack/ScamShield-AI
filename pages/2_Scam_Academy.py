
import streamlit as st
from modules.ui_theme import apply_theme

st.set_page_config(
    page_title="Scam Academy | ScamShield AI",
    page_icon="🎓",
    layout="wide"
)

apply_theme()

# =========================================================
# PREMIUM ACADEMY THEME
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

.academy-eyebrow {
    color: #91B9FF;
    font-size: .7rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 14px;
}

.academy-title {
    color: #F4F7FF;
    font-size: clamp(2.1rem, 4vw, 3.5rem);
    font-weight: 900;
    letter-spacing: -2px;
    line-height: 1.15;
    margin-bottom: 14px;
}

.academy-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.academy-description {
    color: #A5B5D1;
    font-size: .96rem;
    line-height: 1.9;
    max-width: 800px;
}

.academy-hero {
    background: linear-gradient(120deg,rgba(24,47,88,.88),rgba(20,43,76,.78));
    border: 1px solid rgba(117,153,220,.25);
    border-radius: 21px;
    padding: 28px;
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

div[data-testid="stRadio"] {
    background: rgba(17,31,56,.65);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
    padding: 14px;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 800;
    min-height: 46px;
    padding: .55rem 1rem;
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

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg,#2868D8,#72D9FF);
}

.academy-footer {
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
# QUIZ DATA
# =========================================================

questions = [
    {
        "question": "Someone asks for your OTP to receive a prize. What should you do?",
        "options": [
            "Share the OTP",
            "Ignore the request and verify independently",
            "Forward the OTP to a friend"
        ],
        "answer": "Ignore the request and verify independently",
        "explanation": "An OTP is private. Never share it with anyone, even someone claiming to represent an organisation.",
        "topic": "OTP Protection"
    },
    {
        "question": "You receive an unexpected UPI collect request. What should you do?",
        "options": [
            "Approve immediately",
            "Check the request and sender before taking action",
            "Share your UPI PIN"
        ],
        "answer": "Check the request and sender before taking action",
        "explanation": "Review unexpected payment requests carefully. A UPI PIN is used to authorise payments, so never share it.",
        "topic": "UPI Safety"
    },
    {
        "question": "A message says your bank account will be blocked unless you click a link. What is safest?",
        "options": [
            "Click the link immediately",
            "Reply with your bank details",
            "Contact the bank through its official app or website"
        ],
        "answer": "Contact the bank through its official app or website",
        "explanation": "Independent verification through official channels helps you avoid phishing attempts.",
        "topic": "Phishing Awareness"
    }
]


# =========================================================
# SESSION STATE
# =========================================================

if "academy_answers" not in st.session_state:
    st.session_state.academy_answers = {}

if "academy_checked" not in st.session_state:
    st.session_state.academy_checked = set()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="academy-eyebrow">SCAMSHIELD AI / CYBER LEARNING CENTRE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="academy-title">Scam <span>Academy.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="academy-description">'
    'Build practical cybersecurity awareness through interactive '
    'challenges, real-world examples and instant explanations.'
    '</div>',
    unsafe_allow_html=True
)

st.caption("LEARN SMART  /  THINK CRITICALLY  /  STAY PROTECTED")

st.divider()


# =========================================================
# HERO
# =========================================================

left, right = st.columns([2, 1])

with left:
    with st.container(border=True):
        st.markdown("### 🎓 Welcome to your Cyber Learning Hub")

        st.write(
            "Explore essential digital safety concepts, "
            "test your knowledge and learn how to recognise "
            "suspicious online behaviour."
        )

        st.info(
            "Your mission: Learn to recognise suspicious requests "
            "before they become a problem."
        )

with right:
    with st.container(border=True):
        st.markdown("## 🧠")

        st.markdown("### THINK BEFORE YOU CLICK")

        st.caption(
            "Knowledge is your first layer of digital protection."
        )


# =========================================================
# LEARNING OVERVIEW
# =========================================================

st.divider()

st.subheader("📚 Academy Overview")

correct_count = sum(
    1 for index, answer in st.session_state.academy_answers.items()
    if answer == questions[index]["answer"]
)

checked_count = len(st.session_state.academy_checked)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Learning Modules", "03")

with col2:
    st.metric("Questions Attempted", f"{checked_count}/3")

with col3:
    st.metric("Correct Answers", f"{correct_count}/3")


# =========================================================
# LEARNING MODULES
# =========================================================

st.divider()

st.subheader("🧩 Explore Learning Modules")

module1, module2, module3 = st.columns(3)

with module1:
    with st.container(border=True):
        st.markdown("### 🔐 OTP Protection")
        st.write("Understand why verification codes must remain private.")
        st.caption("MODULE 01")

with module2:
    with st.container(border=True):
        st.markdown("### 💳 UPI Awareness")
        st.write("Recognise unexpected payment requests and stay cautious.")
        st.caption("MODULE 02")

with module3:
    with st.container(border=True):
        st.markdown("### 🌐 Phishing Awareness")
        st.write("Learn how suspicious messages may pressure you to click.")
        st.caption("MODULE 03")


# =========================================================
# INTERACTIVE QUIZ
# =========================================================

st.divider()

st.subheader("🎯 Cyber Awareness Challenge")

st.write(
    "Answer all three questions and review the explanation "
    "after checking each answer."
)

for index, item in enumerate(questions):

    with st.container(border=True):

        st.caption(f"QUESTION {index + 1}  /  {item['topic']}")

        st.markdown(f"### {item['question']}")

        choice = st.radio(
            "Choose your answer:",
            item["options"],
            key=f"academy_question_{index}",
            index=None
        )

        if st.button(
            "Check Answer",
            key=f"academy_check_{index}",
            use_container_width=True
        ):

            if choice is None:
                st.warning("Please select an answer first.")

            else:
                st.session_state.academy_answers[index] = choice
                st.session_state.academy_checked.add(index)

        if index in st.session_state.academy_checked:

            selected = st.session_state.academy_answers[index]

            if selected == item["answer"]:

                st.success("Correct! " + item["explanation"])

            else:

                st.error("Not quite. " + item["explanation"])

                st.info(
                    "Correct answer: " + item["answer"]
                )


# =========================================================
# LEARNING PROGRESS
# =========================================================

st.divider()

st.subheader("📈 Your Learning Progress")

progress = checked_count / len(questions)

st.progress(progress)

st.write(
    f"Questions completed: **{checked_count} out of {len(questions)}**"
)

if checked_count == len(questions):

    st.success(
        f"Challenge completed! You answered "
        f"{correct_count} out of 3 questions correctly."
    )

    if correct_count == 3:
        st.balloons()
        st.markdown("### 🏆 Cyber Safety Champion!")

    else:
        st.info(
            "Review the explanations and try the challenge again "
            "to strengthen your awareness."
        )

else:

    st.info(
        "Complete all three questions to finish the challenge."
    )


# =========================================================
# RESET QUIZ
# =========================================================

if st.button("🔄 Restart Learning Challenge"):

    st.session_state.academy_answers = {}
    st.session_state.academy_checked = set()

    for index in range(len(questions)):
        st.session_state.pop(f"academy_question_{index}", None)

    st.rerun()


# =========================================================
# SAFETY REMINDER
# =========================================================

st.divider()

st.subheader("💡 Golden Cyber Safety Reminder")

st.warning(
    "Never share your OTP, UPI PIN or password. "
    "Pause, verify unexpected requests independently "
    "and never make payments under pressure."
)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="academy-footer">'
    'SCAMSHIELD AI  •  SCAM ACADEMY'
    '<br>LEARN TODAY. STAY SAFER TOMORROW.'
    '</div>',
    unsafe_allow_html=True
)
