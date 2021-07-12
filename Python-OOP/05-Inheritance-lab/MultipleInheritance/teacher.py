from MultipleInheritance.person import Person
from MultipleInheritance.employee import Employee


class Teacher(Employee, Person):
    def __init__(self):
        Employee.__init__(self)
        Person.__init__(self)

    def teach(self):
        return "teaching..."
