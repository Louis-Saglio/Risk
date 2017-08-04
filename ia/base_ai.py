import sample.territoire as trt

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
        self.player = player

    def choose_card_set(self) -> tuple:
        raise NotImplementedError

    def choose_reinforcements_placement(self, reinforcements_number: int) -> dict:
        raise NotImplementedError

    def choose_attacker_number(self, attacker: trt.Territoire, defender: trt.Territoire) -> int:
        raise NotImplementedError

    def choose_target(self) -> dict:
        raise NotImplementedError

    def choose_continue_attack(self, attacker: trt.Territoire, defender: trt.Territoire) -> bool:
        raise NotImplementedError

    def choose_dice_number(self, attacker: trt.Territoire, defender: trt.Territoire, role: str) -> int:
        raise NotImplementedError
