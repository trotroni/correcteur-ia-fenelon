# evaluation.py

def calcul_note_sur_20(score, score_max):
    if score_max == 0:
        return 0
    return round((score / score_max) * 20)


def generer_commentaire(note_20):
    if note_20 >= 16:
        return "Très bonne réponse."
    elif note_20 >= 10:
        return "Réponse correcte mais incomplète."
    elif note_20 >= 5:
        return "Réponse insuffisante."
    else:
        return "Réponse très insuffisante."
