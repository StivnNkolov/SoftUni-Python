from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.sound = None

    @abstractmethod
    def __repr__(self):
        pass

    def make_sound(self):
        return self.sound
