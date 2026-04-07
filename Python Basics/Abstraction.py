# hiding internal details and showing only essential features
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound():
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo!")


lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

        