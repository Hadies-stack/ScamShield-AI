
def calculate_risk(scam_dna, prediction=None, scam_probability=None):

    indicators = scam_dna.get("risk_indicators_count", 0)

    # Start with transparent warning indicators
    score = min(indicators * 20, 60)

    # Add supporting ML evidence when available
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
        explanation = "Several warning signals were identified."
    elif score >= 30:
        level = "Medium"
        explanation = "Some suspicious patterns were identified."
    else:
        level = "Low"
        explanation = "Few known warning signals were identified."

    return {
        "score": score,
        "level": level,
        "explanation": explanation
    }
