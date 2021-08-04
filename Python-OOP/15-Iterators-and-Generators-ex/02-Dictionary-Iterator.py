class dictionary_iter:
    def __init__(self, input_dict: dict):
        self.input_dict = input_dict
        self.pairs = list(self.input_dict.items())

        self.start_point = 0
        self.end_point = len(self.pairs) - 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.start_point
        if self.start_point > self.end_point:
            raise StopIteration

        self.start_point += 1
        return self.pairs[temp]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
