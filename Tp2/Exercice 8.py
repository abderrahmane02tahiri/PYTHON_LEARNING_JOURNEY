# Demander à l'utilisateur de saisir une liste de nombres
entree = input("Saisissez une liste de nombres séparés par des virgules : ")
L = [int(x) for x in entree.split(",")]
valeur_a_rechercher = int(input("Saisissez la valeur à rechercher : "))

def rechercher_occurrences(L, val):
    occurrences = [i for i, x in enumerate(L) if x == val]
    return len(occurrences), occurrences

nombre_occurrences, indices = rechercher_occurrences(L, valeur_a_rechercher)
print(f"Nombre d'occurrences : {nombre_occurrences}")
print(f"Indices des occurrences : {indices}")
