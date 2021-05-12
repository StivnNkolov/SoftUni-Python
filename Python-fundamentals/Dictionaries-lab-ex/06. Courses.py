courses_info = {}

command = input()
while not command == "end":
    courses_name, student_name = command.split(" : ")
    if courses_name not in courses_info:
        courses_info[courses_name] = [student_name]
    else:
        courses_info[courses_name].append(student_name)
    command = input()

for course,students in sorted(courses_info.items(), key=lambda kvs: len(kvs[1]), reverse=True):
    print(f"{course}: {len(students)}")
    for s in sorted(students):
        print(f"-- {s}")