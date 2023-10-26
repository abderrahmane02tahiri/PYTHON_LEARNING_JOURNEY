class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle(Point):
    def __init__(self, x, y, longueur, largeur):
        super().__init__(x, y)
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def __str__(self):
        return f"Rectangle({self.x}, {self.y}, {self.longueur}, {self.largeur})"


class Parallelepipede(Rectangle):
    def __init__(self, x, y, longueur, largeur, hauteur):
        super().__init__(x, y, longueur, largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, hauteur):
        self.hauteur = hauteur

    def aire(self):
        base = super().aire()
        return 2 * (base + self.longueur * self.hauteur + self.largeur * self.hauteur)

    def volume(self):
        return super().aire() * self.hauteur

    def __str__(self):
        return f"Parallelepipede({self.x}, {self.y}, {self.longueur}, {self.largeur}, {self.hauteur})"



# Test de la classe Point
point = Point(1, 2)
print(point)
print(f"Point x: {point.get_x()}, y: {point.get_y()}")

# Test de la classe Rectangle
rectangle = Rectangle(3, 4, 5, 6)
print(rectangle)
print(f"Longueur: {rectangle.get_longueur()}, Largeur: {rectangle.get_largeur()}")
print(f"Aire du rectangle: {rectangle.aire()}")

# Test de la classe Parallelepipede
parallelepiped = Parallelepipede(7, 8, 9, 10, 11)
print(parallelepiped)
print(f"Hauteur: {parallelepiped.get_hauteur()}")
print(f"Aire du parallelepiped: {parallelepiped.aire()}")
print(f"Volume du parallelepiped: {parallelepiped.volume()}")
