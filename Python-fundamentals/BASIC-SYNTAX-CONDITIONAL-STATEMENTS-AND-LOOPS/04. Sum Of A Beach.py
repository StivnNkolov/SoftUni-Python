input_data = input()

lower_case_input = input_data.lower()

sand_count = lower_case_input.count("sand")
water_count = lower_case_input.count("water")
fish_count = lower_case_input.count("fish")
sun_count = lower_case_input.count("sun")

count_of_words = sand_count + water_count + fish_count + sun_count
print(count_of_words)