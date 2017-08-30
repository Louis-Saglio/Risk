import sample.territoire as trt
import sample.armee as arm

# TODO: test validiter custom ai (check_rules_conformity)
# TODO: gestion des regles fin des combat par manque d'effectif dans ia ?

class AI:
    """
    Contient l'interface de base pour les AI
    """

    def __init__(self, player):
        """
        :type player: player.Player
        """
        # todo: manage_player()
        self.player = player

    def choose_card_set(self) -> tuple:
        raise NotImplementedError

    def choose_reinforcements_placement(self, reinforcements_number: int) -> dict:
        raise NotImplementedError

    def choose_attacker_number(self, attacker: arm.Armee, defender: arm.Armee) -> int:
        raise NotImplementedError

    def choose_target(self) -> dict:
        raise NotImplementedError

    def choose_continue_attack(self, attacker: trt.Territoire, defender: trt.Territoire) -> bool:
        raise NotImplementedError

    def choose_dice_number(self, attacker: trt.Territoire, defender: trt.Territoire, role: str) -> int:
        raise NotImplementedError

    def choose_troop_transfer(self) -> dict:
        raise NotImplementedError
