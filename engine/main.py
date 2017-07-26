import data_content as data
from data_reader import create_objects_from_data
from plateau import Continent, Territoire

CONTINENTS = create_objects_from_data(data.CONTINENTS, Continent)
TERRITOIRES = create_objects_from_data(data.TERRITOIRES, Territoire)
