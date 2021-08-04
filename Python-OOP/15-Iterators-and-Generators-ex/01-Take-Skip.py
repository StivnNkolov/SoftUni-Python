class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self._counter = 0
        self.work_value = 0

    def __iter__(self):
        return self

    def __next__(self):
        work_value = self.work_value
        if self._counter == self.count:
            raise StopIteration

        self.work_value += self.step
        self._counter += 1
        return work_value

# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
