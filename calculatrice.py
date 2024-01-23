import os
import pandas as pd

def addition_et_enregistrement():
    try:
        # Saisir les valeurs de l'utilisateur
        valeur1 = float(input("Entrez la première valeur : "))
        valeur2 = float(input("Entrez la deuxième valeur : "))
    except ValueError:
        print("Erreur : Veuillez entrer des valeurs numériques.")
        return None

    # Effectuer l'addition
    resultat = valeur1 + valeur2

    # Créer un DataFrame avec les valeurs
    data = {'Valeur1': [valeur1], 'Valeur2': [valeur2], 'Résultat': [resultat]}
    df = pd.DataFrame(data)

    # Définir le nom du répertoire par défaut
    repertoire = 'resultats_directory'

    # Créer le répertoire s'il n'existe pas
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    # Définir le nom du fichier CSV par défaut
    fichier_csv = os.path.join(repertoire, 'resultats.csv')

    try:
        # Ajouter le DataFrame au fichier CSV ou le créer s'il n'existe pas
        df.to_csv(fichier_csv, mode='a', header=not os.path.isfile(fichier_csv), index=False)
    except Exception as e:
        print(f"Erreur lors de l'enregistrement dans le fichier CSV : {e}")
        return None

    # Retourner le résultat de l'addition
    return resultat

# Exemple d'utilisation
resultat = addition_et_enregistrement()

def main():
    if resultat is not None:
        print(f"Le résultat de l'addition a été enregistré dans le répertoire 'resultats_directory'.")
    else:
        print("Opération annulée en raison d'une erreur.")

# Appel de la fonction main
main()
