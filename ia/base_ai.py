class AI:
    """
    Contient l'interface de base pour les AI
    """

    def __init__(self, player):
        """
        :type player: player.Player
        """
        self.player = player

    def choisir_cible(self):
        raise NotImplementedError

    def effectuer_transfert(self):
        raise NotImplementedError
