grille_tarifaire = {
    'A': {'taux_horaire': 200, 'prime': 1000, 'heures_par_prime': 20},
    'B': {'taux_horaire': 150, 'prime': 800, 'heures_par_prime': 20},
    'C': {'taux_horaire': 120, 'prime': 500, 'heures_par_prime': 15},
    'D': {'taux_horaire': 100, 'prime': 350, 'heures_par_prime': 15},
    'E': {'taux_horaire': 80, 'prime': 100, 'heures_par_prime': 10}
}

# Saisie du grade et du nombre d'heures travaillées
grade = input("Veuillez saisir le grade (A, B, C, D ou E) : ").upper()
heures_travaillees = float(input("Veuillez saisir le nombre d'heures travaillées : "))

# Vérification si le grade existe dans la grille tarifaire
if grade in grille_tarifaire:
    taux_horaire = grille_tarifaire[grade]['taux_horaire']
    prime_par_heures = grille_tarifaire[grade]['prime'] / grille_tarifaire[grade]['heures_par_prime']
    salaire = (taux_horaire * heures_travaillees) + (prime_par_heures * (heures_travaillees // grille_tarifaire[grade]['heures_par_prime']))
    print(f"\nLe salaire de l'employé de grade {grade} qui a travaillé {heures_travaillees} heures est : {salaire:.2f} DH")
else:
    print("Grade invalide. Veuillez saisir un grade valide (A, B, C, D ou E).")
