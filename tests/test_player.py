from unittest import TestCase
import sample.player
import sample.plateau
import sample.territoire
import sample.continent
import ia.ai_for_test
from pprint import pprint


def create_player():
    plateau = sample.plateau.Plateau()
    player = sample.player.Player(plateau)
    player.ai = ia.ai_for_test.IaForTest(player)
    player2 = sample.player.Player(plateau)
    player2.ai = ia.ai_for_test.IaForTest(player2)
    sample.continent.Continent("Asie", 7, plateau)
    a = sample.territoire.Territoire("Chine", plateau, "Asie", "canon")
    b = sample.territoire.Territoire("Oural", plateau, "Asie", "canon")
    c = sample.territoire.Territoire("Siam", plateau, "Asie", "canon")
    a.change_owner(player)
    b.change_owner(player)
    c.change_owner(player)
    player.cards = [a, b, c]
    return locals()


class TestPlayer(TestCase):

    def test__get_renforts_number(self):
        player = create_player()["player"]
        self.assertEqual(player._get_reinforcements_number(), 18)

    def test_place_reinforcements(self):
        player = create_player()["player"]
        player.territoires[0].nbr_unites = 0
        player._place_reinforcements(5)
        self.assertEqual(player.territoires[0].nbr_unites, 5)

    def test_manage_reinforcements(self):
        player = create_player()["player"]
        player.territoires[0].nbr_unites = 0
        player.manage_reinforcements()
        self.assertEqual(player.territoires[0].nbr_unites, 18)

    def test__attack_one_target(self):
        data = create_player()
        player1 = data["player"]
        player2 = data["player2"]
        data["a"].change_owner(player1)
        data["b"].change_owner(player2)
        data["a"].nbr_unites = 70
        data["b"].nbr_unites = 2
        player1._attack_one_target(data["a"], data["b"])
        self.assertIs(player1, data["b"].proprietaire)

    def test_manage_attacks(self):
        pass

    def test_play(self):
        pass
