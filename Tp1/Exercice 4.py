
secondes = float(input("entrez le nombre de seconde a convertire : "))


heures = secondes // 3600
secondes_restantes = secondes % 3600
minutes = secondes_restantes // 60
secondes_finales = secondes_restantes % 60

print(f"{secondes} secondes = {heures}h {minutes}min {secondes_finales}sec")
