class Territoire:

    def __init__(self, nom, continent):
        if not isinstance(continent, Continent):
            pass
        self.nom = nom
        self.continent = continent
        self.proprietaire = None
        self.nbr_unitees = 0
        self.voisins = ()

    def link_with(self, other):
        """
        :type other Territoire
        """
        self.voisins += other,
        other.voisins += self,


class Continent:

    def __init__(self, nom, renforts: int, plateau: Plateau, territoires: tuple=()):
        self.nom = nom
        self.territoires = territoires
        self.renforts = renforts
        self.plateau = plateau


class Plateau:

    def __init__(self):
        self.continent = []
        self.territoires = []
