# interface.py

import json
import tkinter as tk
from correcteur import corriger


with open("data/copies.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]


def lancer_correction():
    id_question = int(var_question.get())
    reponse = zone_texte.get("1.0", tk.END)

    note, commentaire = corriger(id_question, reponse)
    resultat.set(f"Note sur 20 : {note}\n{commentaire}")


fenetre = tk.Tk()
fenetre.title("Agent IA de correction - NSI")

tk.Label(fenetre, text="Choisir la question").pack()

var_question = tk.StringVar(value="1")
for q in questions:
    tk.Radiobutton(
        fenetre,
        text=q["question"],
        variable=var_question,
        value=str(q["id"])
    ).pack(anchor="w")

zone_texte = tk.Text(fenetre, height=6, width=60)
zone_texte.pack()

tk.Button(fenetre, text="Corriger", command=lancer_correction).pack()

resultat = tk.StringVar()
tk.Label(fenetre, textvariable=resultat).pack()

fenetre.mainloop()
