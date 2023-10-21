
notes = [float(input(f"Saisir la note {i + 1} : ")) for i in range(4)]
coefficients = [int(input(f"Saisir le coefficient de la note {i + 1} : ")) for i in range(4)]

somme_produits = sum(notes[i] * coefficients[i] for i in range(4))
somme_coefficients = sum(coefficients)
moyenne = somme_produits / somme_coefficients

# Affichage de la moyenne
print(f"\n Moyenne des notes : {moyenne:.2f}")

# Vérification de la validation du semestre
if moyenne >= 10:
    print("Semestre validé")
elif moyenne >= 7:
    print("Rattrapage")
else:
    print("Semestre non validé")

