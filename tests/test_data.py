import unittest
from pprint import pprint

from data.data_reader import serialize, dump_data, create_objects_from_data
from plateau import Territoire, Plateau, Continent

plt = Plateau()

CONTINENTS = {
    "plateau": (
        ("nom", "renforts"),
    ),
    "plt": (
        ("Europe", 5),
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}


CONTINENTS1 = {
    "plateau": (
        ("nom", "renforts"),
    ),
    plt: (
        ("Amérique-du-Nord", 5),
        ("Océanie", 2),
        ("Afrique", 3),
        ("Amériques-du-Sud", 2),
        ("Asie", 7),
    )
}

europe = Continent("Europe", 5, plt)
TERRITOIRES = {
        "plateau": {
            "continent": (
                ("nom", "icone"),
            )
        },
        plt: {
            "Asie": (
                ("Oural", "canon"),
                ("Chine", "cavalier"),
                ("Sibérie", "fantassin"),
            ),
            europe: (
                ("Islande", "canon"),
                ("Ukraine", "cavalier"),
            )
        }
}


class TestData(unittest.TestCase):

    def test_serialize(self):
        data = serialize(CONTINENTS)
        self.assertEqual(data[0], ('plateau', 'nom', 'renforts'))
        data = serialize(CONTINENTS)
        serialized = [('plateau', 'nom', 'renforts'),
                      ('plt', 'Europe', 5),
                      ('plt', 'Amérique-du-Nord', 5),
                      ('plt', 'Océanie', 2),
                      ('plt', 'Afrique', 3),
                      ('plt', 'Amériques-du-Sud', 2),
                      ('plt', 'Asie', 7)]
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
        create_objects_from_data(CONTINENTS1, Continent)
        objects = create_objects_from_data(TERRITOIRES, Territoire)
        created = {'plateau': plt,
                   'nom': 'Ukraine',
                   'icone': 'cavalier',
                   'continent': europe,
                   'proprietaire': None,
                   'nbr_unitees': 0,
                   'voisins': ()}
        self.assertEqual(objects[4].__dict__, created)

if __name__ == '__main__':
    unittest.main()
