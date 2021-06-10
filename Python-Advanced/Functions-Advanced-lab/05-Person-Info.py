def get_info(**kwargs):
    name = kwargs['name']
    town = kwargs['town']
    age = kwargs['age']
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))