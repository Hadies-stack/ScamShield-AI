
import streamlit as st

st.set_page_config(
    page_title="About ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ About ScamShield AI")

st.subheader("Understand the scam. Before it catches you.")

st.write("""
ScamShield AI is a student-developed AI and
cybersecurity awareness project.

Our mission is to help people recognise suspicious
digital messages and make safer online decisions.
""")

st.divider()

st.header("🧠 How It Works")

st.markdown("""
1. **Message Analysis:** The user provides a message.
2. **Language Detection:** The system estimates its language.
3. **Scam DNA:** It identifies potentially suspicious patterns.
4. **AI Classification:** A trained model can classify messages.
5. **Risk Assessment:** Available indicators are combined
   into an experimental risk score.
""")

st.divider()

st.header("🔐 Our Privacy Principles")

st.markdown("""
- Messages should not be stored by default.
- Never request OTPs, UPI PINs or passwords.
- Do not collect unnecessary personal information.
- Be transparent about how analysis works.
""")

st.divider()

st.header("⚠️ Important Limitations")

st.warning("""
ScamShield AI is an educational prototype.

It cannot guarantee that a message or website is safe.
It does not verify bank accounts, identify message senders
or replace official fraud-reporting services.
""")

st.divider()

st.header("🌐 Cybersecurity Learning Resources")

st.markdown("""
- [CERT-In](https://www.cert-in.org.in/)
- [OWASP](https://owasp.org/)
- [National Cyber Crime Reporting Portal](https://cybercrime.gov.in/)
- [Google Safe Browsing](https://safebrowsing.google.com/)
""")

st.divider()

st.header("🎯 Our Vision")

st.write("""
To make digital safety easier to understand and more
accessible through responsible AI, cybersecurity
education and transparent technology.
""")

st.caption(
    "ScamShield AI | Class 12 Artificial Intelligence Capstone Project"
)
