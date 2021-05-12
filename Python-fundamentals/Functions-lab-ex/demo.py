initial_array = [int(num) for num in input().split()]


command = input()

while True:
    even_nums = [num for num in initial_array if num % 2 == 0]
    odd_nums = [num for num in initial_array if not num % 2 == 0]
    command = command.split()
    if command[0] == "exchange":
        index = int(command[1])
        if not 0 <= index < len(initial_array):
            print("Invalid index")
        else:
            left_part = initial_array[:index + 1]
            right_part = initial_array[index + 1:]
            initial_array = right_part + left_part
    elif command[0] == "max":
        odd_or_even = command[1]
        if odd_or_even == "even":
            if not even_nums:
                print("No matches")
            else:
                max_even_number = max(even_nums)
                if even_nums.count(max_even_number) > 1:
                    result = [idx for idx, val in enumerate(initial_array) if val == max_even_number]
                    print(result[-1])
                else:
                    print(initial_array.index(max_even_number))
        elif odd_or_even == "odd":
            if not odd_nums:
                print("No matches")
            else:
                max_odd_num = max(odd_nums)
                if odd_nums.count(max_odd_num) > 1:
                    result = [idx for idx, val in enumerate(initial_array) if val == max_odd_num]
                    print(result[-1])
                else:
                    print(initial_array.index(max_odd_num))
    elif command[0] == "min":
        odd_or_even1 = command[1]
        if odd_or_even1 == "even":
            if not even_nums:
                print("No matches")
            else:
                min_even_num = min(even_nums)
                if even_nums.count(min_even_num) > 1:
                    result = [idx for idx, val in enumerate(initial_array) if val == min_even_num]
                    print(result[-1])
                else:
                    print(initial_array.index(min_even_num))
        elif odd_or_even1 == "odd":
            if not odd_nums:
                print("No matches")
            else:
                min_odd_num = min(odd_nums)
                if odd_nums.count(min_odd_num) > 1:
                    result = [idx for idx, val in enumerate(initial_array) if val == min_odd_num]
                    print(result[-1])
                else:
                    print(initial_array.index(min_odd_num))
    elif command[0] == "first":
        count = int(command[1])
        odd_or_even2 = command[2]
        if not count > len(initial_array):
            if odd_or_even2 == "even":
                if count >= len(even_nums):
                    print(even_nums)
                else:
                    part_to_be_printed = even_nums[:count]
                    print(part_to_be_printed)
            elif odd_or_even2 == "odd":
                if count >= len(odd_nums):
                    print(odd_nums)
                else:
                    part_to_be_printed = odd_nums[:count]
                    print(part_to_be_printed)
        else:
            print("Invalid count")
    elif command[0] == "last":
        count1 = int(command[1])
        odd_or_even3 = command[2]
        if not count1 > len(initial_array):
            if odd_or_even3 == "even":
                if count1 >= len(even_nums):
                    print(even_nums)
                else:
                    part_to_be_printed1 = even_nums[::-1]
                    part_to_be_printed1 = part_to_be_printed1[:count1]
                    print(part_to_be_printed1)
            elif odd_or_even3 == "odd":
                if count1 >= len(odd_nums):
                    print(odd_nums)
                else:
                    part_to_be_printed1 = odd_nums[::-1]
                    part_to_be_printed1 = part_to_be_printed1[:count1]
                    print(part_to_be_printed1)
    elif command[0] == "end":
        print(initial_array)
        break
    command = input()
