# 1.	Доход в лева - реално число;
# 2.	Среден успех -  реално числсо;
# 3.	Минимална работна заплата – реално число.
import math
income = float(input())
grade = float(input())
minimum_salary = float(input())

social = 0
perfect = 0

if grade >= 5.5:
    perfect = grade * 25
if income < minimum_salary and grade >= 4.5:
    social = minimum_salary * 0.35

if social > perfect:
    print(f"You get a Social scholarship {math.floor(social)} BGN")
elif perfect >= social:
    if perfect != 0:
        print(f"You get a scholarship for excellent results {math.floor(perfect)} BGN")
    else:
        print(f"You cannot get a scholarship!")