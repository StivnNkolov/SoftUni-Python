name = input()

clas = 0
grades_sum = 0
fails = 0

while clas != 12:
    grade = float(input())
    if grade >= 4:
        clas += 1
        grades_sum += grade
    else:
        fails += 1
    if fails == 2:
        print(f"{name} has been excluded at {clas + 1} grade")
        break
if clas == 12:
    print(f"{name} graduated. Average grade: {grades_sum / 12:.2f}")


