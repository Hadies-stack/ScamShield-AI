
import streamlit as st


def apply_theme():

    st.markdown("""
    <style>

    /* =====================================
       SCAMSHIELD AI — DESIGN SYSTEM
       MIDNIGHT BLUE + ROYAL BLUE + PURPLE
    ===================================== */

    :root {
        --background: #080D1C;
        --surface: #101A30;
        --surface-light: #172541;
        --blue: #477BDF;
        --blue-light: #78A5FF;
        --purple: #7950C9;
        --purple-light: #A98AEF;
        --text: #E9EDFF;
        --muted: #AEB9D8;
        --border: rgba(125, 153, 220, 0.19);
    }

    /* MAIN BACKGROUND */

    .stApp {
        background:
            radial-gradient(
                circle at 12% 0%,
                rgba(48, 83, 160, 0.20),
                transparent 32%
            ),
            radial-gradient(
                circle at 88% 12%,
                rgba(121, 80, 201, 0.15),
                transparent 30%
            ),
            #080D1C;

        color: var(--text);
    }

    /* MAIN CONTENT */

    [data-testid="stMainBlockContainer"] {
        max-width: 1450px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

        /* SIDEBAR */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #0B1830 0%,
            #081326 100%
        ) !important;
        border-right: 1px solid rgba(90, 150, 255, 0.22);
    }

    [data-testid="stSidebar"] > div:first-child {
        background: transparent !important;
    }

    [data-testid="stSidebar"] h1 {
        color: #E9EDFF;
        font-weight: 800;
        letter-spacing: -0.8px;
    }

    [data-testid="stSidebar"] p {
        color: #AEB9D8;
    }

    /* BLUE NAVIGATION PANELS */

    [data-testid="stSidebar"] div[data-testid="stPageLink"] a {
        display: flex !important;
        align-items: center;
        padding: 11px 13px !important;
        margin: 5px 0;
        border-radius: 11px !important;
        background: linear-gradient(
            110deg,
            rgba(35, 83, 155, 0.48),
            rgba(22, 52, 100, 0.58)
        ) !important;
        border: 1px solid rgba(100, 157, 255, 0.22) !important;
        color: #DCE8FF !important;
        transition: all 0.2s ease;
    }

    [data-testid="stSidebar"] div[data-testid="stPageLink"] a:hover {
        background: linear-gradient(
            110deg,
            #2868C8,
            #194A91
        ) !important;
        border-color: #78A5FF !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] div[data-testid="stPageLink"] a[aria-current="page"] {
        background: linear-gradient(
            110deg,
            #2868C8,
            #194A91
        ) !important;
        border-color: #78A5FF !important;
        color: #FFFFFF !important;
    }

    /* HEADINGS */

    h1, h2, h3, h4 {
        color: var(--text) !important;
        font-weight: 750 !important;
        letter-spacing: -0.5px;
    }

    h1 {
        letter-spacing: -1.2px !important;
    }

    p, li, label {
        color: #D0D8ED;
    }

    [data-testid="stCaptionContainer"] p {
        color: var(--muted) !important;
    }

    /* NATIVE CONTAINERS / CARDS */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: linear-gradient(
            145deg,
            rgba(23, 37, 65, 0.88),
            rgba(14, 23, 43, 0.96)
        );

        border: 1px solid var(--border);
        border-radius: 17px;
        box-shadow: 0 8px 28px rgba(0, 0, 0, 0.16);
        transition: border-color 0.2s ease,
                    transform 0.2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(121, 80, 201, 0.45);
    }

    /* METRICS */

    [data-testid="stMetric"] {
        background: linear-gradient(
            145deg,
            #172747,
            #111C33
        );

        border: 1px solid var(--border);
        padding: 17px 19px;
        border-radius: 15px;
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted) !important;
    }

    [data-testid="stMetricValue"] {
        color: var(--text) !important;
        font-weight: 800;
    }

    /* BUTTONS */

    .stButton > button,
    .stDownloadButton > button,
    [data-testid="stPageLink"] a {
        background: linear-gradient(
            105deg,
            #315FAF,
            #6743AD
        );

        color: white !important;
        border: 1px solid rgba(164, 177, 255, 0.25);
        border-radius: 10px;
        font-weight: 650;
        min-height: 42px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover,
    [data-testid="stPageLink"] a:hover {
        border-color: var(--purple-light);
        filter: brightness(1.15);
        transform: translateY(-1px);
    }

    /* INPUTS */

    .stTextInput input,
    .stTextArea textarea,
    .stNumberInput input {
        background: #101B32 !important;
        color: var(--text) !important;
        border: 1px solid #344568 !important;
        border-radius: 10px !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus,
    .stNumberInput input:focus {
        border-color: var(--blue-light) !important;
        box-shadow: 0 0 0 2px rgba(71, 123, 223, 0.16);
    }

    /* SELECT BOXES */

    [data-baseweb="select"] > div {
        background: #101B32;
        color: var(--text);
        border-color: #344568;
        border-radius: 10px;
    }

    [data-baseweb="popover"] {
        background: #15223D;
    }

    /* CHECKBOXES AND RADIO BUTTONS */

    [data-testid="stCheckbox"] label,
    [data-testid="stRadio"] label {
        color: var(--text);
    }

    /* TABS */

    [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--border);
    }

    [data-baseweb="tab"] {
        color: var(--muted);
        background: transparent;
    }

    [aria-selected="true"][data-baseweb="tab"] {
        color: var(--blue-light) !important;
        border-bottom-color: var(--purple) !important;
    }

    /* DATA TABLES */

    [data-testid="stDataFrame"],
    [data-testid="stTable"] {
        border: 1px solid var(--border);
        border-radius: 12px;
        overflow: hidden;
    }

    /* EXPANDERS */

    [data-testid="stExpander"] {
        background: rgba(17, 28, 51, 0.85);
        border: 1px solid var(--border);
        border-radius: 12px;
    }

    /* ALERTS */

    [data-testid="stAlert"] {
        border-radius: 12px;
        border: 1px solid var(--border);
    }

    /* DIVIDERS */

    hr {
        border-color: var(--border) !important;
    }

    /* LINKS */

    a {
        color: var(--blue-light);
    }

    a:hover {
        color: var(--purple-light);
    }

    /* SCROLLBAR */

    ::-webkit-scrollbar {
        width: 7px;
        height: 7px;
    }

    ::-webkit-scrollbar-track {
        background: #080D1C;
    }

    ::-webkit-scrollbar-thumb {
        background: #344B78;
        border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #7950C9;
    }

    /* RESPONSIVE */

    @media (max-width: 768px) {
        [data-testid="stMainBlockContainer"] {
            padding: 1rem;
        }

        h1 {
            font-size: 1.8rem !important;
        }

        [data-testid="stMetric"] {
            padding: 12px;
        }
    }

    </style>
    """, unsafe_allow_html=True)
