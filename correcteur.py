# correcteur.py

from data.copies import questions
from analyse import analyser_reponse
from evaluation import calcul_note_sur_20, generer_commentaire

def corriger(id_question, reponse):
    question = next(q for q in questions if q["id"] == id_question)

    score, score_max = analyser_reponse(
        reponse,
        question["criteres"]
    )

    note_20 = calcul_note_sur_20(score, score_max)
    commentaire = generer_commentaire(note_20)

    return note_20, commentaire
