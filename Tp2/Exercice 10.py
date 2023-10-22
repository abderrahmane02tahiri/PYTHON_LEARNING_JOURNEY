# Demander à l'utilisateur de saisir deux listes de nombres
entree1 = input("Saisissez la première liste de nombres séparés par des virgules : ")
L1 = [int(x) for x in entree1.split(",")]
entree2 = input("Saisissez la deuxième liste de nombres séparés par des virgules : ")
L2 = [int(x) for x in entree2.split(",")]

L3 = list(set(L1) & set(L2))
print(L3)
