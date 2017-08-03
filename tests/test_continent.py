from unittest import TestCase
import sample.continent
import sample.plateau
import sample.territoire
import sample.player


class TestContinent(TestCase):

    def test_get_master(self):
        plateau = sample.plateau.Plateau()
        continent = sample.continent.Continent("Asie", 7, plateau)
        continent.territoires = (
            sample.territoire.Territoire("Chine", plateau, continent, "rien"),
            sample.territoire.Territoire("Oural", plateau, continent, "rien")
        )
        player = sample.player.Player(plateau)
        for territoire in continent.territoires:
            territoire.proprietaire = player
        assert continent.get_master() is player
        continent.territoires[0].proprietaire = None
        assert continent.get_master() is None
