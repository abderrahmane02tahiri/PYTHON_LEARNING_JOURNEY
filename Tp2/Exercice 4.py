# Demander à l'utilisateur de saisir une liste de nombres séparés par des virgules
entree = input("Saisissez une liste de nombres séparés par des virgules : ")
L = [int(x) for x in entree.split(",")]
M = [x for x in L if x < 0] + [x for x in L if x >= 0]
print(M)
