nombre1 = float(input("Veuillez saisir le premier nombre : "))
nombre2 = float(input("Veuillez saisir le deuxième nombre : "))

if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
    print("Le produit des deux nombres sera positif")
elif nombre1 == 0 or nombre2 == 0:
    print("Le produit des deux nombres est nul")
else:
    print("Le produit des deux nombres sera négatif")
