employee_happiness = input().split()
happiness_improvement_factor = int(input())
employee_happiness_as_int = list(map(int, employee_happiness))

improve_happiness = list(map(lambda x: x * happiness_improvement_factor, employee_happiness_as_int))
avg_happiness = sum(improve_happiness) / len(improve_happiness)

happy_people = list(filter(lambda x: x >= avg_happiness, improve_happiness))

half = len(improve_happiness) / 2
if len(happy_people) >= half:
    print(f"Score: {len(happy_people)}/{len(improve_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_people)}/{len(improve_happiness)}. Employees are not happy!")