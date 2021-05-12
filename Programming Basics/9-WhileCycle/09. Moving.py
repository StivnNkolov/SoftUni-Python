# 1.	Широчина на свободното пространство - цяло число;
# 2.	Дължина на свободното пространство - цяло число;
# 3.	Височина на свободното пространство - цяло число;
# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа

width = int(input())
lenght = int(input())
high = int(input())

volume = width * lenght * high

command = input()
while command != "Done":
    boxes = int(command)
    volume -= boxes
    if volume <= 0:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break
    command = input()
if volume > 0:
    print(f"{volume} Cubic meters left.")