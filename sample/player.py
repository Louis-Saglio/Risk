from typing import Type
import ia.base_ai
import sample.territoire as trt
import sample.armee as arm
import random
import engine.game_manager as gm
import missions.base_mission
from armee import PERDANT


class PlayerError(BaseException):
    pass


class Player:
    """
    Contient les actions possible pour un joueur
    Ne doit pas contenir de prise de décision (AI)
    """

    def __init__(self, manager: gm.GameManager, ai: Type[ia.base_ai.AI]=None, color: str=None, mission=None):
        # todo: name unique, change_manager(), add/remove_territoire/continent/card, classe mere
        self.manager = manager
        self.manager.players.append(self)
        self.color = color
        self.territoires = []
        self.continents = []
        self.cards = []
        if isinstance(ai, type) and issubclass(ai, ia.base_ai.AI):
            self.ai = ai(self)
        else:
            self.ai = ai
        if isinstance(mission, type) and issubclass(mission, missions.base_mission.BaseMission):
            self.mission = mission(self)
        else:
            self.mission = mission

    def __get_continent_reinforcements(self) -> int:
        return sum([continent.renforts for continent in self.continents])

    def __get_territory_number_reinforcements(self) -> int:
        number = len(self.territoires) // 3
        return number if number >= 3 else 3

    def __get_card_set_reinforcements(self) -> int:
        return self.manager.card_sets.get(self.ai.choose_card_set()) or 0

    def _get_reinforcements_number(self) -> int:
        reinforcements = (
            self.__get_continent_reinforcements(),
            self.__get_territory_number_reinforcements(),
            self.__get_card_set_reinforcements()
        )
        return sum(reinforcements)

    def _place_reinforcements(self, unit_number: int):
        placement = self.ai.choose_reinforcements_placement(unit_number)
        for territoire, unit_number in placement.items():
            territoire.nbr_unites += unit_number

    def manage_reinforcements(self):
        self._place_reinforcements(self._get_reinforcements_number())

    def draw_a_card(self):
        self.cards.append(self.manager.give_a_card())

    @staticmethod
    def _attack_one_target(attacker: trt.Territoire, defender: trt.Territoire):
        attacker.former_armee()
        defender.former_armee()
        attacker.armee.territoire = attacker
        defender.armee.territoire = defender
        attacker.armee.initialise_attaque(defender.armee)
        attacker.armee.envahir(defender.armee)

    @staticmethod
    def _end_attack(attacker: trt.Territoire, defender: trt.Territoire):
        attacker.nbr_unites = attacker.armee.nbr
        defender.nbr_unites = defender.armee.nbr
        if defender.armee.statut is PERDANT:
            defender.change_owner(attacker.proprietaire)

    def manage_attacks(self):
        nbr_trt = len(self.territoires)
        while True:
            target = self.ai.choose_target()
            if target is None:
                break
            self._attack_one_target(**target)
            self._end_attack(**target)
        if len(self.territoires) - nbr_trt > 0:
            self.draw_a_card()

    def manage_troop_transfers(self):
        ai_data = self.ai.choose_troop_transfer()
        ai_data["from_trt"].transfer_troops_to(ai_data["to_trt"], ai_data["nbr_units"])

    def play(self):
        self.manage_reinforcements()
        self.manage_attacks()
        self.manage_troop_transfers()
        self.mission.is_accomplished()
