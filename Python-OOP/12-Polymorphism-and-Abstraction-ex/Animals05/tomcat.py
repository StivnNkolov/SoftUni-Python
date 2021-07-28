from Animals05.cat import Cat


class Tomcat(Cat):
    gender = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.gender)
        self.sound = "Hiss"
