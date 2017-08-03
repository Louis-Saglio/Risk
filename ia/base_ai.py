from territoire import Territoire

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

    def choose_attacker_number(self, attacker: Territoire, defender: Territoire) -> int:
        raise NotImplementedError

    def choose_target(self) -> dict:
        raise NotImplementedError

    def choose_continue_attack(self, attacker: Territoire, defender: Territoire) -> bool:
        raise NotImplementedError

    def choose_dice_number(self) -> int:
        raise NotImplementedError
