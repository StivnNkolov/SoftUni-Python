def string_concat(string, number):
    return string * number


input_string = input()
repeat_count = int(input())

print(string_concat(input_string, repeat_count))