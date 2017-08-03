import unittest
from data.data_reader import serialize, dump_data, create_objects_from_data
import sample.continent
import sample.territoire
from data_for_tests import *


class TestData(unittest.TestCase):

    def test_serialize(self):
        data = serialize(CONTINENTS)
        self.assertEqual(data[0], ('plateau', 'nom', 'renforts'))
        data = serialize(TERRITOIRES1)
        serialized = [('plateau', 'icone1', 'continent', 'nom', 'icone'),
                      ('plt', 'icone11', 'Asie', 'Oural', 'canon'),
                      ('plt', 'icone11', 'Asie', 'Chine', 'cavalier'),
                      ('plt', 'icone11', 'Asie', 'Sibérie', 'fantassin'),
                      ('plt', 'icone11', 'Europe', 'Islande', 'canon'),
                      ('plt', 'icone11', 'Europe', 'Ukraine', 'cavalier')]
        self.assertEqual(data, serialized)

    def test_dump_data(self):
        data = dump_data(CONTINENTS)
        dumped = [{'plateau': 'plt', 'nom': 'Europe', 'renforts': 5},
                  {'plateau': 'plt', 'nom': 'Amérique-du-Nord', 'renforts': 5},
                  {'plateau': 'plt', 'nom': 'Océanie', 'renforts': 2},
                  {'plateau': 'plt', 'nom': 'Afrique', 'renforts': 3},
                  {'plateau': 'plt', 'nom': 'Amériques-du-Sud', 'renforts': 2},
                  {'plateau': 'plt', 'nom': 'Asie', 'renforts': 7}]
        self.assertEqual(data, dumped)

    def test_create_object_from_data(self):
        create_objects_from_data(CONTINENTS1, sample.continent.Continent)
        objects = create_objects_from_data(TERRITOIRES, sample.territoire.Territoire)
        created = {'plateau': PLATEAU,
                   'nom': 'Ukraine',
                   'icone': 'cavalier',
                   'continent': europe,
                   'proprietaire': None,
                   'nbr_unites': 0,
                   'voisins': (),
                   'armee': None}
        self.assertEqual(objects[4].__dict__, created)

if __name__ == '__main__':
    unittest.main()
