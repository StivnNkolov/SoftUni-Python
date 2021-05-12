hour = int(input())
minutes = int(input())

second_minutes = minutes + 15
if second_minutes > 59:
    hour += 1
    second_minutes -= 60
if hour > 23:
    hour = 0
if second_minutes <= 9:
    print(f"{hour}:0{second_minutes}")
else:
    print(f"{hour}:{second_minutes}")
