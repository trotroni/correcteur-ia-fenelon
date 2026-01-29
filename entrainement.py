# entrainement.py

from data.copies import questions, copies
from analyse import analyser_reponse
from evaluation import calcul_note_sur_20

def statistiques():
    erreurs = []

    for copie in copies:
        question = next(q for q in questions if q["id"] == copie["id_question"])

        score, score_max = analyser_reponse(
            copie["reponse_eleve"],
            question["criteres"]
        )

        note_ia = calcul_note_sur_20(score, score_max)
        note_prof = copie["note_prof"] * (20 / question["note_max"])

        erreurs.append(abs(note_ia - note_prof))

        print("Note IA :", note_ia, "/ Note Prof :", round(note_prof, 1))
        print("-" * 40)

    print("Erreur moyenne :", round(sum(erreurs) / len(erreurs), 2))


if __name__ == "__main__":
    statistiques()
