input_data = input().split()

my_dict = {}

for word in input_data:
    for char in word:
        if char not in my_dict:
            my_dict[char] = 0
        my_dict[char] += 1

for key, value in my_dict.items():
    print(f"{key} -> {value}")
