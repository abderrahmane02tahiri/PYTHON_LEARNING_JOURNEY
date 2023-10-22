direction = input("Choisissez la direction (euro en mad ou mad en euro) : ").lower()
conversions = []

while True:
    valeur = float(input("Saisissez une valeur (saisie négative pour arrêter): "))
    if valeur < 0:
        break
    if direction == "euro en mad":
        conversion = valeur * 10.86
    elif direction == "mad en euro":
        conversion = valeur * 0.092
    conversions.append(conversion)

print("Valeurs converties :")
for valeur in conversions:
    print(valeur)
