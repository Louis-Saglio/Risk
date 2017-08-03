import base_ai
import data.data_content
import random
import sample.territoire


class IaForTest(base_ai.AI):

    def choose_attacker_number(self, attacker: sample.territoire.Territoire, defender: sample.territoire.Territoire):
        pass

    def choose_reinforcements_placement(self, reinforcements_number: int) -> dict:
        return {self.player.territoires[0]: reinforcements_number}

    def choose_card_set(self) -> [tuple, None]:
        if len(self.player.territoires) < 3:
            return None
        for _ in range(20):
            card_set = tuple(random.sample([territoire.icone for territoire in self.player.territoires], 3))
            if card_set in data.data_content.CARD_SETS:
                return card_set
