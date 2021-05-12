input_data = int(input())

for first in range(0, input_data):
    for second in range(0, input_data):
        for third in range(0, input_data):
            print(chr(97 + first) + chr(97 + second) + chr(97 + third))