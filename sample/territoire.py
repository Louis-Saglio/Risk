from plateau import PlateauError
import continent
import armee
import sample
import sample.player


class TerritoireError(BaseException):
    pass


class Territoire:

    def __init__(self, nom, plateau, continent, icone):
        self.plateau = plateau
        self.nom = nom
        self.icone = icone
        self.continent = self.find_continent_by_name(continent)
        self.continent.territoires += self,
        self.proprietaire = None  # :type sample.player.Player
        self.nbr_unites = 0
        self.voisins = ()
        self.armee = None
        self.check_attr()

    def check_attr(self):
        if not isinstance(self.continent, sample.continent.Continent):
            raise PlateauError(f"{self.continent}, {type(self.continent)}, {continent.Continent}")

    def find_continent_by_name(self, name):
        if isinstance(name, sample.continent.Continent):
            return name
        for cont in self.plateau.continent:
            if cont.nom == name:
                return cont
        raise PlateauError(f"Aucun continent '{name}' trouvé dans le plateau {self.plateau}\n"
                           f"Nom(s) disponibles : {[plt.nom for plt in self.plateau.continent]}")

    def link_with(self, other):
        """
        :type other Territoire
        """
        self.voisins += other,
        other.voisins += self,

    def former_armee(self, nbr=None) -> armee.Armee:
        if nbr is None:
            nbr = self.nbr_unites
        elif nbr > self.nbr_unites:
            raise TerritoireError
        self.armee = armee.Armee(nbr)
        return self.armee

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
