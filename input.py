# [function]
def voyelle_ou_consonne(): 
    """_summary_

    Returns:
        _type_: _description_
    """
    lettre = input("Entrez une lettre : ").lower()

    if lettre in 'aeiouy':
        return "Voyelle"
    elif lettre in 'bcdfghjklmnpqrstvwxz':
        return "Consonne"
    else:
        return "Caractère non reconnu"
# [result]    
resultat = voyelle_ou_consonne()
print(f"La lettre saisie est une {resultat}.")
