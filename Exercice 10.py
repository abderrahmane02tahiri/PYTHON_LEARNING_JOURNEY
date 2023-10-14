login = input("Saisir le login : ")
mot_de_passe = input("Saisir le mot de passe : ")

if login == "admin" and mot_de_passe == "admin":
    print("Bienvenue !")
else:
    print("Login et/ou mot de passe incorrect(s).")
