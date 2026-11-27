
import textwrap
import streamlit as st
import urllib.request
import xml.etree.ElementTree as ET
import html
import re
from datetime import datetime

from modules.ui_theme import apply_theme


# =========================================================
# REUSABLE HTML HELPERS
# =========================================================

def render_html(content):
    st.html(textwrap.dedent(content).strip())


def section_heading(title, description):
    render_html(
        f"""
        <div class="section-heading">{html.escape(title)}</div>
        <div class="section-description">{html.escape(description)}</div>
        """
    )


def feature_card(icon, title, description):
    render_html(
        f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <div class="feature-title">{html.escape(title)}</div>
            <div class="feature-description">{html.escape(description)}</div>
        </div>
        """
    )


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ScamShield AI | Digital Protection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()


# =========================================================
# GLOBAL DESIGN SYSTEM
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #070B16;
    --surface: #0D1527;
    --surface-2: #111D33;
    --border: rgba(137, 169, 235, 0.14);
    --text: #EDF3FF;
    --muted: #91A3C2;
    --blue: #75AAFF;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 8% 0%, rgba(49, 104, 206, .17), transparent 34%),
        radial-gradient(ellipse at 92% 12%, rgba(30, 170, 220, .10), transparent 32%),
        linear-gradient(145deg, #070B16 0%, #090F1D 55%, #080C18 100%);
    color: var(--text);
}

/* MAIN LAYOUT */

.block-container {
    max-width: 1480px;
    padding: 2rem 2.5rem 4rem;
}

div[data-testid="stVerticalBlock"] {
    gap: 1rem;
}

hr {
    border-color: rgba(137, 169, 235, .13) !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0B1427 0%,
        #080F1D 100%
    );
    border-right: 1px solid rgba(120,155,220,0.16);
}

section[data-testid="stSidebar"] * {
    color: #DCE7FF;
}

section[data-testid="stSidebar"] div[data-testid="stPageLink"] a {
    border-radius: 11px;
    padding: 9px 12px;
    transition: all 0.2s ease;
}

section[data-testid="stSidebar"] div[data-testid="stPageLink"] a:hover {
    background: rgba(76,135,255,0.15);
    border: 1px solid rgba(100,157,255,0.2);
}

/* BRAND HEADER */

.hero-section {
    padding: 55px 24px 42px;
    text-align: center;
    position: relative;
    overflow: hidden;
    border-radius: 24px;
    background:
        radial-gradient(ellipse at 50% 0%,
        rgba(65,120,255,0.17), transparent 65%);
}

.hero-kicker {
    display: inline-block;
    color: #91B9FF;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 23px;
    padding: 9px 15px;
    border: 1px solid rgba(110,160,255,0.22);
    border-radius: 30px;
    background: rgba(50,100,190,0.10);
}

.hero-title {
    color: #F4F7FF;
    font-size: clamp(2.5rem,5vw,4.5rem);
    font-weight: 900;
    line-height: 1.12;
    letter-spacing: -2.5px;
    margin-bottom: 22px;
}

.hero-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-description {
    max-width: 680px;
    margin: 0 auto;
    color: #A5B5D1;
    font-size: 0.96rem;
    line-height: 1.9;
}

/* HERO FEATURE PANEL */

.hero-panel {
    background:
        radial-gradient(circle at 85% 8%, rgba(84, 135, 255, .19), transparent 38%),
        linear-gradient(145deg, rgba(22, 39, 72, .98), rgba(11, 20, 39, .98));
    border: 1px solid rgba(125, 166, 255, .25);
    border-radius: 24px;
    padding: 34px 27px;
    min-height: 390px;
    box-shadow:
        0 22px 65px rgba(0, 0, 0, .28),
        inset 0 1px 0 rgba(255, 255, 255, .045);
    position: relative;
    overflow: hidden;
}

.hero-panel::before {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: rgba(74, 132, 255, .15);
    filter: blur(65px);
    top: -95px;
    right: -75px;
}

.section-kicker {
    color: #91B9FF;
    font-size: .65rem;
    font-weight: 800;
    letter-spacing: 2px;
    position: relative;
}

.hero-shield {
    font-size: 4.5rem;
    text-align: center;
    margin: 30px 0 17px;
    filter: drop-shadow(0 0 25px rgba(87, 151, 255, .45));
    position: relative;
}

.hero-panel-title {
    color: #F1F5FF;
    font-size: 1.4rem;
    font-weight: 850;
    text-align: center;
    position: relative;
}

.hero-panel-description {
    color: #A8B9D8;
    font-size: .82rem;
    line-height: 1.85;
    text-align: center;
    margin: 13px auto 0;
    max-width: 390px;
    position: relative;
}

.capability-wrap {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 9px;
    margin-top: 23px;
    position: relative;
}

.capability {
    padding: 8px 12px;
    border-radius: 30px;
    font-size: .59rem;
    font-weight: 800;
    letter-spacing: .5px;
    background: rgba(77, 143, 255, .12);
    border: 1px solid rgba(105, 157, 255, .23);
    color: #B5D0FF;
}

.capability-purple {
    background: rgba(77, 143, 255, .12);
    border: 1px solid rgba(105, 157, 255, .23);
    color: #B5D0FF;
}

.panel-footer {
    margin-top: 24px;
    padding-top: 16px;
    border-top: 1px solid rgba(145, 170, 230, .16);
    color: #94ACDC;
    font-size: .62rem;
    font-weight: 800;
    letter-spacing: 1.8px;
    text-align: center;
    position: relative;
}

/* SECTION HEADINGS */

.section-heading {
    color: #F1F5FF;
    font-size: 1.75rem;
    font-weight: 900;
    letter-spacing: -0.8px;
    margin-top: 42px;
    margin-bottom: 9px;
}

.section-description {
    color: #9AACC9;
    font-size: 0.86rem;
    line-height: 1.8;
    margin-bottom: 25px;
    max-width: 760px;
}

.step-card {
    background: linear-gradient(
        145deg,
        rgba(20,36,65,0.95),
        rgba(12,22,42,0.98)
    );
    border: 1px solid rgba(117,153,220,0.18);
    border-radius: 17px;
    padding: 23px;
    min-height: 160px;
    transition: all 0.25s ease;
}

.step-card:hover {
    border-color: rgba(100,157,255,0.45);
    transform: translateY(-3px);
}

.step-number {
    color: #83B4FF;
    font-size: 0.68rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 13px;
}

.step-title {
    color: #EDF3FF;
    font-size: 1rem;
    font-weight: 800;
    margin-bottom: 9px;
}

.step-description {
    color: #9AACC9;
    font-size: 0.81rem;
    line-height: 1.8;
}

/* FEATURE CARDS */

.feature-card {
    background: linear-gradient(
        145deg,
        rgba(22,39,70,0.96),
        rgba(12,22,42,0.98)
    );
    border: 1px solid rgba(117,153,220,0.19);
    border-radius: 19px;
    padding: 25px;
    min-height: 205px;
    transition: all 0.28s ease;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 20px;
    right: 20px;
    height: 1px;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(120,170,255,0.55),
        transparent
    );
}

.feature-card:hover {
    border-color: rgba(100,157,255,0.55);
    background: linear-gradient(
        145deg,
        rgba(27,49,88,0.98),
        rgba(15,27,52,1)
    );
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.22);
}

.feature-icon {
    font-size: 2.15rem;
    margin-bottom: 19px;
}

.feature-title {
    color: #EDF3FF;
    font-size: 1.08rem;
    font-weight: 800;
    margin-bottom: 11px;
}

.feature-description {
    color: #9AACC9;
    font-size: 0.83rem;
    line-height: 1.85;
}

/* HOW IT WORKS */

.step-card {
    background: linear-gradient(145deg, rgba(18, 32, 56, .86), rgba(12, 20, 37, .9));
    border: 1px solid rgba(117, 153, 220, .15);
    border-radius: 16px;
    padding: 23px;
    min-height: 155px;
    transition: border-color .2s ease, transform .2s ease;
}

.step-card:hover {
    border-color: rgba(113, 162, 255, .4);
    transform: translateY(-3px);
}

.step-number {
    color: #83B4FF;
    font-size: .67rem;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 13px;
}

.step-title {
    color: #EAF1FF;
    font-size: .98rem;
    font-weight: 800;
    margin-bottom: 8px;
}

.step-description {
    color: #92A5C6;
    font-size: .78rem;
    line-height: 1.8;
}

/* INTELLIGENCE AND TRUST PANELS */

.intelligence-panel,
.trust-panel {
    background:
        radial-gradient(circle at 90% 0%, rgba(91, 129, 225, .12), transparent 40%),
        linear-gradient(120deg, rgba(20, 39, 72, .88), rgba(13, 21, 41, .92));
    border: 1px solid rgba(112, 157, 255, .19);
    border-radius: 19px;
    padding: 28px;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .025);
}

/* NEWS */

.news-card {
    background: linear-gradient(
        145deg,
        rgba(20,35,62,0.95),
        rgba(12,21,39,0.98)
    );
    border: 1px solid rgba(117,153,220,0.17);
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 14px;
    transition: all 0.22s ease;
}

.news-card:hover {
    border-color: rgba(100,157,255,0.42);
    transform: translateY(-2px);
}

.news-card a {
    color: #B5D1FF;
    text-decoration: none;
    font-weight: 800;
}

.news-description {
    color: #9AACC9;
    font-size: 0.8rem;
    line-height: 1.8;
    margin-top: 9px;
}

/* BUTTONS */

div.stButton > button {
    border-radius: 11px;
    font-weight: 750;
    min-height: 46px;
    border: 1px solid rgba(115, 165, 255, .3);
    background: linear-gradient(110deg, #2868D8, #247FBF);
    color: #FFFFFF;
    box-shadow: 0 7px 20px rgba(39, 87, 180, .15);
    transition: all .2s ease;
}

div.stButton > button:hover {
    border-color: #A4C7FF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(56, 105, 205, .25);
}

div.stButton > button:focus {
    box-shadow: 0 0 0 2px rgba(116, 166, 255, .25);
}

/* INPUTS */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
    background: #101B30;
    border-color: rgba(130, 160, 220, .2);
    border-radius: 10px;
    color: #EDF3FF;
}

/* FOOTER */

.footer {
    border-top: 1px solid rgba(120,155,220,0.16);
    margin-top: 60px;
    padding-top: 28px;
    padding-bottom: 15px;
    color: #8296B8;
    font-size: 0.76rem;
    line-height: 1.8;
    text-align: center;
}

/* RESPONSIVE */

@media (max-width: 900px) {
    .block-container {
        padding: 1.3rem 1.2rem 3rem;
    }

    .hero-section {
        padding-top: 32px;
    }

    .hero-title {
        letter-spacing: -1.8px;
    }

    .hero-panel {
        min-height: auto;
    }
}

@media (max-width: 600px) {
    .hero-title {
        font-size: 2.65rem;
    }

    .section-heading {
        font-size: 1.45rem;
    }

    .feature-card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

with st.sidebar:

    render_html("""
    <div style="padding:12px 4px 22px 4px;">
        <div style="
            font-size:1.65rem;
            font-weight:900;
            color:#EAF1FF;
            letter-spacing:-1px;">
            🛡️ ScamShield AI
        </div>
        <div style="
            font-size:0.65rem;
            color:#7FAEFF;
            font-weight:800;
            letter-spacing:2px;
            margin-top:5px;">
            DIGITAL PROTECTION PLATFORM
        </div>
    </div>
    """)

    st.divider()

    st.caption("MAIN")
    st.page_link("app.py", label="Command Centre", icon="🏠")

    st.caption("PROTECTION")
    st.page_link("pages/1_Cyber_Safety.py", label="Cyber Safety", icon="🛡️")
    st.page_link("pages/4_Link_Safety.py", label="Link Safety", icon="🔗")
    st.page_link("pages/3_Family_Safety.py", label="Family Safety", icon="👨‍👩‍👧")

    st.caption("KNOWLEDGE")
    st.page_link("pages/2_Scam_Academy.py", label="Scam Academy", icon="🎓")
    st.page_link("pages/5_About_ScamShield.py", label="About ScamShield", icon="ℹ️")

    st.caption("INTELLIGENCE")
    st.page_link("pages/6_Test_Lab.py", label="AI Test Lab", icon="🧪")
    st.page_link("pages/7_Threat_Intelligence.py", label="Threat Intelligence", icon="🔍")
    st.page_link("pages/8_Threat_Network.py", label="Threat Network", icon="🌐")
    st.page_link("pages/9_Market_Insights.py", label="Market Insights", icon="📊")
    st.page_link("pages/10_Global_Intelligence.py", label="Global Intelligence", icon="🌍")

    st.divider()

    st.caption("AI-POWERED DIGITAL SAFETY")


# =========================================================
# CYBERSECURITY NEWS FETCHER
# =========================================================

@st.cache_data(ttl=300, show_spinner=False)
def get_cyber_news():

    feeds = [
        "https://www.cisa.gov/news.xml",
        "https://news.google.com/rss/search?q=cybersecurity+scam+phishing&hl=en-IN&gl=IN&ceid=IN:en"
    ]

    articles = []

    for feed_url in feeds:

        try:
            request = urllib.request.Request(
                feed_url,
                headers={"User-Agent": "Mozilla/5.0 ScamShieldAI"}
            )

            with urllib.request.urlopen(request, timeout=8) as response:
                content = response.read()

            root = ET.fromstring(content)

            for item in root.findall(".//item"):

                title = item.findtext("title", "").strip()
                link = item.findtext("link", "").strip()
                description = item.findtext("description", "").strip()

                if not title or not link:
                    continue

                description = re.sub(r"<[^>]+>", " ", description)
                description = html.unescape(description)
                description = " ".join(description.split())

                articles.append({
                    "title": title,
                    "link": link,
                    "description": description[:230]
                })

        except Exception:
            continue

    unique = []
    seen = set()

    for article in articles:
        if article["link"] not in seen:
            seen.add(article["link"])
            unique.append(article)

    return unique[:8]


# =========================================================
# BRAND HEADER
# =========================================================

render_html("""
<div style="
    display:flex;
    justify-content:space-between;
    align-items:center;
    flex-wrap:wrap;
    gap:10px;
    padding-bottom:15px;
    border-bottom:1px solid rgba(120,155,220,0.14);">

    <div style="
        color:#A9C5F3;
        font-size:0.75rem;
        font-weight:900;
        letter-spacing:2px;">
        🛡️ SCAMSHIELD AI
    </div>

    <div style="
        color:#8499BB;
        font-size:0.67rem;
        font-weight:800;
        letter-spacing:1.5px;">
        AI-POWERED DIGITAL PROTECTION
    </div>

</div>
""")


# =========================================================
# HERO
# =========================================================

render_html("""
<div class="hero-section">

    <div class="hero-kicker">
        YOUR DIGITAL DEFENCE STARTS HERE
    </div>

    <div class="hero-title">
        Don't let a scam<br>
        catch you <span>off guard.</span>
    </div>

    <div class="hero-description">
        ScamShield AI helps you examine suspicious messages,
        check unfamiliar links and understand digital threats
        with AI-powered analysis and public threat intelligence.

        <br><br>

        Your digital safety. Your control. Smarter protection.
    </div>

</div>
""")


# =========================================================
# HERO ACTIONS AND PANEL
# =========================================================

left, right = st.columns([1.1, 0.9], gap="large")

with left:

    render_html("""
    <div style="
        color:#7FAEFF;
        font-size:0.7rem;
        font-weight:800;
        letter-spacing:2px;
        margin-bottom:15px;">
        START PROTECTING YOURSELF
    </div>
    """)

    if st.button("🛡️ Analyse a Message", use_container_width=True):
        st.switch_page("pages/1_Cyber_Safety.py")

    if st.button("🔗 Check a Suspicious Link", use_container_width=True):
        st.switch_page("pages/4_Link_Safety.py")

    render_html("""
    <div style="
        margin-top:20px;
        color:#8298BB;
        font-size:0.77rem;
        line-height:1.8;">
        User-controlled analysis.<br>
        You choose what you want to examine.
    </div>
    """)


with right:

    render_html("""
    <div class="hero-panel">

        <div class="section-kicker" style="text-align:center;">
            SCAMSHIELD AI / ACTIVE PROTECTION
        </div>

        <div class="hero-shield">🛡️</div>

        <div class="hero-panel-title">
            AI-Powered Scam Detection
        </div>

        <div class="hero-panel-description">
            Analyse suspicious messages, inspect unfamiliar
            links and identify potential digital fraud
            with AI-assisted analysis.
        </div>

        <div class="capability-wrap">

            <span class="capability">MESSAGE ANALYSIS</span>
            <span class="capability">LINK PROTECTION</span>
            <span class="capability capability-purple">THREAT INTELLIGENCE</span>

        </div>

        <div class="panel-footer">
            DETECT • ANALYSE • PROTECT
        </div>

    </div>
    """)


st.write("")
st.divider()


# =========================================================
# PROTECTION CENTRE
# =========================================================

section_heading(
    "Protect yourself from digital scams",
    "Your essential tools for understanding and examining potential digital threats."
)

cards = [
    (
        "📩",
        "Cyber Safety",
        "Examine suspicious SMS messages and text content with AI-assisted scam detection.",
        "pages/1_Cyber_Safety.py"
    ),
    (
        "🔗",
        "Link Safety",
        "Inspect unfamiliar URLs and understand potential phishing warning signs.",
        "pages/4_Link_Safety.py"
    ),
    (
        "👨‍👩‍👧",
        "Family Safety",
        "Explore practical digital safety guidance for safer online experiences.",
        "pages/3_Family_Safety.py"
    )
]

columns = st.columns(3, gap="medium")

for column, card in zip(columns, cards):

    with column:

        feature_card(card[0], card[1], card[2])

        if st.button(
            "Explore " + card[1],
            use_container_width=True,
            key="feature_" + card[1]
        ):
            st.switch_page(card[3])


# =========================================================
# HOW IT WORKS
# =========================================================

section_heading(
    "How ScamShield Works",
    "A clearer way to examine digital risks and understand the results."
)

steps = [
    (
        "01 / SUBMIT",
        "Choose Content",
        "Submit a suspicious message or link that you want to examine."
    ),
    (
        "02 / ANALYSE",
        "AI-Assisted Analysis",
        "The relevant detection tool examines available patterns and indicators."
    ),
    (
        "03 / UNDERSTAND",
        "Review the Results",
        "Understand potential warning signs and recommended precautions."
    )
]

columns = st.columns(3, gap="medium")

for column, step in zip(columns, steps):

    with column:

        render_html(f"""
        <div class="step-card">
            <div class="step-number">{step[0]}</div>
            <div class="step-title">{step[1]}</div>
            <div class="step-description">{step[2]}</div>
        </div>
        """)


# =========================================================
# INTELLIGENCE CENTRE
# =========================================================

section_heading(
    "Go beyond basic detection",
    "Explore the technology, research and public information supporting digital safety."
)

intelligence = [
    (
        "🧪",
        "AI Test Lab",
        "Explore the AI detection system and examine its capabilities.",
        "pages/6_Test_Lab.py"
    ),
    (
        "🔍",
        "Threat Intelligence",
        "Explore public cybersecurity information and threat updates.",
        "pages/7_Threat_Intelligence.py"
    ),
    (
        "🌐",
        "Threat Network",
        "Explore network-related threat intelligence and activity.",
        "pages/8_Threat_Network.py"
    ),
    (
        "📊",
        "Market Insights",
        "Explore cybersecurity trends and market-related information.",
        "pages/9_Market_Insights.py"
    )
]

columns = st.columns(4, gap="medium")

for column, item in zip(columns, intelligence):

    with column:

        feature_card(item[0], item[1], item[2])

        if st.button(
            "Explore",
            use_container_width=True,
            key="intel_" + item[1]
        ):
            st.switch_page(item[3])


# =========================================================
# GLOBAL INTELLIGENCE
# =========================================================

section_heading(
    "See the bigger digital picture",
    "A dedicated global exploration space within ScamShield AI."
)

global_left, global_right = st.columns([1.15, 0.85], gap="large")

with global_left:

    render_html("""
    <div class="intelligence-panel">

        <div style="font-size:2.8rem;margin-bottom:12px;">
            🌍
        </div>

        <div style="
            color:#EDF3FF;
            font-size:1.35rem;
            font-weight:900;
            margin-bottom:12px;">
            Global Intelligence
        </div>

        <div style="
            color:#A0B3D2;
            font-size:0.86rem;
            line-height:1.9;">

            Explore the interactive 3D Earth, geographic
            coverage visualisations, public BGP network
            activity and satellite-data exploration.

            <br><br>

            Discover the wider digital landscape through
            a dedicated global intelligence experience.

        </div>

    </div>
    """)

with global_right:

    render_html("""
    <div style="
        min-height:230px;
        border-radius:19px;
        border:1px solid rgba(105,157,255,0.25);
        background:radial-gradient(circle at center,rgba(45,100,190,0.30),rgba(12,22,44,0.96) 70%);
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        text-align:center;
        padding:25px;">

        <div style="
            font-size:4rem;
            filter:drop-shadow(0 0 20px rgba(70,140,255,0.35));">
            🌐
        </div>

        <div style="
            color:#EAF1FF;
            font-size:1.1rem;
            font-weight:900;
            margin-top:12px;">
            GLOBAL NETWORK VIEW
        </div>

        <div style="
            color:#91A8CE;
            font-size:0.75rem;
            margin-top:8px;">
            Interactive geographic intelligence
        </div>

    </div>
    """)

    if st.button(
        "🌍 Open Global Intelligence",
        use_container_width=True
    ):
        st.switch_page("pages/10_Global_Intelligence.py")


# =========================================================
# CYBERSECURITY UPDATES
# =========================================================

section_heading(
    "Cybersecurity Updates",
    "Public cybersecurity news and information from external sources."
)

with st.spinner("Loading cybersecurity updates..."):
    news_articles = get_cyber_news()

if news_articles:

    for article in news_articles:

        safe_title = html.escape(article["title"])
        safe_link = html.escape(article["link"], quote=True)
        safe_description = html.escape(article["description"])

        render_html(f"""
        <div class="news-card">

            <a href="{safe_link}" target="_blank">
                {safe_title}
            </a>

            <div class="news-description">
                {safe_description}
            </div>

        </div>
        """)

else:

    st.info(
        "Public cybersecurity updates are temporarily unavailable."
    )


# =========================================================
# PRIVACY AND TRANSPARENCY
# =========================================================

section_heading(
    "Your privacy matters",
    "Digital protection should never require unnecessary access to personal information."
)

render_html("""
<div class="trust-panel">

    <div style="
        color:#EAF1FF;
        font-size:1.2rem;
        font-weight:900;
        margin-bottom:12px;">
        Your information stays under your control.
    </div>

    <div style="
        color:#A3B5D4;
        font-size:0.86rem;
        line-height:1.9;">

        ScamShield AI is designed around user-submitted
        content and user-controlled analysis.

        <br><br>

        You decide which messages and links you want to
        examine. The platform does not need automatic
        access to your personal messages or calls.

        <br><br>

        Detection results can be incorrect. A result should
        not be treated as a guarantee that a message or
        website is safe or fraudulent.

        <br><br>

        Never submit passwords, OTPs, UPI PINs or banking
        credentials for analysis.

    </div>

</div>
""")

render_html("""
<div style="
    display:flex;
    flex-wrap:wrap;
    gap:15px;
    margin-top:17px;
    color:#91A8CE;
    font-size:0.75rem;
    font-weight:700;">

    <div>✓ User-controlled analysis</div>
    <div>✓ Clear explanations of detection limitations</div>
    <div>✓ Public information sources</div>

</div>
""")


# =========================================================
# FOOTER
# =========================================================

render_html(f"""
<div class="footer">

    <div style="
        color:#A9C5F3;
        font-size:0.9rem;
        font-weight:900;
        letter-spacing:1.5px;
        margin-bottom:8px;">
        🛡️ SCAMSHIELD AI
    </div>

    AI-POWERED DIGITAL PROTECTION

    <br><br>

    A student-developed AI Capstone Project

    <br><br>

    © {datetime.now().year} ScamShield AI

</div>
""")
