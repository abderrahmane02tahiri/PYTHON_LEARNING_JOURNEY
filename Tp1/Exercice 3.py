distance = float(input("saisir la distance"))
temps = float(input("saisir le temps"))

if temps == 0:
    temps = 1
vitesse = distance/temps

print("la vitesse est")
print(vitesse)