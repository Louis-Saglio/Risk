import sample.armee
import sample.continent
import engine.game_manager as gm


class TerritoireError(BaseException):
    pass


class Territoire:

    def __init__(self, nom, continent=None, manager=None, icone=None):
        """
        :type manager: game_manager.GameManager
        """
        self.nom = nom
        self.icone = icone
        self.voisins = []
        self.continent = self.change_continent(continent, manager)  # todo: remove_territoire()
        self.proprietaire = None  # :type sample.player.Player
        self.nbr_unites = 0
        self.armee = None
        self.check_attr()

    def check_attr(self):
        if not isinstance(self.continent, sample.continent.Continent):
            raise sample.plateau.PlateauError(f"{self.continent}, {type(self.continent)}, {sample.continent.Continent}")

    def link_with(self, other):
        """
        :type other: Territoire
        """
        self.voisins.append(other)
        other.voisins.append(self)

    def former_armee(self, nbr=None) -> sample.armee.Armee:
        # todo: relocaliser dans checker
        if nbr is None:
            nbr = self.nbr_unites
        elif nbr > self.nbr_unites:
            raise TerritoireError
        self.armee = sample.armee.Armee(nbr)
        return self.armee

    def change_owner(self, new_owner):
        if hasattr(self, "proprietaire") and self.proprietaire is not None:
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

    def change_continent(self, new_continent, manager=None):
        if hasattr(self, "continent"):
            self.continent.territoires.remove(self)
        if isinstance(manager, gm.GameManager):
            self.continent = manager.find_item_from_field_list_by_field("continents", new_continent, "nom")
        elif isinstance(new_continent, sample.continent.Continent):
            self.continent = new_continent
        else:
            raise TerritoireError(f"Vous devez spécifier un continent de type Continent ou un continent de type str et "
                                  f"un manager de type GameManager\nReçu :\n\tContinent : {type(new_continent)}"
                                  f"\n\tManager : {type(manager)}")
        self.continent.territoires.append(self)
        return self.continent

    def __str__(self):
        return str(self.nom) + str(id(self))
        # return str(self.__dict__)

    def __repr__(self):
        return self.__str__()
