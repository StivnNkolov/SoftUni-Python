from project.supply.supply import Supply
from project.survivor import Survivor


class FoodSupply(Supply):
    needs_increase = 20

    def __init__(self):
        super().__init__(self.needs_increase)
