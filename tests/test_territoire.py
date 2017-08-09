from unittest import TestCase
import sample.territoire as trt
import sample.continent as ctn
import engine.game_manager as gm


def create_data():
    manager = gm.GameManager()
    continent = ctn.Continent("Asie", 7, manager)
    chine = trt.Territoire("chine", manager, continent, "cavalier")
    oural = trt.Territoire("oural", manager, continent, "canon")
    return locals()

class TestTerritoire(TestCase):

    def test_link_with(self):
        data = create_data()
        data["chine"].link_with(data["oural"])
        self.assertIs(data["oural"].voisins[0], data["chine"].voisins[0].voisins[0])

    def test_former_armee(self):
        data = create_data()
        data["chine"].nbr_unites = 5
        data["chine"].former_armee()
        self.assertEqual(data["chine"].armee.nbr, 5)

    def test_change_owner(self):
        pass

    def test_transfer_troops_to(self):
        data = create_data()
        data["oural"].nbr_unites = 1
        data["chine"].nbr_unites = 7
        data["chine"].transfer_troops_to(data["oural"], 5)
        self.assertEqual(data["chine"].nbr_unites, 2)
        self.assertEqual(data["oural"].nbr_unites, 6)
