def numbers_searching(*args):
    sorted_data = sorted(args)
    duplicates = []
    searched_list = []

    data_with_unique_values = set(args)
    full_range_of_nums = [el for el in range(min(data_with_unique_values) + 1, max(data_with_unique_values) + 1)]
    difference = data_with_unique_values.symmetric_difference(full_range_of_nums)
    searched_list.append(max(difference))
    for el in sorted_data:

        if args.count(el) > 1 and el not in duplicates:
            duplicates.append(el)
            
    searched_list.append(duplicates)
    return searched_list


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
