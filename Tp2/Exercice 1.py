# Saisie du chiffre par l'utilisateur
chiffre = int(input("Veuillez saisir un chiffre : "))

# Initialisation de la somme
somme = 0
terme_precedent = 0

# Calcul de la somme
for i in range(1, 5):
    terme = int(str(chiffre) * i)
    somme += terme + terme_precedent
    terme_precedent = terme

# Affichage du résultat
print(f"La somme {chiffre} + {chiffre}{chiffre} + {chiffre}{chiffre}{chiffre} + {chiffre}{chiffre}{chiffre}{chiffre} = {somme}")
