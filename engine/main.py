from os import chdir
chdir("/home/louis/Projects/Risk")


import data_content as data
from data_reader import create_objects_from_data
from continent import Continent
from territoire import Territoire

CONTINENTS = create_objects_from_data(data.CONTINENTS, Continent)
TERRITOIRES = create_objects_from_data(data.TERRITOIRE, Territoire)
