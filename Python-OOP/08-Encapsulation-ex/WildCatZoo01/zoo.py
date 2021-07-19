from WildCatZoo01.cheetah import Cheetah


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if self.__budget < price and self.__animal_capacity > 0:
            return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)

                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_workers_salary = 0
        for worker in self.workers:
            total_workers_salary += worker.salary

        if total_workers_salary <= self.__budget:
            self.__budget -= total_workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_for_animals_care = 0
        for animal in self.animals:
            total_sum_for_animals_care += animal.money_for_care

        if total_sum_for_animals_care <= self.__budget:
            self.__budget -= total_sum_for_animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal) + "\n")
        result += f"----- {len(lions)} Lions:\n"
        result += ''.join(lions)
        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal) + "\n")
        result += f"----- {len(tigers)} Tigers:\n"
        result += ''.join(tigers)
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Cheetah":
                cheetahs.append(repr(animal))
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += '\n'.join(cheetahs)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = []
        for w in self.workers:
            if w.__class__.__name__ == "Keeper":
                keepers.append(repr(w) + "\n")

        result += f"----- {len(keepers)} Keepers:\n"
        result += ''.join(keepers)

        caretakers = []
        for w in self.workers:
            if w.__class__.__name__ == "Caretaker":
                caretakers.append(repr(w) + "\n")

        result += f"----- {len(caretakers)} Caretakers:\n"
        result += ''.join(caretakers)

        vets = []
        for w in self.workers:
            if w.__class__.__name__ == "Vet":
                vets.append(repr(w) )

        result += f"----- {len(vets)} Vets:\n"
        result += '\n'.join(vets)

        return result



