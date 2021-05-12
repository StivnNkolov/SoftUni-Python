peoples_count = int(input())
total_presentations = 0
total_grades = 0

name = input()
while name != "Finish":
    total_sum = 0
    for i in range(1, peoples_count + 1):
        grade = float(input())
        total_sum += grade
    print(f"{name} - {total_sum / peoples_count:.2f}.")
    total_presentations += 1
    total_grades += total_sum
    name = input()

print(f"Student's final assessment is {total_grades / (total_presentations * peoples_count):.2f}.")