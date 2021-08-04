class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.starting_point = len(iterable) - 1
        self.end_point = 0

        self.work_value = self.starting_point

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.work_value
        if self.work_value < self.end_point:
            raise StopIteration

        self.work_value -= 1
        return self.iterable[temp]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
