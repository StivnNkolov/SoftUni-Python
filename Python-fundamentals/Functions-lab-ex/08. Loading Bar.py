def loading_bar(data):
    list1 = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    percent = data // 10
    for n in range(percent):
        list1[n] = "%"

    if percent == 10:
        print(f"100% Complete!")
        print(f"[{''.join(list1)}]")
    else:
        print(f"{input_data}% [{''.join(list1)}]")
        print("Still loading...")


input_data = int(input())
loading_bar(input_data)

# initial_list = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
# percentage = input_data // 10
#
# for num in range(percentage):
#     initial_list[num] = "%"
#
# if percentage == 10:
#     print(f"100% Complete!")
#     print(f"[{''.join(initial_list)}]")
# else:
#     print(f"{input_data}% [{''.join(initial_list)}]")
#     print("Still loading...")