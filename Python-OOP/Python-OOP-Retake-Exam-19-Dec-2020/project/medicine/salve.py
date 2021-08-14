from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Salve(Medicine):
    health_increase = 50

    def __init__(self):
        super().__init__(self.health_increase)

