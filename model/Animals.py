class Animals:

    def __init__(self, name=None, kind=None, size_in_m=None, weight_in_kg=None, point=None, age_in_years=None,
                 hunt_for_prey=None, classes=None):
        self.name = name
        self.kind = kind
        self.size_in_m = size_in_m
        self.weight_in_kg = weight_in_kg
        self.point = point
        self.age_in_years = age_in_years
        self.hunt_for_prey = hunt_for_prey
        self.classes = classes

    def __del__(self):
        return

    def __str__(self):
        name = 'Name: {}\n'.format(self.name)
        kind = 'kind: {}\n'.format(self.kind)
        size_in_m = 'size_in_m: {}\n'.format(self.size_in_m)
        weight_in_kg = 'weight in kg: {}\n'.format(self.weight_in_kg)
        point = 'point: {}\n'.format(self.point)
        age_in_years = 'age in years: {}\n'.format(self.age_in_years)
        hunt_for_prey = 'hunt for prey: {}\n'.format(self.hunt_for_prey)
        classes = 'class: {}\n'.format(self.classes)

        return name + kind + size_in_m + weight_in_kg + point + age_in_years + hunt_for_prey + classes


class Lion:

    def __init__(self, size_of_mane_in_sm=None):
        self.size_of_mane_in_sm = size_of_mane_in_sm

    def __del__(self):
        return

    def __str__(self):
        size_of_mane_in_sm = f'size of mane in sm: {self.size_of_mane_in_sm}'
        return size_of_mane_in_sm


class Cheetah:

    def __init__(self, magnitude_of_points=None):
        self.magnitude_of_points = magnitude_of_points

    def __del__(self):
        return

    def __str__(self):
        magnitude_of_points = f'magnitude of points: {self.magnitude_of_points}'
        return magnitude_of_points


class Vulture:

    def __init__(self, wingspan_in_centimeters=None):
        self.wingspan_in_centimeters = wingspan_in_centimeters

    def __del__(self):
        return

    def __str__(self):
        wingspan_in_centimeters = f'wingspan in centimeters: {self.wingspan_in_centimeters}'
        return wingspan_in_centimeters
