class Continent:

    def __init__(self, nom, renforts: int, plateau, territoires: tuple=()):
        self.nom = nom
        self.territoires = territoires
        self.renforts = renforts
        self.plateau = plateau
        self.plateau.continents += self,