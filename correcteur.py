def corriger(texte):
    score = 0
    details = {}

    if "algorithme" in texte.lower():
        score += 5
        details["algorithme"] = "Présent"
    else:
        details["algorithme"] = "Absent"

    if "variable" in texte.lower():
        score += 5
        details["variable"] = "Présent"
    else:
        details["variable"] = "Absent"

    note = min(score, 20)

    return {
        "note": note,
        "details": details
    }
