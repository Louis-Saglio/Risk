import unittest
from pprint import pprint

from data.data_reader import serialize, dump_data, create_objects_from_data
from plateau import Plateau
from continent import Continent
from territoire import Territoire

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


TERRITOIRES1 = {
    ("plateau", "icone1"): {
        "continent": (
            ("nom", "icone"),
        )
    },
    ("plt", "icone11"): {
        "Asie": (
            ("Oural", "canon"),
            ("Chine", "cavalier"),
            ("Sibérie", "fantassin"),
        ),
        "Europe": (
            ("Islande", "canon"),
            ("Ukraine", "cavalier"),
        )
    }
}


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
