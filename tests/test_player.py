from unittest import TestCase
import sample.player
import sample.territoire
import sample.continent
import ia.ai_for_test
from pprint import pprint
import engine.game_manager as gm
import sample.armee as arm
import ia.ai_for_test as ai


def create_data():
    manager = gm.GameManager()
    player = sample.player.Player(manager, ai.IaForTest)
    player2 = sample.player.Player(manager, ai.IaForTest)
    continent = sample.continent.Continent("Asie", 7, manager)
    a = sample.territoire.Territoire("Chine", manager, "Asie", "canon")
    b = sample.territoire.Territoire("Oural", manager, "Asie", "canon")
    c = sample.territoire.Territoire("Siam", manager, "Asie", "canon")
    a.change_owner(player)
    b.change_owner(player)
    c.change_owner(player)
    player.cards = [a, b, c]
    return locals()


class TestPlayer(TestCase):

    def test__get_renforts_number(self):
        data = create_data()
        player = data["player"]
        player.continents.append(data["continent"])
        self.assertEqual(player._get_reinforcements_number(), 18)

    def test_place_reinforcements(self):
        player = create_data()["player"]
        player.territoires[0].nbr_unites = 0
        player._place_reinforcements(5)
        self.assertEqual(player.territoires[0].nbr_unites, 5)

    def test_manage_reinforcements(self):
        player = create_data()["player"]
        player.territoires[0].nbr_unites = 0
        player.manage_reinforcements()
        self.assertEqual(player.territoires[0].nbr_unites, 11)

    def test__attack_one_target(self):
        data = create_data()
        player1 = data["player"]
        player2 = data["player2"]
        player1.nom = "louis"
        player2.nom = "autre"
        data["a"].change_owner(player1)
        data["b"].change_owner(player2)
        data["a"].nbr_unites = 300
        data["b"].nbr_unites = 30
        player1._attack_one_target(data["a"], data["b"])
        defender = data["b"].armee
        self.assertIs(defender.statut, arm.PERDANT)
        self.assertEqual(defender.nbr, 0)
        attacker = data["a"].armee
        self.assertIs(attacker.statut, arm.GAGNANT)
        self.assertLess(attacker.nbr, 300)

    def test_manage_attacks(self):
        data = create_data()
        data["c"].change_owner(data["player2"])
        data["c"].link_with(data["a"])
        data["c"].nbr_unites = 1
        data["a"].nbr_unites = 100
        data["player"].manage_attacks()
        self.assertIs(data["c"].proprietaire, data["a"].proprietaire)

    def test_manage_troop_transfers(self):
        data = create_data()
        data["a"].link_with(data["b"])
        data["a"].nbr_unites = 5
        data["b"].nbr_unites = 1
        data["player"].manage_troop_transfers()
        self.assertEqual(data["a"].nbr_unites, 4)
        self.assertEqual(data["b"].nbr_unites, 2)

    def test_play(self):
        pass
