from mathematical_calculations import mapper

first_number, operator, second_number = input().split()
first_number = float(first_number)
second_number = float(second_number)

if mapper.calculations_mapper().get(operator):
    print(
        f"{mapper.calculations_mapper()[operator](first_number, second_number)} ")
else:
    print("Invalid operator")
