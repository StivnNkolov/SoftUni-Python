from Animals05.cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.gender)
        self.sound = "Meow"
