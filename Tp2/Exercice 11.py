# Demander à l'utilisateur de saisir une liste de nombres
entree = input("Saisissez une liste de nombres séparés par des virgules : ")
L = [int(x) for x in entree.split(",")]
L.reverse()
print(L)
