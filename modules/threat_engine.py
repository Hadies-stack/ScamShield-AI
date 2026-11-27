
import re

from modules.scam_dna import analyse_scam_dna
from modules.language_support import detect_language
from modules.risk_engine import calculate_risk


CALL_PATTERNS = {
    "Impersonation": [
        r"\bcalling from (your )?bank\b",
        r"\bpolice department\b",
        r"\bcyber cell\b",
        r"\bbank officer\b",
        r"बैंक से बोल रहा",
        r"पुलिस से बोल रहा",
    ],

    "Credential request": [
        r"\bshare your otp\b",
        r"\btell me your otp\b",
        r"\bshare your pin\b",
        r"\bshare your password\b",
        r"ओटीपी बताइए",
        r"ओटीपी साझा",
        r"पिन बताइए",
        r"पासवर्ड बताइए",
    ],

    "Remote access request": [
        r"\binstall.*remote access\b",
        r"\binstall.*screen sharing\b",
        r"\bshare your screen\b",
        r"\bdownload.*support app\b",
        r"स्क्रीन शेयर",
        r"रिमोट एक्सेस",
    ],

    "Threat or pressure": [
        r"\barrest you\b",
        r"\baccount.*blocked\b",
        r"\blegal action\b",
        r"\bimmediately transfer\b",
        r"\bdo not tell anyone\b",
        r"गिरफ्तार",
        r"खाता बंद",
        r"किसी को मत बताना",
        r"तुरंत पैसे भेजें",
    ],
}


CALL_EXPLANATIONS = {
    "Impersonation": "The caller may be claiming to represent an official organisation. Verify independently.",
    "Credential request": "The caller appears to request sensitive credentials. Never disclose OTPs, PINs or passwords.",
    "Remote access request": "The caller may be asking for device access. Do not grant access to an unverified caller.",
    "Threat or pressure": "The caller may be using threats, urgency or secrecy to influence your decision.",
}


def analyse_threat(message, channel="SMS"):

    message = message.strip()

    if not message:
        return {"error": "Please provide message or call details."}

    channel = channel.upper()

    language = detect_language(message)
    dna = analyse_scam_dna(message)

    findings = list(dna["findings"])
    matched_phrases = dict(dna["matched_phrases"])
    explanations = list(dna["explanations"])

    if channel == "CALL":

        for category, patterns in CALL_PATTERNS.items():

            matches = []

            for pattern in patterns:
                for match in re.finditer(pattern, message, re.IGNORECASE):
                    matches.append(match.group())

            if matches:
                findings.append(category)

                matched_phrases[category] = list(
                    dict.fromkeys(matches)
                )

                explanations.append({
                    "indicator": category,
                    "explanation": CALL_EXPLANATIONS[category]
                })

    findings = list(dict.fromkeys(findings))

    combined_dna = {
        "risk_indicators_count": len(findings),
        "findings": findings
    }

    risk = calculate_risk(combined_dna)

    if findings:
        safety_actions = [
            "Do not share OTPs, PINs or passwords.",
            "Do not transfer money under pressure.",
            "Verify the caller or sender independently.",
            "Avoid unexpected links and remote-access requests.",
        ]
    else:
        safety_actions = [
            "No known warning pattern was identified.",
            "Do not share sensitive information.",
            "Verify unusual requests independently.",
        ]

    return {
        "channel": channel,
        "language": language,
        "findings": findings,
        "matched_phrases": matched_phrases,
        "explanations": explanations,
        "risk": risk,
        "safety_actions": safety_actions,
        "disclaimer": (
            "Experimental analysis only. "
            "This result does not confirm whether "
            "a communication is fraudulent."
        )
    }
