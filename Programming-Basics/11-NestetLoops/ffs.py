n = int(input())
l = int(input())

for first in range(1, n + 1):
    for second in range(1, n + 1):
        for third in range(l):
            for fourth in range(l):
                for fifth in range(1, n + 1):
                    if first < fifth > second:
                        print(f"{first}{second}{chr(97 + third)}{chr(97 + fourth)}{fifth}", end=" ")