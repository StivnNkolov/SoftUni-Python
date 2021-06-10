def combination(data, result=0, expression=""):
    if not data:
        return [(expression, result)]

    plus_result = combination(data[1:], result + data[0], f"{expression}+{data[0]}")
    minus_result = combination(data[1:], result - data[0], f"{expression}-{data[0]}")
    return plus_result + minus_result


input_data = [int(el) for el in input().split(", ")]

[print(f"{el[0]}={el[1]}") for el in combination(input_data)]
