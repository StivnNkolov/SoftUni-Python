import math
number_of_people = int(input())
capacity = int(input())

courses = number_of_people / capacity
print(math.ceil(courses))