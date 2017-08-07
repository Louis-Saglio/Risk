import sample.armee
import sample.continent
import engine.game_manager as gm


class TerritoireError(BaseException):
    pass


class Territoire:

    def __init__(self, nom, manager, continent, icone):
        # TODO: changer les tuples en list
        self.manager = manager
        self.nom = nom
        self.icone = icone
        self.continent = self.manager.find_continent_by_name(continent)
        self.continent.territoires += self,
        self.proprietaire = None  # :type sample.player.Player
        self.nbr_unites = 0
        self.voisins = ()
        self.armee = None
        self.check_attr()

    def check_attr(self):
        if not isinstance(self.continent, sample.continent.Continent):
            raise sample.plateau.PlateauError(f"{self.continent}, {type(self.continent)}, {sample.continent.Continent}")

    def link_with(self, other):
        """
        :type other: Territoire
        """
        self.voisins += other,
        other.voisins += self,

    def former_armee(self, nbr=None) -> sample.armee.Armee:
        if nbr is None:
            nbr = self.nbr_unites
        elif nbr > self.nbr_unites:
            raise TerritoireError
        self.armee = sample.armee.Armee(nbr)
        return self.armee

    def change_owner(self, new_owner):
        if self.proprietaire is not None:
            self.proprietaire.territoires.remove(self)
        self.proprietaire = new_owner
        new_owner.territoires.append(self)

    def transfer_troops_to(self, to, nbr: int):
        """
        :param nbr:
        :type to: Territoire
        """
        self.nbr_unites -= nbr
        to.nbr_unites += nbr

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
