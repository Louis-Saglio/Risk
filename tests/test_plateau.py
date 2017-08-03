from unittest import TestCase
import sample.plateau
import sample.continent
from territoire import Territoire


class TestTerritoire(TestCase):

    def test_link_with(self):
        plt = sample.plateau.Plateau()
        europe = sample.continent.Continent("Europe", 5, plt)
        asie = sample.continent.Continent("Asie", 7, plt)
        t1 = Territoire("Ukraine", plt, europe, "cav")
        t2 = Territoire("Oural", plt, asie, "cav")
        t1.link_with(t2)
        assert t1 in t2.voisins
