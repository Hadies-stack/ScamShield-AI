
HIGH_RISK_INDICATORS = {
    "Credential request",
    "Remote access request",
    "Threat or pressure"
}


def calculate_risk(scam_dna, prediction=None, scam_probability=None):

    findings = scam_dna.get("findings", [])
    indicators = scam_dna.get("risk_indicators_count", len(findings))

    score = min(indicators * 20, 60)

    # High-impact warning patterns
    if HIGH_RISK_INDICATORS.intersection(findings):
        score = max(score, 60)

    if prediction == "scam" and scam_probability is not None:
        if scam_probability >= 80:
            score += 30
        elif scam_probability >= 60:
            score += 20
        else:
            score += 10

    score = min(score, 100)

    if score >= 60:
        level = "High"
        explanation = "One or more high-impact warning patterns were identified."
    elif score >= 30:
        level = "Medium"
        explanation = "Some suspicious patterns were identified."
    else:
        level = "Low"
        explanation = "Few known warning patterns were identified."

    return {
        "score": score,
        "level": level,
        "explanation": explanation
    }
