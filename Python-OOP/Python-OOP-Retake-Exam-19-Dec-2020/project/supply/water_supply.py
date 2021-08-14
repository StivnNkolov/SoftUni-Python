from project.supply.supply import Supply
from project.survivor import Survivor


class WaterSupply(Supply):
    needs_increase = 40

    def __init__(self):
        super().__init__(self.needs_increase)


