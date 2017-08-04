import ia.randomAI
import data
import sample.territoire
import random


def roll_dice(nbr: int) -> list:
    # TODO: nbr des dans settings
    dice = [random.randint(1, 6) for _ in range(nbr)]
    dice.sort(reverse=True)
    return dice

def compare_dice(attacker_dice: list, defender_dice: list):
    nbr_dead = {"attacker": 0, "defender": 0}
    for attacker_die, defender_die in zip(attacker_dice, defender_dice):
        if attacker_die > defender_die:
            nbr_dead["defender"] += 1
        else:
            nbr_dead["attacker"] += 1
    return nbr_dead

def get_attack_winner(attacker: sample.territoire.Territoire, defender: sample.territoire.Territoire):
    if attacker.nbr_unites == 1:
        return defender
    if defender.nbr_unites == 0:
        return attacker

class PlayerError(BaseException):
    pass


class Player:
    """
    Contient les actions possible pour un joueur
    Ne doit pas contenir de prise de décision (AI)
    """

    def __init__(self, plateau):
        self.territoires = []
        self.plateau = plateau
        self.cards = []
        self.ai = ia.randomAI.RandomAi(self)

    def __get_continent_reinforcements(self) -> int:
        # TODO: self.continents_possedes
        renforts = 0
        for continent in self.plateau.continent:
            if continent.get_master() is self:
                renforts += continent.renforts
        return renforts

    def __get_territory_number_reinforcements(self) -> int:
        number = len(self.territoires) // 3
        return number if number >= 3 else 3

    def __get_card_set_reinforcements(self) -> int:
        return data.data_content.CARD_SETS.get(self.ai.choose_card_set()) or 0

    def _get_reinforcements_number(self) -> int:
        reinforcements = (
            self.__get_continent_reinforcements(),
            self.__get_territory_number_reinforcements(),
            self.__get_card_set_reinforcements()
        )
        return sum(reinforcements)

    def _place_reinforcements(self, unit_number):
        placement = self.ai.choose_reinforcements_placement(unit_number)
        for territoire, unit_number in placement.items():
            territoire.nbr_unites += unit_number

    def manage_reinforcements(self):
        self._place_reinforcements(self._get_reinforcements_number())

    def __one_round_attack(self, attacker: sample.territoire.Territoire, defender: sample.territoire.Territoire):
        attacker_nbr_dice = self.ai.choose_dice_number(attacker, defender, "attacker")
        defender_nbr_dice = defender.proprietaire.ai.choose_dice_number(attacker, defender, "defender")
        attacker_dice = roll_dice(attacker_nbr_dice)
        defender_dice = roll_dice(defender_nbr_dice)
        nbr_dead = compare_dice(attacker_dice, defender_dice)
        attacker.nbr_unites -= nbr_dead["attacker"]
        defender.nbr_unites -= nbr_dead["defender"]

    def _attack_one_target(self, attacker: sample.territoire.Territoire, defender: sample.territoire.Territoire):
        while get_attack_winner(attacker, defender) is None:
            self.__one_round_attack(attacker, defender)
            if not self.ai.choose_continue_attack(attacker, defender):
                break
        if get_attack_winner(attacker, defender) is attacker:
            defender.change_owner(attacker.proprietaire)
            # TODO: give a card attention aux import récursifs !

    def manage_attacks(self):
        while True:
            target_data = self.ai.choose_target()
            if target_data is None:
                break
            self._attack_one_target(**target_data)

    def play(self):
        self.manage_reinforcements()
        self.manage_attacks()
