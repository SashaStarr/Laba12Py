import doctest

from model.Animals import Animals
from model.Classes import Classes
from model.Sort_Type import Sort_Type


class AnimalManagerUtils:

    def __init__(self, animals_list=None):
        if animals_list is None:
            self.animals_list = []
        else:
            self.animals_list = animals_list

    def __del__(self):
        return

    def sort_animals_by_name(self, type_of_sort: str):
        """
        >>> first_animal = Animals('Tom', 'lions', 2, 70, 'male', 5, True, Classes.LION)
        >>> second_animal = Animals('Gloria', 'lions', 1, 80, 'male', 3, True, Classes.LION)
        >>> third_animal = Animals('Kenny', 'cheetahs', 1, 45, 'female', 2, False, Classes.CHEETAH)
        >>> fourth_animal = Animals('Bars','cheetahs', 0.5, 30, 'female', 4, True, Classes.CHEETAH)
        >>> fifth_animal = Animals('Boby', 'vulture', 1, 15, 'male', 1, False, Classes.VULTURE)
        >>> animals = [first_animal, second_animal, third_animal, fourth_animal , fifth_animal]
        >>> manager_utils = AnimalManagerUtils(animals)
        >>> sorted_animals = manager_utils.sort_animals_by_name(Sort_Type.ASCENDING.value)
        >>> for animal_ascend in sorted_animals: print(animal_ascend.name)
        Bars
        Boby
        Gloria
        Kenny
        Tom
        >>> sorted_animals = manager_utils.sort_animals_by_name(Sort_Type.DESCENDING.value)
        >>> for animal_descen in sorted_animals: print(animal_descen.name)
        Tom
        Kenny
        Gloria
        Boby
        Bars
        """
        sorted_animals = sorted(self.animals_list, key=lambda animal: animal.name)
        if type_of_sort == Sort_Type.ASCENDING.value:
            return sorted_animals
        elif type_of_sort == Sort_Type.DESCENDING.value:
            return sorted_animals[::-1]
        else:
            return sorted_animals

    def sort_animals_by_size_in_m(self, type_of_sort: int):
        """
        >>> first_animal = Animals('Tom', 'lions', 5, 70, 'male', 5, True, Classes.LION)
        >>> second_animal = Animals('Gloria', 'lions',4, 80, 'male', 3, True, Classes.LION)
        >>> third_animal = Animals('Kenny', 'cheetahs', 3, 45, 'female', 2, False, Classes.CHEETAH)
        >>> fourth_animal = Animals('Bars','cheetahs', 1, 30, 'female', 4, True, Classes.CHEETAH)
        >>> fifth_animal = Animals('Boby', 'vulture', 2, 15, 'male', 1, False, Classes.VULTURE)
         >>> animals = [first_animal, second_animal, third_animal, fourth_animal , fifth_animal]
        >>> manager_utils = AnimalManagerUtils(animals)
        >>> sorted_animals = manager_utils.sort_animals_by_size_in_m(Sort_Type.ASCENDING.value)
        >>> for animal in sorted_animals: print(animal.name)
        Bars
        Boby
        Kenny
        Gloria
        Tom
        >>> sorted_animals = manager_utils.sort_animals_by_size_in_m(Sort_Type.DESCENDING.value)
        >>> for animal_1 in sorted_animals: print(animal_1.name)
        Tom
        Gloria
        Kenny
        Boby
        Bars
        """
        sorted_animals = sorted(self.animals_list, key=lambda animal: animal.size_in_m)
        if type_of_sort == Sort_Type.ASCENDING.value:
            return sorted_animals
        elif type_of_sort == Sort_Type.DESCENDING.value:
            return sorted_animals[::-1]


if __name__ == "__main__":
    doctest.testmod(verbose=True)