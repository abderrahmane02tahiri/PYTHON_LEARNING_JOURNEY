import random


def jeu_deviner_nombre():
    nombre_a_deviner = random.randint(1, 100)
    nombre_d_essais = 0

    print("On va jouer à un petit jeu, je vais générer un nombre entre 1 et 100 et tu vas le deviner en 7 essais.")

    while nombre_d_essais < 7:
        essai = input(">>> ")

        if not essai.isdigit():
            print("Oups, vous avez saisi un nombre en dehors de l'intervalle.")
            continue

        essai = int(essai)

        if essai < 1 or essai > 100:
            print("Oups, vous avez saisi un nombre en dehors de l'intervalle.")
        elif essai < nombre_a_deviner:
            print("Oups, entrez un nombre plus grand !")
            nombre_d_essais += 1
        elif essai > nombre_a_deviner:
            print("Oups, entrez un nombre plus petit !")
            nombre_d_essais += 1
        else:
            nombre_d_essais += 1
            print(f"Bravo, {essai} est le nombre que j'ai choisi. Vous l'avez deviné en {nombre_d_essais} essais.")
            break
    else:
        print("J'ai gagné, je suis le meilleur. Le nombre que j'ai choisi est", nombre_a_deviner)
    print("Au revoir!")


jeu_deviner_nombre()
