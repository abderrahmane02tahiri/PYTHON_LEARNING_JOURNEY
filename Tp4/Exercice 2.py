class Batiment:
    def __init__(self, adresse):
        self.adresse = adresse

    def get_adresse(self):
        return self.adresse

    def set_adresse(self, adresse):
        self.adresse = adresse

    def __str__(self):
        return f"Batiment à l'adresse : {self.adresse}"


class Maison(Batiment):
    def __init__(self, adresse, nbPieces):
        super().__init__(adresse)
        self.nbPieces = nbPieces

    def get_nbPieces(self):
        return self.nbPieces

    def set_nbPieces(self, nbPieces):
        self.nbPieces = nbPieces

    def __str__(self):
        return f"Maison à l'adresse : {self.adresse}, {self.nbPieces} pièces"


class Immeuble(Batiment):
    def __init__(self, adresse, nbAppart):
        super().__init__(adresse)
        self.nbAppart = nbAppart

    def get_nbAppart(self):
        return self.nbAppart

    def set_nbAppart(self, nbAppart):
        self.nbAppart = nbAppart

    def __str__(self):
        return f"Immeuble à l'adresse : {self.adresse}, {self.nbAppart} appartements"


# Test de la classe Batiment
batiment = Batiment("ain ati 2")
print(batiment)

# Test de la classe Maison
maison = Maison("errachidia", 5)
print(maison)
print(f"Nombre de pièces: {maison.get_nbPieces}")

# Test de la classe Immeuble
immeuble = Immeuble("casa ain sbaa", 10)
print(immeuble)
print(f"Nombre d'appartements: {immeuble.get_nbAppart()}")
