
import streamlit as st
import urllib.request
import urllib.parse
import json
import pandas as pd
from datetime import datetime
from modules.ui_theme import apply_theme

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Market Insights | ScamShield AI",
    page_icon="📈",
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
        radial-gradient(ellipse at 5% 0%, rgba(65,120,255,.13), transparent 32%),
        radial-gradient(ellipse at 95% 5%, rgba(30,170,220,.09), transparent 30%),
        linear-gradient(145deg, #061326, #081B31 55%, #061326);
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
    letter-spacing: -.5px;
}

p, label, li {
    color: #AABBD7;
    line-height: 1.8;
}

.market-hero {
    background:
        radial-gradient(ellipse at 90% 0%,rgba(65,140,255,.17),transparent 55%),
        linear-gradient(120deg,#102746,#0D1D36);
    border: 1px solid rgba(117,153,220,.23);
    border-radius: 22px;
    padding: 34px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}

.kicker {
    color: #91B9FF;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 3px;
}

.market-title {
    color: #F4F7FF;
    font-size: clamp(2rem,4vw,3rem);
    font-weight: 900;
    letter-spacing: -1.8px;
    margin: 13px 0;
}

.market-title span {
    background: linear-gradient(90deg,#64A8FF,#72D9FF,#A4C9FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.market-copy {
    color: #A5B5D1;
    line-height: 1.85;
    max-width: 800px;
    font-size: .92rem;
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
    min-height: 44px;
    transition: all .22s ease;
}

div.stButton > button:hover {
    border-color: #A9CAFF;
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(65,112,220,.22);
}

div[data-testid="stSelectbox"] > div > div {
    background: #0D1D36;
    border-color: rgba(117,153,220,.25);
    border-radius: 11px;
}

div[data-testid="stExpander"] {
    background: rgba(17,31,56,.85);
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid rgba(117,153,220,.2);
    border-radius: 13px;
    overflow: hidden;
}

div[data-testid="stAlert"] {
    border-radius: 13px;
}

hr {
    border-color: rgba(120,155,220,.16);
}

.market-section-label {
    color: #91B9FF;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.market-footer {
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
# MARKET DATA
# =========================================================

SYMBOLS = {
    "NIFTY 50": "^NSEI",
    "SENSEX": "^BSESN",
    "Reliance Industries": "RELIANCE.NS",
    "TCS": "TCS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS",
    "ITC": "ITC.NS"
}


@st.cache_data(ttl=900, show_spinner=False)
def fetch_market_data(symbol, period):
    """Fetch publicly available Yahoo Finance chart data."""

    url = (
        "https://query1.finance.yahoo.com/v8/finance/chart/"
        + urllib.parse.quote(symbol, safe="")
        + f"?range={period}&interval=1d"
    )

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 ScamShieldAI/1.0"}
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        result = json.loads(response.read().decode("utf-8"))

    chart_result = result.get("chart", {}).get("result")

    if not chart_result:
        raise ValueError("No market data was returned.")

    item = chart_result[0]
    timestamps = item.get("timestamp", [])
    quote = item["indicators"]["quote"][0]

    closes = quote.get("close", [])
    volumes = quote.get("volume", [])

    rows = []

    for timestamp, close, volume in zip(timestamps, closes, volumes):
        if close is None:
            continue

        rows.append({
            "Date": datetime.fromtimestamp(timestamp),
            "Close": float(close),
            "Volume": volume if volume is not None else 0
        })

    if not rows:
        raise ValueError("No usable price observations were found.")

    df = pd.DataFrame(rows)
    df = df.sort_values("Date").reset_index(drop=True)

    return df


# =========================================================
# TECHNICAL INDICATORS
# =========================================================

def calculate_indicators(df):
    df = df.copy()

    df["SMA20"] = df["Close"].rolling(20).mean()
    df["SMA50"] = df["Close"].rolling(50).mean()

    difference = df["Close"].diff()

    gains = difference.clip(lower=0)
    losses = -difference.clip(upper=0)

    average_gain = gains.rolling(14).mean()
    average_loss = losses.rolling(14).mean()

    relative_strength = average_gain / average_loss.replace(0, float("nan"))

    df["RSI"] = 100 - (100 / (1 + relative_strength))

    return df


def format_price(value):
    return f"₹{value:,.2f}"


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 📈 Market Insights")
    st.caption("SCAMSHIELD AI / FINANCIAL INTELLIGENCE")

    st.divider()

    st.page_link("app.py", label="← Back to Command Centre")

    st.divider()

    st.markdown("### DATA INFORMATION")

    st.caption("Source: Yahoo Finance chart endpoint")
    st.caption("Refresh interval: 15 minutes")
    st.caption("Data availability depends on the external provider.")


# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class="market-hero">
    <div class="kicker">SCAMSHIELD AI / MARKET INTELLIGENCE</div>
    <div class="market-title">Understand the <span>market.</span></div>
    <div class="market-copy">
        Explore Indian market indices, company price history,
        technical indicators and financial data.
        Understand what the numbers show before drawing conclusions.
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# CONTROLS
# =========================================================

left, right = st.columns([2, 1])

with left:
    selected_name = st.selectbox(
        "Select market or company",
        list(SYMBOLS.keys())
    )

with right:
    period = st.selectbox(
        "Chart period",
        ["1mo", "3mo", "6mo", "1y", "2y"],
        index=1
    )

if st.button("↻ Refresh market data"):
    fetch_market_data.clear()
    st.rerun()


# =========================================================
# FETCH AND DISPLAY
# =========================================================

symbol = SYMBOLS[selected_name]

try:

    with st.spinner("Fetching market information..."):
        df = fetch_market_data(symbol, period)

    df = calculate_indicators(df)

    latest = df.iloc[-1]
    previous = df.iloc[-2] if len(df) > 1 else latest

    latest_price = latest["Close"]
    previous_price = previous["Close"]

    change = latest_price - previous_price

    change_percent = (
        (change / previous_price) * 100
        if previous_price else 0
    )

    st.markdown('<div class="market-section-label">MARKET SNAPSHOT</div>',
                unsafe_allow_html=True)

    first_col, second_col, third_col = st.columns(3)

    with first_col:
        st.metric(
            "Latest available close",
            format_price(latest_price),
            f"{change:+.2f} ({change_percent:+.2f}%)"
        )

    with second_col:
        st.metric(
            "20-day moving average",
            format_price(latest["SMA20"])
            if pd.notna(latest["SMA20"]) else "Not enough data"
        )

    with third_col:
        st.metric(
            "50-day moving average",
            format_price(latest["SMA50"])
            if pd.notna(latest["SMA50"]) else "Not enough data"
        )

    st.caption(
        f"Last observation: {latest['Date'].strftime('%d %b %Y')} "
        f"· Symbol: {symbol}"
    )

    # -----------------------------------------------------
    # PRICE CHART
    # -----------------------------------------------------

    st.divider()

    st.subheader("📊 Price Movement")

    chart_data = df.set_index("Date")[["Close", "SMA20", "SMA50"]]

    st.line_chart(
        chart_data,
        height=380
    )

    st.caption(
        "Close = closing price. SMA20 and SMA50 = "
        "20-session and 50-session simple moving averages."
    )

    # -----------------------------------------------------
    # RSI
    # -----------------------------------------------------

    st.divider()

    st.subheader("📉 Relative Strength Index (RSI)")

    rsi_data = df.set_index("Date")[["RSI"]].dropna()

    if not rsi_data.empty:

        st.line_chart(rsi_data, height=220)

        current_rsi = latest["RSI"]

        if pd.notna(current_rsi):

            st.metric("Latest calculated RSI", f"{current_rsi:.2f}")

            if current_rsi >= 70:
                st.info(
                    "The RSI is above 70. This is commonly described "
                    "as an overbought-zone reading."
                )

            elif current_rsi <= 30:
                st.info(
                    "The RSI is below 30. This is commonly described "
                    "as an oversold-zone reading."
                )

            else:
                st.info(
                    "The RSI is between 30 and 70. "
                    "This is the commonly observed middle range."
                )

    else:
        st.info("There is not enough price history to calculate RSI.")

    # -----------------------------------------------------
    # TECHNICAL OVERVIEW
    # -----------------------------------------------------

    st.divider()

    st.subheader("🔍 Technical Overview")

    sma20 = latest["SMA20"]
    sma50 = latest["SMA50"]

    overview_1, overview_2 = st.columns(2)

    with overview_1:

        with st.container(border=True):

            if pd.notna(sma20):

                if latest_price > sma20:
                    st.write("**Price vs SMA20:** Above the 20-session average.")

                else:
                    st.write("**Price vs SMA20:** Below the 20-session average.")

            else:
                st.write("**Price vs SMA20:** Insufficient observations.")

    with overview_2:

        with st.container(border=True):

            if pd.notna(sma50):

                if latest_price > sma50:
                    st.write("**Price vs SMA50:** Above the 50-session average.")

                else:
                    st.write("**Price vs SMA50:** Below the 50-session average.")

            else:
                st.write("**Price vs SMA50:** Insufficient observations.")

    # -----------------------------------------------------
    # RECENT DATA
    # -----------------------------------------------------

    st.divider()

    st.subheader("📋 Recent Market Data")

    display_df = df.tail(10).copy()
    display_df["Date"] = display_df["Date"].dt.strftime("%d %b %Y")

    st.dataframe(
        display_df.sort_values("Date", ascending=False),
        use_container_width=True,
        hide_index=True
    )

except Exception as error:

    st.error(
        "Market data could not be loaded right now. "
        "The external data provider may be unavailable or may have "
        "limited access. Please try again later."
    )

    st.caption(f"Technical detail: {error}")


# =========================================================
# MARKET EDUCATION
# =========================================================

st.divider()

st.subheader("🎓 Understand the Indicators")

with st.expander("What is a moving average?"):

    st.write(
        "A simple moving average calculates the average closing price "
        "over a selected number of trading sessions. It helps describe "
        "historical price direction."
    )

with st.expander("What is RSI?"):

    st.write(
        "The Relative Strength Index is a momentum indicator that "
        "ranges from 0 to 100. Readings above 70 and below 30 are "
        "commonly studied as possible overbought and oversold conditions. "
        "They do not guarantee a future price movement."
    )

with st.expander("Important limitations"):

    st.write(
        "This page is an educational market-analysis tool. "
        "Indicators are calculated from historical price observations. "
        "They can be delayed, incomplete or inaccurate and should not "
        "be treated as guaranteed predictions or personalised investment advice."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    '<div class="market-footer">'
    'SCAMSHIELD AI • MARKET INSIGHTS • EDUCATIONAL INTELLIGENCE'
    '</div>',
    unsafe_allow_html=True
)
