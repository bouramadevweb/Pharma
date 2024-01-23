# Ma function
def verifier(lettre):
    lettre = lettre.lower()

    if lettre in 'aeiouy':
        return "Voyelle"
    elif lettre in 'bcdfghjklmnpqrstvwxz':
        return "Consonne"
    else:
        return "Caractère non reconnu"


# [input]
caractere = input("Entrez une lettre : ")
# [j'appel ma fonction]
resultat_v = verifier(caractere)

print(f"La lettre '{caractere}' est une {resultat_v}.")
