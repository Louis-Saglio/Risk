class Continent:

    def __init__(self, nom, renforts: int, plateau, territoires: tuple=()):
        self.nom = nom
        self.territoires = territoires
        self.renforts = renforts
        self.plateau = plateau
        self.plateau.continent += self,

    def __str__(self):
        # return f"{self.nom} {id(self.plateau)}"
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
