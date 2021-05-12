input_data = float(input())

type_of_number = ''

if input_data == 0:
    print("zero")
if input_data > 0:
    type_of_number = "positive"
    if input_data < 1:
        type_of_number = "small positive"
    elif input_data > 1000000:
        type_of_number = "large positive"
elif input_data < 0:
    type_of_number = "negative"
    if abs(input_data) < 1:
        type_of_number = "small negative"
    elif abs(input_data) > 1000000:
        type_of_number = "large negative"


print(type_of_number)