bad_grades = int(input())

grades_sum = 0
grade_count = 0
last_problem = ""
bad_grade_count = 0

comand = input()
while comand != "Enough":
    grade = int(input())
    grades_sum += grade
    grade_count += 1
    last_problem = comand
    if grade <= 4:
        bad_grade_count += 1
    if bad_grades == bad_grade_count:
        break
    comand = input()

if comand == "Enough":
    print(f"Average score: {grades_sum / grade_count:.2f}")
    print(f"Number of problems: {grade_count}")
    print(f"Last problem: {last_problem}")
if bad_grades == bad_grade_count:
    print(f"You need a break, {bad_grade_count} poor grades.")


# bad_grades_possible = int(input())
#
# grades_sum = 0
# tasks_count = 0
# last_task = ""
# bad_grades_count = 0
#
# task_name = input()
#
# while task_name != "Enough":
#     grade = int(input())
#     grades_sum += grade
#     tasks_count += 1
#     last_task = task_name
#     if grade <= 4:
#         bad_grades_count += 1
#         if bad_grades_count >= bad_grades_possible:
#             print(f"You need a break, {bad_grades_count} poor grades.")
#             break
#     task_name = input()
#
# if task_name == "Enough":
#     print(f"Average score: {grades_sum / tasks_count:.2f}")
#     print(f"Number of problems: {tasks_count}")
#     print(f"Last problem: {last_task}")
#
#     # o
#     # "Average score: {средна оценка}"
#     # o
#     # "Number of problems: {броя на всички задачи}"
#     # o
#     # "Last problem: {името на последната задача}"

