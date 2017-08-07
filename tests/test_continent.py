from unittest import TestCase
import sample.continent
import sample.territoire
import sample.player
import engine.game_manager as gm


class TestContinent(TestCase):

    def test_get_master(self):
        manager = gm.GameManager()
        continent = sample.continent.Continent("Asie", 7, manager)
        continent.territoires = (
            sample.territoire.Territoire("Chine", manager, continent, "rien"),
            sample.territoire.Territoire("Oural", manager, continent, "rien")
        )
        player = sample.player.Player(manager)
        for territoire in continent.territoires:
            territoire.proprietaire = player
        assert continent.get_master() is player
        continent.territoires[0].proprietaire = None
        assert continent.get_master() is None
