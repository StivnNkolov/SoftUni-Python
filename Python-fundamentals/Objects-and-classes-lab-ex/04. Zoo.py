class Zoo:
    __animals = 0

    def __init__(self, name_of_the_zoo):
        self.name_of_the_zoo = name_of_the_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
            Zoo.__animals += 1
        elif species == "fish":
            self.fishes.append(name)
            Zoo.__animals += 1
        elif species == "bird":
            self.birds.append(name)
            Zoo.__animals += 1

    def get_info(self, given_species):
        if given_species == "mammal":
            return f"Mammals in {self.name_of_the_zoo}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"
        elif given_species == "fish":
            return f"Fishes in {self.name_of_the_zoo}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"
        elif given_species == "bird":
            return f"Birds in {self.name_of_the_zoo}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
number_of_animals = int(input())
for animal in range(number_of_animals):
    animal_inf0 = input().split()
    species, name = animal_inf0
    zoo.add_animal(species, name)

given_species = input()
zoo.get_info(given_species)
print(zoo.get_info(given_species))
