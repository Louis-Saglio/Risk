from data_reader import create_objects_from_data
import sample.continent
from inspect import isclass


class GameManagerError(BaseException):
    pass


# noinspection PyShadowingNames,PyUnusedLocal
class GameManager:
    def __init__(self):
        self.continents = []
        self.players = []
        self.card_sets = {}


    def give_a_card(self):
        return NotImplementedError

    def find_item_from_field_list_by_field(self, field_list: str, item_value, item_field_name="name"):
        if not isinstance(item_value, str):
            return item_value
        for field in self.__dict__[field_list]:
            if field.__dict__[item_field_name] == item_value:
                return field
        raise GameManagerError

    # def create(self, kind, **kwargs):
    #     klass = self.classes_available[kind]
    #     # si None message erreur
    #     field_list = self.__dict__[kind + 's']

