class Continent:

    def __init__(self, nom, renforts: int, manager, territoires: tuple=()):
        self.nom = nom
        self.territoires = territoires  # type: tuple[sample.territoire.Territoire]
        self.renforts = renforts
        self.manager = manager
        self.manager.continents.append(self)
        # noinspection PyNoneFunctionAssignment
        self.owner = self.get_master()

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
        if not self.territoires:
            return None
        for territoire in self.territoires[1::]:
            if territoire.proprietaire is not self.territoires[0].proprietaire:
                return None
        if self.territoires:
            return self.territoires[0].proprietaire

    def change_owner(self, new_owner):
        if self.owner is not None:
            self.owner.continents.remove(self)
            self.owner = new_owner
            self.owner.continents.append(self)
        else:
            self.owner = new_owner

    def manage_owner(self):
        self.change_owner(self.get_master())
