number_of_lines = int(input())

courses_list = []

for _ in range(number_of_lines):
    courses_names = input()
    courses_list.append(courses_names)

print(courses_list)