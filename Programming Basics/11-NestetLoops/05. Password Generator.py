number = int(input())

for first in range(1, 10):
    for second in range(1, 10):
        for third in range(1, 10):
            for fourth in range(1, 10):
                if number % first == 0 and number % second == 0 and number % third == 0 and number % fourth == 0:
                    print(f"{first}{second}{third}{fourth}", end=" ")


for first in range(1, n)