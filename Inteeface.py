import tkinter as tk
from tkinter import  messagebox
import smtplib
from email.message import EmailMessage

# Pour stocker les champs de la première fenêtre
entries = {}

def envoie_mail(destinataire, sujet, message):
    smtp_server = "smtp.gmail.com"
    port = 587
    expediteur = "theotokosmongadji1@gmail.com"  # <- Adresse Gmail réelle
    mot_de_passe = "luba knhx tqbr kgzp"
    msg = EmailMessage()
    msg["From"] = expediteur
    msg["To"] = destinataire
    msg["Subject"] = sujet
    msg.set_content(message)

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(expediteur, mot_de_passe)
            server.send_message(msg)
            messagebox.showinfo("Succès", "Email envoyé avec succès.")
            return True
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur d'envoi : {e}")
        return False

def seconde_fenetre():
    # Récupération des données de la première fenêtre
    nom = entries["Nom"].get().strip()
    prenom = entries["Prenom"].get().strip()
    mail = entries["Mail"].get().strip()
    grade = entries["Grade"].get().strip()
    reference_acte = entries["Reference Acte"].get().strip()

    if not nom or not prenom or not mail or not grade or not reference_acte:
        messagebox.showerror('Erreur','Veuillez remplir tous les champs')
        return

    # Nouvelle fenêtre secondaire
    fenetre2 = tk.Toplevel()
    fenetre2.title("IDLC")
    fenetre2.geometry("500x400")

    labels_deux = ['Matricule','Date effet','Reliquat an','Reliquat jour','Reliquat mois','Reference acte']
    entries_two = {}

    for i, texte in enumerate(labels_deux):
        tk.Label(fenetre2, text=texte).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        e = tk.Entry(fenetre2)
        e.grid(row=i, column=1, padx=10, pady=5, sticky="w")
        entries_two[texte] = e

    def valider():
        # On récupère les champs de la deuxième fenêtre
        contenu = f"""Bonjour {prenom} {nom},

Voici les informations que vous avez remplies :

- Grade : {grade}
- Référence Acte : {reference_acte}

Détails :
"""
        for k, v in entries_two.items():
            contenu += f"- {k} : {v.get()}\n"

        # Envoi du mail
        sujet = "Confirmation de vos informations"
        envoie_mail(mail, sujet, contenu)

    bouton_valider = tk.Button(fenetre2, text="VALIDER", command=valider)
    bouton_valider.grid(row=len(labels_deux), column=1, pady=20)

# ---- Fenêtre principale ----

fenetre = tk.Tk()
fenetre.title("Formulaire Client")
fenetre.geometry("500x300")

labels = ["Nom", "Prenom", "Mail", "Grade", "Reference Acte"]

for i, label_text in enumerate(labels):
    tk.Label(fenetre, text=label_text).grid(row=i, column=0, padx=10, pady=10, sticky="e")
    entry = tk.Entry(fenetre)
    entry.grid(row=i, column=1, padx=10, pady=10, ipadx=50)
    entries[label_text] = entry

tk.Button(fenetre, text="Continuer", command=seconde_fenetre).grid(row=5, column=1, pady=20)

fenetre.mainloop()
















