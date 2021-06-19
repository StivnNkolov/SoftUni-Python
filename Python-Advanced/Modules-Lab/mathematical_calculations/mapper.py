from mathematical_calculations import logic
def calculations_mapper():
    mapper = {
        "+": logic.sum_numbers,
        "-": logic.subtract,
        "*": logic.multiply,
        "/": logic.divide,
        "^": logic.power,
    }
    return mapper