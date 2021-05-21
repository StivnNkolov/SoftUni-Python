number_of_students = int(input())

students_dict = {}

for student in range(number_of_students):
    student_input = tuple(input().split())
    name, grade = student_input

    if name not in students_dict:
        students_dict[name] = []

    students_dict[name].append(float(grade))

for key, value in students_dict.items():
    print(f"{key} ->", end=" ")
    for v in value:
        print(f"{v:.2f}", end=" ")
    print(f"(avg: {sum(value) / len(value):.2f})")
