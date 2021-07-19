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
        total_workers_salary = sum([worker.salary for worker in self.workers])
        if total_workers_salary <= self.__budget:
            self.__budget -= total_workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_for_animals_care = sum([animal.money_for_care for animal in self.animals])
        if total_sum_for_animals_care <= self.__budget:
            self.__budget -= total_sum_for_animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [repr(animal)  for animal in self.animals if animal.__class__.__name__ == "Lion"]
        result.append(f"----- {len(lions)} Lions:")
        result.extend(lions)

        tigers = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Tiger"]
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)

        cheetahs = [repr(animal) for animal in self.animals if animal.__class__.__name__ == "Cheetah"]
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]

        keepers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        result.append(f"----- {len(keepers)} Keepers:")
        result.extend(keepers)

        caretakers = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        vets = [repr(worker) for worker in self.workers if worker.__class__.__name__ == "Vet"]
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(result)



