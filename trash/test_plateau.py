from unittest import TestCase

import engine.game_manager as gm
import sample.continent
from sample.territoire import Territoire


class TestTerritoire(TestCase):

    def test_link_with(self):
        manager = gm.GameManager()
        europe = sample.continent.Continent("Europe", 5, manager)
        asie = sample.continent.Continent("Asie", 7, manager)
        t1 = Territoire("Ukraine", manager, europe, "cav")
        t2 = Territoire("Oural", manager, asie, "cav")
        t1.link_with(t2)
        assert t1 in t2.voisins
