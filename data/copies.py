# data/copies.py

questions = [
    {
        "id": 1,
        "question": "Qu'est-ce qu'un algorithme ?",
        "note_max": 4,
        "criteres": {
            "suite": {"poids": 1, "synonymes": ["ensemble", "enchaînement"]},
            "instructions": {"poids": 1, "synonymes": ["étapes", "ordres"]},
            "résoudre": {"poids": 1, "synonymes": ["solution", "traiter"]},
            "problème": {"poids": 1, "synonymes": ["tâche", "situation"]}
        }
    },
    {
        "id": 2,
        "question": "Qu'est-ce qu'une variable ?",
        "note_max": 3,
        "criteres": {
            "valeur": {"poids": 1, "synonymes": ["donnée"]},
            "mémoire": {"poids": 1, "synonymes": ["stockage"]},
            "modifiable": {"poids": 1, "synonymes": ["changeable"]}
        }
    }
]

copies = [
    {
        "id_question": 1,
        "reponse_eleve": "Un algorithme est une suite d'étapes permettant de résoudre un problème",
        "note_prof": 4
    },
    {
        "id_question": 1,
        "reponse_eleve": "C'est une méthode",
        "note_prof": 1
    },
    {
        "id_question": 2,
        "reponse_eleve": "Une variable stocke une valeur en mémoire",
        "note_prof": 3
    }
]
