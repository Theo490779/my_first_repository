import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import csv
def supprimer_article():
    name = entry_nom.get().strip()
    article = entry_article.get().strip()
    if not name or not article:
        messagebox.showwarning("Erreur", "Remplir les deux cases svp")
    else:
        try:
            with open("donnees.csv",newline="",encoding="utf-8") as fichier:
                lecteur = csv.reader(fichier)
                lignes = list(lecteur)

                entete = ligne[0]
                donnees = ligne[1:]

            nouvelle_donnees = []
            trouvee = False
            for ligne in donnees:
                if ligne[0] == name or ligne[1:] == article:
                    trouvee = True
                else:
                    nouvelle_donnees.append(ligne)
            if trouvee:
                with open("donnees.csv","w", newline="", encoding="utf-8") as fichier_deux:
                    ecrivain = csv.writer(fichier_deux)
                    ecrivain.writerow(entete)
                    ecrivain.writerows(nouvelle_donnees)
                    messagebox.showinfo("Succès", 'La ligne a été supprimée')
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier n'a pas été retrouvé")



window = tk.Tk()
window.title("Annuler")
window.geometry("900x500")
label_nom= tk.Label(window,text="Nom")
label_nom.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_nom = tk.Entry(window)
entry_nom.grid(row=0, column=1, padx=10, pady=10)

label_article= tk.Label(window,text="Article")
label_article.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_article= tk.Entry(window)
entry_article.grid(row=1, column=1, padx=10, pady=10)

bouton = tk.Button(window, text="Supprimer", command="None")
bouton.grid(row=2,column=1,padx=10, pady=10 )


