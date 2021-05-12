# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
record_in_seconds = float(input())
distance_in_meters = float(input())
time_for_one_meter_in_sec = float(input())

time_for_the_distance = distance_in_meters * time_for_one_meter_in_sec
delay = (distance_in_meters // 15) * 12.5
time_with_delay = time_for_the_distance + delay
if time_with_delay < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_with_delay:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_with_delay - record_in_seconds:.2f} seconds slower.")