import pandas as pd

def calculatrice_addition_enregistrement_csv():
    try:
        # Saisie des nombres à additionner
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        # Effectuer l'addition
        resultat = nombre1 + nombre2

        # Afficher le résultat intermédiaire
        print(f"Résultat intermédiaire : {nombre1} + {nombre2} = {resultat}")

        # Enregistrer le résultat dans le fichier bcoul.csv
        chemin_fichier_sortie = 'bcoul.csv'
        df = pd.DataFrame({'nombre1': [nombre1], 'nombre2': [nombre2], 'resultat': [resultat]})
        df.to_csv(chemin_fichier_sortie, mode='a', header=not pd.read_csv(chemin_fichier_sortie).index.any(), index=False)

        print("Opération terminée avec succès. Résultat enregistré dans", chemin_fichier_sortie)
    # gestion des erreur
    except ValueError:
        print("Erreur : Veuillez saisir des nombres valides.")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

# Exemple d'utilisation
calculatrice_addition_enregistrement_csv()
 