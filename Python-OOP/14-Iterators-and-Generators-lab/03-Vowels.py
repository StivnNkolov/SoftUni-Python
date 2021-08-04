class vowels:
    def __init__(self, input_string):
        self.input_string = input_string

        self.start_point = 0
        self.work_number = self.start_point

        self.list_with_vowels = ("A", "E", "I", "O", "U", "Y",
                                 "a", "e", "i", "o", "u", "y")

        self.formatted_string = [el for el in self.input_string
                                 if el in self.list_with_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.work_number
        if temp == len(self.formatted_string):
            raise StopIteration

        self.work_number += 1

        return self.formatted_string[temp]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

print(list(my_string))


