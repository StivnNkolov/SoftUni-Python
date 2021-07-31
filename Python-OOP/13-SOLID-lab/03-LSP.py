# # Initial code
#
# from abc import abstractmethod, ABC
#
#
# class Duck(ABC):
#     pass
#
#
# class RubberDuck(Duck):
#     @staticmethod
#     def quack():
#         return "Squeek"
#
#     @staticmethod
#     def walk():
#         """Rubber duck can walk only if you move it"""
#         raise Exception('I cannot walk by myself')
#
#     @staticmethod
#     def fly():
#         """Rubber duck can fly only if you throw it"""
#         raise Exception('I cannot fly by myself')
#
#
# class RobotDuck(Duck):
#     HEIGHT = 50
#
#     def __init__(self):
#         self.height = 0
#
#     @staticmethod
#     def quack():
#         return 'Robotic quacking'
#
#     @staticmethod
#     def walk():
#         return 'Robotic walking'
#
#     def fly(self):
#         """can only fly to specific height but
#         when it reaches it starts landing automatically"""
#         if self.height == RobotDuck.HEIGHT:
#             self.land()
#         else:
#             self.height += 1
#
#     def land(self):
#         self.height = 0


# Refactored code

from abc import abstractmethod, ABC


class Duck(ABC):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class StaticDuck(Duck):
    @staticmethod
    @abstractmethod
    def quack():
        pass


class MovingDuck(Duck):
    @staticmethod
    @abstractmethod
    def walk():
        pass

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class RealDuck(MovingDuck):
    HEIGHT = 100

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return "Duck duck"

    @staticmethod
    def walk():
        return "real duck is moving"

    def fly(self):
        if self.height == RealDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


class RubberDuck(StaticDuck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(StaticDuck):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


def making_sounds(animals):
    for animal in animals:
        print(animal.quack())


rubber_duck = RubberDuck
robot_duck = RobotDuck
real_duck = RealDuck

making_sounds([real_duck, rubber_duck, robot_duck])