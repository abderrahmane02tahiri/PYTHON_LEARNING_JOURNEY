def supprimer_occurrences(L, val):
    L[:] = [x for x in L if x != val]

L = [1, 2, 3, 4, 2, 5, 2]
valeur_a_supprimer = 2
supprimer_occurrences(L, valeur_a_supprimer)
print(L)
