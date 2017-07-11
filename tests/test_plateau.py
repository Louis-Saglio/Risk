from unittest import TestCase
from plateau import Plateau
from sample.plateau import Territoire, Continent


class TestTerritoire(TestCase):

    def test_link_with(self):
        plt = Plateau()
        europe = Continent("Europe", 5, plt)
        asie = Continent("Asie", 7, plt)
        t1 = Territoire("Ukraine", plt, europe, "cav")
        t2 = Territoire("Oural", plt, asie, "cav")
        t1.link_with(t2)
        assert t1 in t2.voisins


class TestContinent(TestCase):
    pass
