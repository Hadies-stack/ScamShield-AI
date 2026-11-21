
import streamlit as st

st.set_page_config(
    page_title="Cyber Safety | ScamShield AI",
    page_icon="🔐",
    layout="wide"
)

st.title("🔐 Cyber Safety Centre")

st.write(
    "Learn how to recognise common online threats "
    "and protect your digital identity."
)

st.divider()

st.header("1. UPI Safety")

st.warning(
    "Never enter your UPI PIN to receive money. "
    "A UPI PIN is used to authorise payments."
)

st.markdown("""
- Verify the recipient before making a payment.
- Never share your UPI PIN or OTP.
- Be cautious of unexpected collect requests.
- Contact your bank through its official channels if something seems wrong.
""")

st.divider()

st.header("2. Phishing Awareness")

st.markdown("""
Phishing messages try to trick people into sharing
sensitive information or visiting unsafe websites.

**Warning signs:**
- Unexpected account warnings.
- Unusual requests for personal information.
- Pressure to act immediately.
- Links that do not match the official organisation's domain.
""")

st.divider()

st.header("3. Password and Account Safety")

st.markdown("""
- Use unique passwords for important accounts.
- Enable multi-factor authentication.
- Never share login codes.
- Review account activity regularly.
- Keep your devices and applications updated.
""")

st.divider()

st.header("4. Official Cybersecurity Resources")

st.markdown("""
- [CERT-In](https://www.cert-in.org.in/)
- [National Cyber Crime Reporting Portal](https://cybercrime.gov.in/)
- [OWASP](https://owasp.org/)
""")

st.info(
    "If you experience financial cyber fraud in India, "
    "contact your bank immediately and report it through "
    "the official cybercrime portal or helpline 1930."
)

st.caption(
    "Educational information. Always use official channels "
    "for reporting and account recovery."
)
