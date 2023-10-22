# Demander à l'utilisateur de saisir une liste de nombres
entree = input("Saisissez une liste de nombres séparés par des virgules : ")
L = [int(x) for x in entree.split(",")]
valeur_a_supprimer = int(input("Saisissez la valeur à supprimer : "))

def supprimer_occurrences(L, val):
    L[:] = [x for x in L if x != val]

supprimer_occurrences(L, valeur_a_supprimer)
print(L)
