import ia.randomAI
import data
import sample.territoire
import sample.armee
import sample.plateau

print(sample.plateau)
print(sample.continent)
print(sample.armee)


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
        return len(self.territoires) // 3

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
        for territoire, unit_number in placement:
            territoire.nbr_unites += unit_number

    def manage_reinforcements(self):
        self._place_reinforcements(self._get_reinforcements_number())

    def _attack_one_target(self, attacker: sample.territoire.Territoire, defender: sample.territoire.Territoire):
        attacker.armee.choisir_nbr_des = self.ai.choose_dice_number
        defender.armee.choisir_nbr_des = defender.proprietaire.ai.choose_dice_number
        while True:
            attacker.former_armee()
            defender.former_armee()
            attacker.armee.initialise_attaque(defender)
            attacker.armee.attaquer()
            if self.ai.choose_continue_attack(attacker, defender) is False:
                break
        attacker.nbr_unites = attacker.armee.nbr
        defender.nbr_unites = defender.armee.nbr

    def manage_attacks(self):
        while True:
            ai_data = self.ai.choose_target()
            if ai_data is None:
                break
            self._attack_one_target(**ai_data)

    def play(self):
        self.manage_reinforcements()
        self.manage_attacks()
