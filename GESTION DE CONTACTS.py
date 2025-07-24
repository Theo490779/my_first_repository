# GESTION DE CONTACTS
import tkinter as tk
from tkinter import ttk, messagebox
def gestion_contact():
    name = entries['Name'].get().strip()
    phone = entries['Phone'].get().strip()
    email = entries['Email'].get().strip()
    if not name or not phone or not email:
        messagebox.showerror("Error","Please fill in all fields")
        return
    table.insert('','end', values=(name,phone,email))
    

def clique_tableau(event):
    # Récupère l'item sélectionné
    item = table.selection()[0]

    # Récupère les valeurs de la ligne
    values = table.item(item, 'values')

    # Remplit les champs avec les valeurs
    entries['Name'].delete(0, tk.END)
    entries['Name'].insert(0, values[0])  # Nom



premier_interface = tk.Tk()
premier_interface.title('Contacts')
premier_interface.geometry('400x300')

entries = {}
label = ['Name','Phone_number','Email']
for i,elemet in enumerate (label):
    tk.Label(premier_interface, text=elemet).grid(row=i, column=0, padx=10, pady=10,sticky="e")
    entry = tk.Entry(premier_interface)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entries[elemet] = entry
tk.Button(premier_interface, text='Add', command=gestion_contact).grid(row=3, column=0, padx=10, pady=10)
tk.Button(premier_interface,text='Delete',command='None').grid(row=3, column=4, padx=10, pady=10)
colone = ('Nom','Téléphone','E-mail' )
table = ttk.Treeview(premier_interface, columns=colone,show='headings', height=15)
for col in colone:
    table.heading(col, text=col)
    table.column(col, width=120)
    

premier_interface.mainloop()