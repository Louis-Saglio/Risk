import ia.base_ai
import data.data_content
import random
import sample.territoire as trt


class IaForTest(ia.base_ai.AI):

    def choose_continue_attack(self, attacker: trt.Territoire, defender: trt.Territoire) -> bool:
        if defender.proprietaire is self.player:
            return False
        return True

    def choose_dice_number(self, attacker: trt.Territoire, defender: trt.Territoire, role: str) -> int:
        return 2

    def choose_target(self) -> dict:
        for territoire in self.player.territoires:
            for voisin in territoire.voisins:
                if voisin.proprietaire is not self.player:
                    return {"attacker": territoire, "defender": voisin}

    def choose_attacker_number(self, attacker: trt.Territoire, defender: trt.Territoire):
        return attacker.nbr_unites

    def choose_reinforcements_placement(self, reinforcements_number: int) -> dict:
        return {self.player.territoires[0]: reinforcements_number}

    def choose_card_set(self) -> [tuple, None]:
        if len(self.player.cards) < 3:
            return None
        for _ in range(20):
            card_set = tuple(random.sample([territoire.icone for territoire in self.player.territoires], 3))
            if card_set in data.data_content.CARD_SETS:
                return card_set
