# interface.py

import tkinter as tk
from correcteur import corriger
from data.copies import questions

def lancer_correction():
    id_q = int(var_question.get())
    reponse = zone_texte.get("1.0", tk.END)

    note, commentaire = corriger(id_q, reponse)

    resultat.set(f"Note : {note}\n{commentaire}")

# Fenêtre
fenetre = tk.Tk()
fenetre.title("Agent IA de correction - NSI")

# Question
tk.Label(fenetre, text="Choisir la question").pack()
var_question = tk.StringVar(value="1")

for q in questions:
    tk.Radiobutton(
        fenetre,
        text=q["question"],
        variable=var_question,
        value=str(q["id"])
    ).pack(anchor="w")

# Zone texte
zone_texte = tk.Text(fenetre, height=6, width=60)
zone_texte.pack()

# Bouton
tk.Button(fenetre, text="Corriger", command=lancer_correction).pack()

# Résultat
resultat = tk.StringVar()
tk.Label(fenetre, textvariable=resultat).pack()

fenetre.mainloop()
