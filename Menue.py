from tkinter import ttk ,Tk
from tkinter import * 
from tkinter import messagebox
from subprocess import call

# Function ACHAT
def ACHATS():
    root.destroy()
    call(["PYTHON","ACHAT"])
#Function Vente
def VENTES():
    root.destroy()
    call(["PYTHON","VENTES"])
    
#Ma fenêtre
root = Tk()



root.title("Gest de stock")

root.geometry("600x200+400+200")

root.resizable(False,False)
root.config(background="#808080")

#ajout de titre
lbltitre = Label(root,borderwidth=3, relief=SUNKEN,text="GESTION DES ACHAT",font=("Sans serif",25),background="#483D88",foreground="white")
lbltitre.place(x=0,y=0,width=600)

#Bouton achat
btnachat = Button(root,text="ACHATS",font=("arial",24),bg="#483D88",fg="white", command=ACHATS)
btnachat.place(x=100 , y=100 ,width=200)

btnVente =Button(root,text="VENTE",font=("arial",24),bg="#483D88",fg="white",command=VENTES)
btnVente.place(x=350,y=100,width=200)
root.mainloop()