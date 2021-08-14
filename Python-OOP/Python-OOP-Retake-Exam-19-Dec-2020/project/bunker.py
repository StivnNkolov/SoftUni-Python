from project.medicine.medicine import Medicine
from project.medicine.painkiller import Painkiller
from project.medicine.salve import Salve
from project.supply.food_supply import FoodSupply
from project.supply.supply import Supply
from project.supply.water_supply import WaterSupply
from project.survivor import Survivor


class Bunker:
    __food_type = "FoodSupply"
    __water_type = "WaterSupply"
    __painkiller_type = "Painkiller"
    __salve_type = "Salve"

    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @staticmethod
    def __find_last_added_element(iterable, searched_type):
        for index in range(len(iterable) - 1, -1, -1):
            needed_element = iterable[index]
            if type(needed_element).__name__ == searched_type:
                return needed_element

    @staticmethod
    def __create_data_for_properties(iterable_object, item_type: str):
        data = [el for el in iterable_object if type(el).__name__ == item_type]
        return data

    @property
    def food(self):
        food_data = self.__create_data_for_properties(self.supplies, self.__food_type)
        if not food_data:
            raise IndexError("There are no food supplies left!")
        return food_data

    @property
    def water(self):
        water_data = self.__create_data_for_properties(self.supplies, self.__water_type)
        if not water_data:
            raise IndexError("There are no water supplies left!")
        return water_data

    @property
    def painkillers(self):
        painkillers_list = self.__create_data_for_properties(self.supplies, self.__painkiller_type)
        if not painkillers_list:
            raise IndexError("There are no painkillers left!")
        return painkillers_list

    @property
    def salves(self):
        salves_list = self.__create_data_for_properties(self.supplies, self.__salve_type)
        if not salves_list:
            raise IndexError("There are no salves left!")
        return salves_list

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type):
        if survivor.needs_healing:
            needed_medicine = self.__find_last_added_element(self.medicine, medicine_type)
            needed_medicine.apply(survivor)
            self.medicine.remove(needed_medicine)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            needed_supply = self.__find_last_added_element(self.supplies, sustenance_type)
            needed_supply.apply(survivor)
            self.supplies.remove(needed_supply)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            reducer = survivor.age * 2
            survivor.needs -= reducer

        for survivor in self.survivors:
            self.sustain(survivor, self.__food_type)
            self.sustain(survivor, self.__water_type)

f1 = FoodSupply()
f2 = FoodSupply()
f3 = FoodSupply()

w1 = WaterSupply()
w2 = WaterSupply()
w3 = WaterSupply()

p1 = Painkiller()
p2 = Painkiller()
p3 = Painkiller()

s1 = Salve()
s2 = Salve()
s3 = Salve()
