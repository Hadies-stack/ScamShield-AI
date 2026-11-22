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
    "Urgency": "The message creates pressure to act quickly.",
    "Sensitive information request": "The message mentions sensitive information such as OTPs, PINs or passwords.",
    "Payment pressure": "The message appears to request money or payment.",
    "Prize or reward claim": "The message mentions a prize or reward.",
    "Suspicious link language": "The message contains link-related warning signs."
}

def analyse_scam_dna(message):
    findings = []
    matched_phrases = {}

    for category, patterns in SCAM_PATTERNS.items():
        matches = []

        for pattern in patterns:
            for match in re.finditer(pattern, message, re.IGNORECASE):
                matches.append(match.group())

        if matches:
            findings.append(category)
            matched_phrases[category] = list(set(matches))

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
        "explanations": explanations,
        "matched_phrases": matched_phrases
    }
