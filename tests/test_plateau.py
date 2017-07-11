from unittest import TestCase

from sample.plateau import Territoire, Continent


class TestTerritoire(TestCase):

    def test_link_with(self):
        europe = Continent("Europe", 5)
        asie = Continent("Asie", 7)
        t1 = Territoire("Ukraine", europe)
        t2 = Territoire("Oural", asie)
        t1.link_with(t2)
        assert t1 in t2.voisins


class TestContinent(TestCase):
    pass
