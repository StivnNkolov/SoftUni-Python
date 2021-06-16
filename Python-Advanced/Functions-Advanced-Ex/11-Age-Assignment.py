def age_assignment(*args, **kwargs):
    names_ages_dict = {el: 0 for el in args}
    for el in names_ages_dict:
        for key, value in kwargs.items():
            if el.startswith(key):
                names_ages_dict[el] = value

    return names_ages_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
