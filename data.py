from pprint import pprint
from plateau import Continent

CONTINENTS = (
    ("nom", "renforts"),
    ("Europe", 5),
    ("Amérique-du-Nord", 5),
    ("Océanie", 2),
    ("Afrique", 3),
    ("Amériques-du-Sud", 2),
)


TERRITOIRES = (
    ("nom", "continent"),
    ("Alaska", )
)


def dump_data(data):
    rep = []
    for a in data[1::]:
        rep.append({})
        for i in range(len(a)):
            rep[-1][data[0][i]] = a[i]
    return rep


def create_objects_from_data(data, klass: type):
    rep = []
    for dico in dump_data(data):
        rep.append(klass(**dico))
    return rep


pprint(dump_data(CONTINENTS))
pprint([cont.__dict__ for cont in create_objects_from_data(CONTINENTS, Continent)])
