def create_students_info_dict(number_from_input):
    students_info_d = {}
    for _ in range(number_from_input):
        student_input = tuple(input().split())
        name, grade = student_input

        if name not in students_info_d:
            students_info_d[name] = []
        students_info_d[name].append(float(grade))
    return students_info_d


def get_formatted_grades(grades):
    return [f"{el:.2f}" for el in grades]


def get_avg_grade(grades):
    return sum(grades) / len(grades)


def print_result(student_info_dict):
    for key, value in student_info_dict.items():
        result = get_formatted_grades(value)
        avg = get_avg_grade(value)
        print(f"{key} -> {' '.join(result)} (avg: {avg:.2f})")


students_info_dict = create_students_info_dict(int(input()))
print_result(students_info_dict)
