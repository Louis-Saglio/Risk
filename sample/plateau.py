class PlateauError(BaseException):
    pass


class Plateau:

    def __init__(self):
        self.continents = ()
        self.territoires = ()

    # def __repr__(self):
    #     return "Plateau::" + str(id(self))
    #
    # def __str__(self):
    #     return self.__repr__()
