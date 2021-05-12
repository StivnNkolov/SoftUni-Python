input_data = int(input())

years = input_data * 100

days = years * 365.2422

hours = int(days) * 24

minutes = hours * 60

print(f"{input_data} centuries = {years} years = {int(days)} days = {hours} hours = {minutes} minutes")