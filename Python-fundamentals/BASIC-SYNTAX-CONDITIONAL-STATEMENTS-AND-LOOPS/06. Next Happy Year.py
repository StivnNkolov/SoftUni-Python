last_happy_year = int(input()) + 1

is_found = False

while not is_found:
    last_happy_year = str(last_happy_year)
    set_happy_ear = set(last_happy_year)
    if len(set_happy_ear) == len(last_happy_year):
        is_found = True
        print(last_happy_year)
        break
    last_happy_year = int(last_happy_year) + 1
