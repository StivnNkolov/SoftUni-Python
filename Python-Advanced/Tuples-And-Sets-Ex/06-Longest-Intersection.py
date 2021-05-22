number_of_lines = int(input())

all_insertion = {}
for _ in range(number_of_lines):
    ranges = tuple(input().split("-"))
    first_range, second_range = ranges
    first_start, first_end = tuple(int(el) for el in tuple(first_range.split(",")))
    second_start, second_end = tuple(int(el) for el in tuple(second_range.split(",")))
    range1 = set()
    range2 = set()
    for num in range(first_start, first_end + 1):
        range1.add(num)
    for num in range(second_start, second_end + 1):
        range2.add(num)
    all_insertion[_] = range2 & range1


values = []
for key, value in all_insertion.items():
    values.append(len(value))

highestValue = max(values)
indexOfHighestValue = values.index(highestValue)


for key, value in all_insertion.items():
    if key == indexOfHighestValue:
        print(f"Longest intersection is [{', '.join(str(v) for v in value)}] with length {len(value)}")
