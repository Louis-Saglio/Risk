import data.data_content
import sample
from data_reader import create_objects_from_data


class GameManager:

    def __init__(self):
        pass

    def create_elements(self, element, from_data=True):
        """
        Si from_data :
            Renvoie une liste d'instance d' <element> avec les données de <ELEMENT>
        Sinon :
            Renvoi <ELEMENT>
        """
        data = eval(f"data.data_content.{element.upper()}")
        if from_data:
            klass = eval(f"sample.{element.lower()}.{element.capitalize()}")
            elements = create_objects_from_data(data, klass)
        else:
            elements = data
        return elements


if __name__ == '__main__':
    from data.data_content import PLATEAU
    test = GameManager()
    a = test.create_elements("plateau", False)
    assert a is PLATEAU
    a = test.create_elements("territoire")
    a = test.create_elements("continent")
    print(a)
