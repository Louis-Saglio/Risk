import ia


class PlayerError(BaseException):
    pass


class Player:
    """
    Contient les actions possible pour un joueur
    Ne doit pas contenir de prise de décision (AI)
    """
    def __init__(self):
        self.unites_disponibles = 0
        self.ai = ia.base_ai.AI(self)

    def placer_unite(self):
        if self.unites_disponibles < 1:
            raise PlayerError
        self.unites_disponibles -= 0
        self.ai.placer_unite().nbr_unites += 1

    def attaquer_territoire(self, origine, territoire):
        """
        :type origine: territoire.Territoire
        :type territoire territoire.Territoire
        """
        armee_attaquant = origine.former_armee(self.ai.choisir_nbr_attaquants())
        armee_defenseur = territoire.former_armee(territoire.nbr_unites)
        armee_attaquant.initialise_attaque(armee_defenseur)
        armee_attaquant.attaquer()
