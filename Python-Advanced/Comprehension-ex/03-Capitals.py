country_names = input().split(", ")
capital_name = input().split(", ")

for index in range(len(country_names)):
    print(f"{country_names[index]} -> {capital_name[index]}")