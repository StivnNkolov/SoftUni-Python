from MovieWorld02.customer import Customer
from MovieWorld02.dvd import DVD


class MovieWorld:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        capacity = MovieWorld.customer_capacity()
        if len(self.customers) < capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        capacity = MovieWorld.dvd_capacity()
        if len(self.dvds) < capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_dvd.age_restriction > current_customer.age:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = [customer for customer in self.customers if customer.id == customer_id][0]
        current_dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]

        if current_dvd in current_customer.rented_dvds:
            current_dvd.is_rented = False
            current_customer.rented_dvds.remove(current_dvd)
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for c in self.customers:
            result.append(repr(c))

        for d in self.dvds:
            result.append(repr(d))

        return '\n'.join(result)
