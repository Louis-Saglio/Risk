from unittest import TestCase
import engine.game_manager as gm
import sample.continent as ctn


def create_data():
    manager = gm.GameManager()
    continent = ctn.Continent("Asie", 7, manager)
    return locals()


class TestGameManager(TestCase):

    def test_find_item_from_field_list_by_field(self):
        data = create_data()
        continent = data["manager"].find_item_from_field_list_by_field("continents", "Asie", "nom")
        self.assertIs(data["continent"], continent)
        continent = data["manager"].find_item_from_field_list_by_field("continents", continent)
        self.assertIs(data["continent"], continent)

    # def test_create_elements(self):
    #     # TODO créer un jeu de données de test dans data_for_tests
    #     from data.data_content import PLATEAU
    #     test = GameManager()
    #     plateau = test.create_elements("plateau", False, "new")
    #     assert plateau is PLATEAU
    #     test.create_elements("continent", True, plateau)
    #     test.create_elements("territoire", True, plateau)
