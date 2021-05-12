# number_of_snowballs = int(input())
#
# snowballs_info = {}
#
# for ball in range(number_of_snowballs):
#     snow = int(input())
#     time = int(input())
#     quality = int(input())
#     value = (snow / time) ** quality
#     snowballs_info[value] = {"snow": snow, "time": time, "quality": quality}
#
#
# sorted_info = sorted(snowballs_info.items(), key=lambda x: x[0], reverse=True)
# for key, value in sorted_info:
#     print(f"{value['snow']} : {value['time']} = {int(key)} ({value['quality']})")
#     break


snowballs_count = int(input())

max_snow_ball = 0

max_snow = 0
max_time = 0
max_quality = 0

for ball in range(snowballs_count):
    snow = int(input())
    time = int(input())
    quality = int(input())

    snow_ball_points = (snow / time) ** quality

    if snow_ball_points > max_snow_ball:
        max_snow_ball = snow_ball_points
        max_snow = snow
        max_time = time
        max_quality = quality

print(f'{max_snow} : {max_time} = {int(max_snow_ball)} ({max_quality})')