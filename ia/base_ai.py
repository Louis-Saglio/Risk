from territoire import Territoire


class AI:
    """
    Contient l'interface de base pour les AI
    """

    def __init__(self, player):
        """
        :type player: player.Player
        """
        self.player = player

    def placer_unite(self) -> Territoire:
        raise NotImplementedError

    def choisir_nbr_attaquants(self) -> int:
        raise NotImplementedError

    def choisir_cible(self) -> Territoire:
        raise NotImplementedError
