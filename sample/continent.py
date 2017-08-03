import sample.territoire


class Continent:

    def __init__(self, nom, renforts: int, plateau, territoires: tuple=()):
        self.nom = nom
        self.territoires = territoires  # type: tuple[sample.territoire.Territoire]
        self.renforts = renforts
        self.plateau = plateau
        self.plateau.continent += self,

    def __str__(self):
        # return f"{self.nom} {id(self.plateau)}"
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def get_master(self):
        """
        Si self est possédé par un seul joueur renvoi ce joueur.
        Sinon renvoi None
        """
        # TODO test
        for territoire in self.territoires[1::]:
            if territoire.proprietaire is not self.territoires[0].proprietaire:
                return None
        return self.territoires[0].proprietaire
