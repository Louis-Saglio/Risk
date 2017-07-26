from random import choice, randint

import base_ai


class RandomAi(base_ai.AI):

    def effectuer_transfert(self):
        dep = choice(self.player.territoires)
        """:type dep plateau.Territoire"""
        arrv = choice(dep.voisins)
        nbr = randint(0, dep.nbr_unitees)

    def choisir_cible(self):
        pass
