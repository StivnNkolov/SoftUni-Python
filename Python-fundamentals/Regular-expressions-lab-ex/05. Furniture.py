import re

input_data = input()

bought_furniture = []
total_money_spend = 0
furniture = []

pattern = r">>(?P<Name>[A-Za-z]+)<<(?P<Price>[0-9]+\.?([0-9]+)?)\!(?P<Quantity>[0-9]+)"
while not input_data == "Purchase":
    bought_furniture = [obj.groupdict() for obj in re.finditer(pattern, input_data)]
    for furn in bought_furniture:
        furniture.append(furn["Name"])
        total_money_spend += float(furn["Price"]) * int(furn["Quantity"])
    input_data = input()

print(f"Bought furniture:")
if furniture:
    for f in furniture:
        print(f)
print(f"Total money spend: {total_money_spend:.2f}" )
#changing the new line with this comment



# import re
#
# pattern = r">>(?P<Name>[A-Za-z]+)<<(?P<Price>[0-9]+\.?([0-9]+)?)\!(?P<Quantity>[0-9]+)"
#
# line_of_input = input()
#
# furn_names = []
# total_money = 0
#
# while not line_of_input == "Purchase":
#     match = re.match(pattern, line_of_input)
#     if match:
#         furn_names.append(match["Name"])
#         total_money += float(match["Price"]) * int(match["Quantity"])
#     line_of_input = input()
#
# print("Bought furniture:")
# if furn_names:
#     for f in furn_names:
#         print(f)
# print(f"Total money spend: {total_money:.2f}")
