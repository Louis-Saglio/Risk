from plateau import PlateauError
from continent import Continent


class Territoire:

    def __init__(self, nom, plateau, continent, icone):
        self.plateau = plateau
        self.nom = nom
        self.icone = icone
        self.continent = self.find_continent_by_name(continent)
        self.continent.territoires += self,
        self.proprietaire = None
        self.nbr_unitees = 0
        self.voisins = ()
        self.check_attr()

    def check_attr(self):
        if not isinstance(self.continent, Continent):
            raise PlateauError(f"{self.continent}, {type(self.continent)}")

    def find_continent_by_name(self, name):
        if isinstance(name, Continent):
            return name
        for cont in self.plateau.continents:
            if cont.nom == name:
                return cont
        raise PlateauError(f"Aucun continent '{name}' trouvé dans le plateau {self.plateau}\n"
                           f"Nom(s) disponibles : {[plt.nom for plt in self.plateau.continents]}")

    def link_with(self, other):
        """
        :type other Territoire
        """
        self.voisins += other,
        other.voisins += self,