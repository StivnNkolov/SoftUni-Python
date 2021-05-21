number_of_people = int(input())

peoples_set = set()

for _ in range(number_of_people):
    name = input()
    peoples_set.add(name)

for el in peoples_set:
    print(el)
