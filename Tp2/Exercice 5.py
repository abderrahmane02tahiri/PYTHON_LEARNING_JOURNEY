# Demander à l'utilisateur de saisir une liste triée de nombres
entree = input("Saisissez une liste triée de nombres séparés par des virgules : ")
L = [int(x) for x in entree.split(",")]
valeur_a_inserer = int(input("Saisissez la valeur à insérer : "))

def inserer_valeur(L, val):
    index = 0
    while index < len(L) and L[index] < val:
        index += 1
    L.insert(index, val)

inserer_valeur(L, valeur_a_inserer)
print(L)
