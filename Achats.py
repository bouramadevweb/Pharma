import tkinter
from tkinter import ttk ,Tk
from cProfile import label
from tkinter import*
from subprocess import call
from tkinter import messagebox
import mysql.connector


# Ma fenetre 
root =Tk()

root.title("MENUE ACHAT")
root.geometry('1300x700+0+0')
root.resizable(False,False)
root.config(bg='#808080')
#
def Retour():
    root.destroy()
    call(['PYTHON','Principale.py'])

#Ajouter 
#def Ajouter():
    
    
root.mainloop()