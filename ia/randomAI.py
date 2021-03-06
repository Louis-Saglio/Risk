from random import choice, randint
import sample.territoire as trt
import ia.base_ai


class RandomAi(ia.base_ai.AI):

    def choose_troop_transfer(self) -> dict:
        territoires = [territoire for territoire in self.player.territoires if territoire.nbr_unites > 1]
        return {"from_trt": choice(territoires), "to_trt": self.player.territoires[0].voisins[0], "nbr_units": 1}

    def choose_attacker_number(self, attacker: trt.Territoire, defender: trt.Territoire) -> int:
        pass

    def choose_target(self) -> dict:
        pass

    def choose_card_set(self) -> tuple:
        pass

    def choose_dice_number(self, attacker: trt.Territoire, defender: trt.Territoire, role: str) -> int:
        pass

    def choose_continue_attack(self, attacker: trt.Territoire, defender: trt.Territoire) -> bool:
        pass

    def choose_reinforcements_placement(self, reinforcements_number: int) -> dict:
        pass

    def effectuer_transfert(self):
        dep = choice(self.player.territoires)
        """:type dep plateau.Territoire"""
        arrv = choice(dep.voisins)
        nbr = randint(0, dep.nbr_unitees)

    def choisir_cible(self):
        pass
