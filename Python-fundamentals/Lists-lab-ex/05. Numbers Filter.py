number_of_lines = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(number_of_lines):
    input_integers = int(input())
    if input_integers % 2 == 0:
        even_list.append(input_integers)
    if not input_integers % 2 == 0:
        odd_list.append(input_integers)
    if input_integers < 0:
        negative_list.append(input_integers)
    else:
        positive_list.append(input_integers)

command = input()
if command == "even":
    print(even_list)
elif command == "odd":
    print(odd_list)
elif command == "negative":
    print(negative_list)
elif command == "positive":
    print(positive_list)