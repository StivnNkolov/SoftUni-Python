student_book = {}
good_students = {}

rows = int(input())

for r in range(rows):
    student_name = input()
    grade = float(input())
    if student_name not in student_book:
        student_book[student_name] = []
    student_book[student_name].append(grade)
for stu, avr_grade in student_book.items():
    avg = sum(student_book[stu]) / len(student_book[stu])
    student_book[stu] = avg
for key, value in dict(sorted(student_book.items(), key=lambda kvs: -kvs[1])).items():
    if student_book[key] >= 4.5:
        print(f"{key} -> {value:.2f}")


#
#
# print(student_book)

