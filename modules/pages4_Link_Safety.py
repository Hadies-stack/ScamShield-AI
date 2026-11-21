
import streamlit as st

from modules.link_checker import check_url

st.set_page_config(
    page_title="Link Safety | ScamShield AI",
    page_icon="🔗",
    layout="wide"
)

st.title("🔗 Link Safety Checker")

st.subheader("Think before you click.")

st.write(
    "Check a URL for common suspicious characteristics "
    "without opening the website."
)

url = st.text_input(
    "Enter a suspicious URL:",
    placeholder="https://example.com"
)

if st.button("Check URL", type="primary"):

    if not url.strip():
        st.warning("Please enter a URL.")

    else:
        result = check_url(url)

        st.divider()
        st.header("Analysis Results")

        if not result["valid"]:
            st.error(result["findings"][0])

        else:
            st.write(f"**Domain:** {result['hostname']}")

            if result["findings"]:
                st.warning("Warning indicators found:")

                for finding in result["findings"]:
                    st.write(f"⚠️ {finding}")

            else:
                st.success(
                    "No basic URL warning indicators detected."
                )

            st.info(
                "This is a basic URL inspection, not a "
                "malware scan or safety certification. "
                "Do not visit an unfamiliar link just because "
                "it passes these checks."
            )

st.divider()

st.subheader("🔐 Link Safety Tips")

st.markdown("""
- Check the spelling of website domains.
- Avoid unexpected login links.
- Never enter banking credentials on unfamiliar websites.
- Use official apps or manually typed website addresses.
""")
