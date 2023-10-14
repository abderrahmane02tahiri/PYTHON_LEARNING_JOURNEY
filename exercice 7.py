nombre1 = float(input("Veuillez saisir le premier nombre : "))
nombre2 = float(input("Veuillez saisir le deuxième nombre : "))
operation = input("Veuillez saisir l'opération (+, -, *, /) : ")

if operation == '+':
    resultat = nombre1 + nombre2
    print(f"Le résultat de l'addition est : {resultat}")
elif operation == '-':
    resultat = nombre1 - nombre2
    print(f"Le résultat de la soustraction est : {resultat}")
elif operation == '*':
    resultat = nombre1 * nombre2
    print(f"Le résultat de la multiplication est : {resultat}")
elif operation == '/':
    if nombre2 == 0:
        print("Erreur : Division par zéro.")
    else:
        resultat = nombre1 / nombre2
        print(f"Le résultat de la division est : {resultat}")
else:
    print("Opération non valide. Veuillez saisir l'une des opérations suivantes : +, -, *, /")
