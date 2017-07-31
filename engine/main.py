from pprint import pprint
import game_manager as gm

manager = gm.GameManager()

manager.create_elements("plateau", False, "new")
manager.create_elements("continent", True, manager.plateaux[0])
manager.create_elements("territoire", True, manager.plateaux[0])

pprint(manager.plateaux[0].__dict__)
