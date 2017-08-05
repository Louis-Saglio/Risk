from data_reader import create_objects_from_data
import data.data_content


# noinspection PyShadowingNames,PyUnusedLocal
class GameManager:

    def __init__(self):
        self.plateaux = []

    def create_elements(self, element: str, create: bool, plateau):
        """
        Si from_data :
            Renvoie une liste d'instance d' <element> avec les données de <ELEMENT>
        Sinon :
            Renvoi <ELEMENT>
        """
        # TODO: refactor
        data = eval(f"data.data_content.{element.upper()}")
        if create:
            sample = __import__(f"sample.{element.lower()}")
            klass = eval(f"sample.{element.lower()}.{element.capitalize()}")
            elements = create_objects_from_data(data, klass)
        else:
            elements = data
        if plateau not in ("new", None):
            plateau.__dict__[element.lower()] = elements
        elif plateau == "new":
            self.plateaux.append(elements)
        return elements

    def give_a_card(self):
        raise NotImplementedError
