from pprint import pprint

import continent
import data_content
import game_manager as gm
from data_reader import create_objects_from_data

manager = gm.GameManager()

plateau = data_content.PLATEAU
continents = create_objects_from_data(data_content.CONTINENT, continent.Continent)
# manager.create_elements("plateau", False, "new")
# manager.create_elements("continent", True, manager.plateaux[0])
# manager.create_elements("territoire", True, manager.plateaux[0])
#
# manager.create_elements("player", True, "new")
