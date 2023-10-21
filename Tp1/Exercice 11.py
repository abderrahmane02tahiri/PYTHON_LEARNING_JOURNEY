
poids = float(input("Veuillez saisir votre poids en kilogrammes : "))
taille = float(input("Veuillez saisir votre taille en mètres : "))

imc = poids / (taille ** 2)

interpretation = ""
if imc > 40:
    interpretation = "obésité morbide ou massive"
elif imc >= 35:
    interpretation = "obésité sévère"
elif imc >= 30:
    interpretation = "obésité modérée"
elif imc >= 25:
    interpretation = "surpoids"
elif imc >= 18.5:
    interpretation = "corpulence normale"
elif imc >= 16.5:
    interpretation = "maigreur"
else:
    interpretation = "famine"

print(f"\nVotre IMC est : {imc:.2f}")
print("Interprétation de l'IMC :", interpretation)
