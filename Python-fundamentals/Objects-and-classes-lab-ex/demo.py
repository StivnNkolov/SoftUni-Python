class Zoo:
    __animals = 0

    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.mammals = []
        self.fish = []
        self.bird = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == "fish":
            self.fish.append(name)
            Zoo.__animals += 1
        elif species == "bird":
            self.bird.append(name)
            Zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name_of_zoo}: {', '.join(self.mammals)}\nTotal animals: {self.__animals}"
        elif species == "fish":
            return f"Fishes in {self.name_of_zoo}: {', '.join(self.fish)}\nTotal animals: {self.__animals}"
        elif species == "bird":
            return f"Birds in {self.name_of_zoo}: {', '.join(self.bird)}\nTotal animals: {self.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

n = int(input())

for i in range(n):
    animals_input = input()
    species, name = animals_input.split()
    zoo.add_animal(species, name)

species_input = input()
print(zoo.get_info(species_input))
