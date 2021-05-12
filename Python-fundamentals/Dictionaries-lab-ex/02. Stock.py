input_data = input().split()

my_dict_with_p_q = {}

for index in range(0, len(input_data), 2):
    product = input_data[index]
    volume = int(input_data[index + 1])
    my_dict_with_p_q[product] = volume

products_to_search_for = input().split()
for product in products_to_search_for:
    if product in my_dict_with_p_q:
        print(f"We have {my_dict_with_p_q[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
