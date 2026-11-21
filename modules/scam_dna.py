
import re

SCAM_PATTERNS = {
    "Urgency": [
        r"urgent",
        r"immediately",
        r"act now",
        r"within 24 hours",
        r"account.*blocked",
        r"turant",
        r"abhi"
    ],
    "Sensitive information request": [
        r"\botp\b",
        r"\bpin\b",
        r"password",
        r"bank details",
        r"share.*details"
    ],
    "Payment pressure": [
        r"pay now",
        r"send money",
        r"processing fee",
        r"registration fee",
        r"upi"
    ],
    "Prize or reward claim": [
        r"you have won",
        r"lottery",
        r"prize",
        r"claim.*reward",
        r"inaam",
        r"lakh.*jeet"
    ],
    "Suspicious link language": [
        r"click.*link",
        r"verify.*link",
        r"bit\.ly",
        r"tinyurl",
        r"http://"
    ]
}


def analyse_scam_dna(message):
    message = message.lower()
    findings = []

    for category, patterns in SCAM_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, message):
                findings.append(category)
                break

    return {
        "findings": findings,
        "risk_indicators_count": len(findings)
    }
