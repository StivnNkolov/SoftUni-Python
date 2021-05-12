# 1.	Дължина в см – цяло число
# 2.	Широчина в см – цяло число
# 3.	Височина в см – цяло число
# 4.	Процент зает обем – реално число
lenght = int(input())
width = int(input())
height = int(input())
occupied_percentage = float(input())
whole_volume = lenght * width * height  #celia obem na akvariuma v kubichni sm 299625
volume_after_sand = whole_volume - (occupied_percentage / 100)
water_needed = volume_after_sand / 1000
print(water_needed)




