def inserer_valeur(L, val):
    index = 0
    while index < len(L) and L[index] < val:
        index += 1
    L.insert(index, val)

L = [1, 3, 5, 7, 9]
valeur_a_inserer = 4
inserer_valeur(L, valeur_a_inserer)
print(L)
