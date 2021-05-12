def defining_grade(input_grade):
    if 2 <= input_grade <= 2.99:
        return "Fail"
    elif 3 <= input_grade <= 3.49:
        return "Poor"
    elif 3.50 <= input_grade <= 4.49:
        return "Good"
    elif 4.50 <= input_grade <= 5.49:
        return "Very Good"
    elif 5.50 <= input_grade <= 6:
        return "Excellent"


grade = float(input())
print(defining_grade(grade))

