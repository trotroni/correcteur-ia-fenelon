# entrainement.py

import json
from analyse import analyser_reponse
from evaluation import calcul_note_sur_20


with open("data/copies.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]
copies = data["copies"]


def statistiques():
    erreurs = []

    for copie in copies:
        question = next(q for q in questions if q["id"] == copie["id_question"])

        score, score_max = analyser_reponse(
            copie["reponse_eleve"],
            question["criteres"]
        )

        note_ia = calcul_note_sur_20(score, score_max)
        note_prof = copie["note_prof_sur_20"]

        erreurs.append(abs(note_ia - note_prof))

        print("Réponse :", copie["reponse_eleve"])
        print("Note IA :", note_ia, "| Note Prof :", note_prof)
        print("-" * 40)

    print("Erreur moyenne :", round(sum(erreurs) / len(erreurs), 2))


if __name__ == "__main__":
    statistiques()
