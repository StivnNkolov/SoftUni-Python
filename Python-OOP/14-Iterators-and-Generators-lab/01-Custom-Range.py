class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = self.start

    def __iter__(self):
        return self

    def __next__(self):
        temp_value = self.value
        if temp_value > self.end:
            raise StopIteration

        self.value += 1
        return temp_value


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
