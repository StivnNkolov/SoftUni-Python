def flights(*args):
    flights_list = args[:args.index("Finish")]
    flights_with_passengers_count_dict = {}
    for el in range(0, len(flights_list), 2):
        if not flights_list[el] in flights_with_passengers_count_dict:
            flights_with_passengers_count_dict[flights_list[el]] = 0
        flights_with_passengers_count_dict[flights_list[el]] += flights_list[el + 1]
    return flights_with_passengers_count_dict

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))