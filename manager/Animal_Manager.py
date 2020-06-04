import doctest
from model.Animals import Animals
from model.Classes import Classes


class AnimalManager(object):
    def __init__(self, animals_list=None):
        if animals_list is None:
            self.animals_list = []
        else:
            self.animals_list = animals_list

    def __del__(self):
        return

    def find_animals_by_classes(self, animals_classes_to_find: Classes):
        """
        >>> first_animal = Animals('Simba','lions', 2, 70, 'male', 5, True, Classes.LION)
        >>> second_animal = Animals('Kok', 'cheehas', 1, 40, 'female',2, True,Classes.CHEETAH )
        >>> third_animal = Animals('Rex','vulture', 1, 20, 'male', 3, False,Classes.VULTURE )
        >>> animals = [first_animal, second_animal,third_animal]
        >>> manager = AnimalManager(animals)
        >>> print(manager.find_animals_by_classes(Classes.LION))
        ['Simba']
        >>> print(manager.find_animals_by_classes(Classes.CHEETAH))
        ['Kok']
        >>> print(manager.find_animals_by_classes(Classes.VULTURE))
        ['Rex']
        """
        result_animals = []
        for animal in self.animals_list:
            if animal.classes == animals_classes_to_find:
                result_animals.append(animal.name)
            else:
                pass
        return result_animals


if __name__ == "__main__":
    doctest.testmod(verbose=True)
