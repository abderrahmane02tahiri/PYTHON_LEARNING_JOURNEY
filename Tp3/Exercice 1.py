import math


def somme(m, n):
    total = 0
    if m < n:
        for i in range(m, n + 1):
            total += i
    else:
        for i in range(n, m + 1):
            total += i
    return total


def delta(a, b, c):
    return b ** 2 - 4 * a * c

def NombreRacine(a, b, c):
    D = delta(a, b, c)
    if D > 0:
        return 2
    elif D == 0:
        return 1
    else:
        return 0

def AfficheNombreRacine(a, b, c):
    num_racines = NombreRacine(a, b, c)
    if num_racines == 2:
        print("Il y a 2 solutions.")
    elif num_racines == 1:
        print("Il y a 1 solution.")
    else:
        print("Il n'y a pas de solution réelle.")


def Racine1(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b + math.sqrt(D)) / (2 * a)
    else:
        return None


def Racine2(a, b, c):
    D = delta(a, b, c)
    if D >= 0:
        return (-b - math.sqrt(D)) / (2 * a)
    else:
        return None


def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s


def temps_ecoule(h1, m1, s1, h2, m2, s2):
    temps1 = conversion_temps(h1, m1, s1)
    temps2 = conversion_temps(h2, m2, s2)
    duree = abs(temps1 - temps2)
    return duree


def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100


def vitesse(distance, temps):
    distance_en_metres = conversion_distance(*distance)
    temps_en_secondes = conversion_temps(*temps)
    vitesse_ms = distance_en_metres / temps_en_secondes
    return vitesse_ms


print("Test de la fonction somme:")
print(somme(1, 5))  
print("\nTest de la fonction delta:")
print(delta(1, 5, 6))

print("\nTest de la fonction NombreRacine:")
print(NombreRacine(1, 5, 6))

print("\nTest de la fonction AfficheNombreRacine:")
AfficheNombreRacine(1, 5, 6)

print("\nTest de la fonction Racine1:")
print(Racine1(1, 5, 6))

print("\nTest de la fonction Racine2:")
print(Racine2(1, 5, 6))

print("\nTest de la fonction conversion_temps:")
print(conversion_temps(1, 30, 10))

print("\nTest de la fonction temps_ecoule:")
print(temps_ecoule(1, 30, 10, 0, 45, 20))

print("\nTest de la fonction conversion_distance:")
print(conversion_distance(3, 500, 25))

print("\nTest de la fonction vitesse:")
print(vitesse((3, 500, 25), (0, 45, 20)))