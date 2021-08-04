from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name

        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget - price >= 0 and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget - price < 0 and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker.name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary_for_workers = sum([worker.salary for worker in self.workers])
        if total_salary_for_workers <= self.__budget:
            self.__budget -= total_salary_for_workers
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_sum_for_animal_care = sum([animal.money_for_care for animal in self.animals])
        if total_sum_for_animal_care <= self.__budget:
            self.__budget -= total_sum_for_animal_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = []
        result.append(f"You have {len(self.animals)} animals")
        lions = [repr(animal) for animal in self.animals if isinstance(animal, Lion)]
        result.append(f"----- {len(lions)} Lions:")
        result.extend(lions)
        tigers = [repr(animal) for animal in self.animals if isinstance(animal, Tiger)]
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        cheetahs = [repr(animal) for animal in self.animals if isinstance(animal, Cheetah)]
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        result = []
        result.append(f"You have {len(self.workers)} workers")

        keepers = [repr(worker) for worker in self.workers if isinstance(worker, Keeper)]
        result.append(f"----- {len(keepers)} Keepers:")
        result.extend(keepers)

        caretakers = [repr(worker) for worker in self.workers if isinstance(worker, Caretaker)]
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)

        vets = [repr(worker) for worker in self.workers if isinstance(worker, Vet)]
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return '\n'.join(result)



# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
