import tkinter as tk
from tkinter import messagebox

# Modèle
class Produit: #[Class Produit]
    """produit"""
    def __init__(self, nom, categorie, quantite):
        self.nom = nom
        self.categorie = categorie
        self.quantite = quantite

class StockModel: #[Class Stock Model]
    """Stock Model"""
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def supprimer_produit(self, index):
        del self.produits[index]

# Vue
class StockView(tk.Tk): #[Class StockView]
    """Stock View"""
    def __init__(self, controller):
        super().__init__()
        self.title("Gestion de Stock")
        self.geometry("1300x700")

        self.controller = controller

        # Initialiser l'interface après que le contrôleur ait été correctement lié
        self.creer_interface()

    def creer_interface(self):
        # Widgets de la fenêtre
        self.label_nom = tk.Label(self, text="Nom du Produit:")
        self.entry_nom = tk.Entry(self)

        self.label_categorie = tk.Label(self, text="Catégorie:")
        self.entry_categorie = tk.Entry(self)

        self.label_quantite = tk.Label(self, text="Quantité:")
        self.entry_quantite = tk.Entry(self)

        self.bouton_ajouter = tk.Button(self, text="Ajouter Produit", command=self.controller.ajouter_produit)
        self.bouton_afficher = tk.Button(self, text="Afficher Stock", command=self.controller.afficher_stock)

        self.listbox_stock = tk.Listbox(self, height=10, width=50)
        self.bouton_modifier = tk.Button(self, text="Modifier Produit", command=self.controller.modifier_produit)
        self.bouton_supprimer = tk.Button(self, text="Supprimer Produit", command=self.controller.supprimer_produit)

        # Placement des widgets
        self.label_nom.pack(pady=5)
        self.entry_nom.pack(pady=5)

        self.label_categorie.pack(pady=5)
        self.entry_categorie.pack(pady=5)

        self.label_quantite.pack(pady=5)
        self.entry_quantite.pack(pady=5)

        self.bouton_ajouter.pack(pady=10)
        self.bouton_afficher.pack(pady=10)

        self.listbox_stock.pack(pady=10)
        self.bouton_modifier.pack(pady=5)
        self.bouton_supprimer.pack(pady=5)

        self.reset_champs()  # Appel à la méthode pour initialiser les champs

    def reset_champs(self):
        self.entry_nom.delete(0, tk.END)
        self.entry_categorie.delete(0, tk.END)
        self.entry_quantite.delete(0, tk.END)

        # Mettre à jour la référence du contrôleur dans la vue après l'initialisation des boutons
        self.controller.view = self
        self.bouton_ajouter.config(command=self.controller.ajouter_produit)
        self.bouton_afficher.config(command=self.controller.afficher_stock)
        self.bouton_modifier.config(command=self.controller.modifier_produit)
        self.bouton_supprimer.config(command=self.controller.supprimer_produit)

# Contrôleur
class StockController: #[Stock controller]
    """Stock Controller"""
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Vérifier si la vue n'est pas None avant de configurer les commandes des boutons
        if self.view is not None:
            self.view.bouton_ajouter.config(command=self.ajouter_produit)
            self.view.bouton_afficher.config(command=self.afficher_stock)
            self.view.bouton_modifier.config(command=self.modifier_produit)
            self.view.bouton_supprimer.config(command=self.supprimer_produit)

    # ... (restez inchangé)


    def ajouter_produit(self):
        nom = self.view.entry_nom.get()
        categorie = self.view.entry_categorie.get()
        quantite = self.view.entry_quantite.get()

        if nom and categorie and quantite:
            produit = Produit(nom, categorie, quantite)
            self.model.ajouter_produit(produit)

            messagebox.showinfo("Succès", "Produit ajouté avec succès!")
            self.view.reset_champs()
            self.afficher_stock()
        else:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")

    def afficher_stock(self):
        self.view.listbox_stock.delete(0, tk.END)
        if self.model.produits:
            for i, produit in enumerate(self.model.produits, start=1):
                self.view.listbox_stock.insert(tk.END, f"{i}. Nom: {produit.nom}, Catégorie: {produit.categorie}, Quantité: {produit.quantite}")
        else:
            self.view.listbox_stock.insert(tk.END, "Le stock est vide.")

    def modifier_produit(self):
        selected_index = self.view.listbox_stock.curselection()
        if selected_index:
            selected_index = selected_index[0]
            produit = self.model.produits[selected_index]

            messagebox.showinfo("Détails du Produit", f"Nom: {produit.nom}\nCatégorie: {produit.categorie}\nQuantité: {produit.quantite}")
        else:
            messagebox.showwarning("Sélection nécessaire", "Veuillez sélectionner un produit à modifier.")

    def supprimer_produit(self):
        selected_index = self.view.listbox_stock.curselection()
        if selected_index:
            selected_index = selected_index[0]
            produit = self.model.produits[selected_index]

            confirmation = messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer le produit {produit.nom}?")
            if confirmation:
                self.model.supprimer_produit(selected_index)
                messagebox.showinfo("Succès", "Produit supprimé avec succès!")
                self.afficher_stock()
        else:
            messagebox.showwarning("Sélection nécessaire", "Veuillez sélectionner un produit à supprimer.")


# Point d'entrée
if __name__ == "__main__":
    model = StockModel()
    controller = StockController(model, None)  # Remplacez 'None' par votre instance de vue si nécessaire
    view = StockView(controller)
    view.mainloop()

