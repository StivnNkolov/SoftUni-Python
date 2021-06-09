country_names = input().split(", ")
capital_names = input().split(", ")

# for index in range(len(country_names)):
#     print(f"{country_names[index]} -> {capital_names[index]}")

my_dict = {country_names[index]: capital_names[index] for index in range(len(country_names))}

[print(f"{country} -> {capital}") for country, capital in my_dict.items()]
