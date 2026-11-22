
import re

SCAM_PATTERNS = {
    "Urgency": [
        r"urgent", r"immediately", r"act now",
        r"within 24 hours", r"account.*blocked",
        r"turant", r"abhi", r"तुरंत",
        r"आज.*बंद", r"जल्दी", r"अभी"
    ],
    "Sensitive information request": [
        r"\botp\b", r"\bpin\b", r"password",
        r"bank details", r"share.*details",
        r"भेजें.*otp", r"ओटीपी",
        r"पासवर्ड", r"पिन"
    ],
    "Payment pressure": [
        r"pay now", r"send money",
        r"processing fee", r"registration fee",
        r"पैसे भेजें", r"भुगतान करें"
    ],
    "Prize or reward claim": [
        r"you have won", r"lottery", r"prize",
        r"claim.*reward", r"inaam", r"इनाम",
        r"लॉटरी", r"जीत"
    ],
    "Suspicious link language": [
        r"click.*link", r"verify.*link",
        r"bit\.ly", r"tinyurl", r"http://",
        r"लिंक पर क्लिक", r"लिंक खोलें"
    ]
}

EXPLANATIONS = {
    "Urgency": "The message creates pressure to act quickly. Scammers may use urgency to stop people from checking information.",
    "Sensitive information request": "The message mentions sensitive information such as OTPs, PINs or passwords. Never share these with anyone.",
    "Payment pressure": "The message appears to request money or payment. Independently verify the request before paying.",
    "Prize or reward claim": "The message mentions a prize or reward. Unexpected prize claims can be used to trick people.",
    "Suspicious link language": "The message contains link-related warning signs. Avoid opening unexpected links."
}

def analyse_scam_dna(message):
    message = message.lower()
    findings = []

    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, message):
                findings.append(category)
                break

    explanations = [
        {
            "indicator": finding,
            "explanation": EXPLANATIONS[finding]
        }
        for finding in findings
    ]

    return {
        "findings": findings,
        "risk_indicators_count": len(findings),
        "explanations": explanations
    }
