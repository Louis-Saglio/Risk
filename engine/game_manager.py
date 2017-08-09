from data_reader import create_objects_from_data
import sample.continent


class GameManagerError(BaseException):
    pass


# noinspection PyShadowingNames,PyUnusedLocal
class GameManager:
    def __init__(self):
        self.continents = []

    def give_a_card(self):
        return NotImplementedError

    def find_continent_by_name(self, name):
        if isinstance(name, sample.continent.Continent):
            return name
        for cont in self.continents:
            if cont.nom == name:
                return cont
        raise GameManagerError(f"Aucun continent '{name}' trouvé dans le jeu {self}\n"
                               f"Nom(s) disponibles : {[plt.nom for plt in self.plateau.continent]}")
