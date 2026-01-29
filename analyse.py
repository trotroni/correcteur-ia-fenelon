# analyse.py

import string

def nettoyer_texte(texte):
    texte = texte.lower()
    for c in string.punctuation:
        texte = texte.replace(c, "")
    return texte


def critere_present(reponse, mot, synonymes):
    if mot in reponse:
        return True
    for syn in synonymes:
        if syn in reponse:
            return True
    return False


def analyser_reponse(reponse, criteres):
    reponse = nettoyer_texte(reponse)
    score = 0
    score_max = 0

    for mot, data in criteres.items():
        poids = data["poids"]
        score_max += poids

        if critere_present(reponse, mot, data["synonymes"]):
            score += poids

    return score, score_max
