from unittest import TestCase
import sample.player
import sample.plateau
import ia.ai_for_test
import data_for_tests
import data.data_reader
from continent import Continent
from territoire import Territoire


class TestPlayer(TestCase):

    def test__get_renforts_number(self):
        plateau = sample.plateau.Plateau()
        player = sample.player.Player(plateau)
        player.ai = ia.ai_for_test.IaForTest(player)
        assert player._get_reinforcements_number() == 0

    def test_place_reinforcements(self):
        pass

    def test_play(self):
        pass
